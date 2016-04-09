"""
 *
 * This file is part of rasdaman community.
 *
 * Rasdaman community is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * Rasdaman community is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
 * See the GNU  General Public License for more details.
 *
 * You should have received a copy of the GNU  General Public License
 * along with rasdaman community.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Copyright 2003 - 2016 Peter Baumann / rasdaman GmbH.
 *
 * For more information please see <http://www.rasdaman.org>
 * or contact Peter Baumann via <baumann@rasdaman.com>.
 *
"""

import numpy as np
import signal, os
from grpc.beta import implementations
# from scipy import sparse
from utils import *
from remote_procedures import *


class Connection:
    def __init__(self, hostname="0.0.0.0", port=7001, username="rasguest", password="rasguest"):
        """
        Class to represent the connection from the python client to the rasdaman server
        :param str hostname: the hostname of the rasdaman server
        :param int port: the port on which rasdaman listens on
        """
        self.hostname = hostname
        self.port = port
        self.username = username
        self.password = password
        self.channel = implementations.insecure_channel(hostname, port)
        self.stub = rasmgr.beta_create_RasMgrClientService_stub(self.channel)
        self.session = None
        self._rasmgr_keep_alive_running = None
        self._keep_alive_thread = None
        self.connect()

    def disconnect(self):
        self._stop_keep_alive()
        rasmgr_disconnect(self.stub, self.session.clientUUID, self.session.clientId)
        self.session = None
        # TODO: Stop rasmgr_keep_alive

    def connect(self):
        self.session = rasmgr_connect(self.stub, self.username, self.password)
        self._keep_alive()
        # TODO: Keep running the rasmgr_keep_alive on a separate thread

    def _keep_alive(self):
        if not self._rasmgr_keep_alive_running:
            self._rasmgr_keep_alive_running = True
            if not self._keep_alive_thread:
                self._keep_alive_thread = StoppableTimeoutThread(rasmgr_keep_alive,
                                                                 self.session.keepAliveTimeout / 2000,
                                                                 self.stub, self.session.clientUUID)
                self._keep_alive_thread.start()
        else:
            raise Exception("RasMgrKeepAlive already running")

    def _stop_keep_alive(self):
        if self._rasmgr_keep_alive_running is not None:
            self._rasmgr_keep_alive_running = None
            if self._keep_alive_thread is not None:
                self._keep_alive_thread.stop()
                self._keep_alive_thread.join()
                self._keep_alive_thread = None
            else:
                raise Exception("No thread named _keep_alive_thread to stop")
        else:
            raise Exception("rasmgr_keep_alive thread not running")

    def database(self, name):
        """
        Returns a database object initialized with this connection
        :rtype: Database
        :return: a new database object
        """
        database = Database(self, name)
        return database


class Database:
    def __init__(self, connection, name):
        """
        Class to represent a database stored inside a rasdaman server
        :param Connection connection: the connection to the rasdaman server
        :param str name: the name of the database
        """
        self.connection = connection
        self.name = name
        self.rasmgr_db = None
        self.rassrvr_db = None
        self.channel = None
        self.stub = None
        self._rassrvr_keep_alive_running = None
        self._keep_alive_thread = None
        self.open()

    def open(self):
        self.rasmgr_db = rasmgr_open_db(self.connection.stub, self.connection.session.clientUUID,
                                        self.connection.session.clientId, self.name)
        if self.rasmgr_db.dbSessionId == self.connection.session.clientUUID:
            self.connection._stop_keep_alive()
        self.channel = implementations.insecure_channel(self.rasmgr_db.serverHostName, self.rasmgr_db.port)
        self.stub = rassrvr.beta_create_ClientRassrvrService_stub(self.channel)
        self.rassrvr_db = rassrvr_open_db(self.stub, self.connection.session.clientId, self.name)
        self._keep_alive()

    def close(self):
        self._stop_keep_alive()
        rassrvr_close_db(self.stub, self.connection.session.clientId)
        rasmgr_close_db(self.connection.stub, self.connection.session.clientUUID, self.connection.session.clientId,
                        self.rasmgr_db.dbSessionId)

    def create(self):
        raise NotImplementedError("Sorry, not implemented yet")

    def destroy(self):
        raise NotImplementedError("Sorry, not implemented yet")

    def transaction(self, rw=False):
        """
        Returns a new transaction object for this database
        :rtype: Transaction
        :return: a new transaction object
        """
        transaction = Transaction(self, rw=rw)
        return transaction

    @property
    def collections(self):
        """
        Returns all the collections for this database
        :rtype: list[Collection]
        """
        transaction = self.transaction()
        query = transaction.query("select r from RAS_COLLECTIONNAMES as r")
        result = query._execute_read()
        collection = [rassrvr_get_collection_by_name(self.stub, self.connection.session.clientId, name) for name in
                      result]
        return collection

    def _keep_alive(self):
        if not self._rassrvr_keep_alive_running:
            self._rassrvr_keep_alive_running = True
            if not self._keep_alive_thread:
                self._keep_alive_thread = StoppableTimeoutThread(rassrvr_keep_alive,
                                                                 self.connection.session.keepAliveTimeout / 2000,
                                                                 self.stub, self.connection.session.clientUUID,
                                                                 self.rasmgr_db.dbSessionId)
                self._keep_alive_thread.start()
        else:
            raise Exception("RasSrvrKeepAlive already running")

    def _stop_keep_alive(self):
        if self._rassrvr_keep_alive_running is not None:
            self._rassrvr_keep_alive_running = None
            if self._keep_alive_thread is not None:
                self._keep_alive_thread.stop()
                self._keep_alive_thread.join()
                self._keep_alive_thread = None
            else:
                raise Exception("No thread named _keep_alive_thread to stop")
        else:
            raise Exception("rassrvr_keep_alive thread not running")


class Collection:
    def __init__(self, transaction, name=None, type=None, oid=None):
        """
        Constructor for the class
        :param Transaction transaction: the transaction for which the collections should be returned
        """
        self.transaction = transaction
        self.name = name
        self.type_name = type
        self.type_structure = None
        self.oid = oid

    @property
    def name(self):
        """
        Returns the name of the collection
        :rtype: str
        """
        return self.name

    def array(self):
        """
        Return the arrays in this collection
        :rtype: Array
        """
        resp = rassrvr_get_collection_by_name(self.transaction.database.stub,
                                              self.transaction.database.connection.session.clientId, self.name)
        return resp

    def create(self):
        resp = rassrvr_insert_collection(self.transaction.database.stub,
                                         self.transaction.database.connection.session.clientId, self.name,
                                         self.type_name, self.oid)
        import pdb;
        pdb.set_trace()
        if resp.status == 0:
            return resp.status
        elif resp.status == 1 or resp.status == 3:
            raise Exception("Error: Unknown Client. Status: " + str(resp.status))
        elif resp.status == 2:
            raise Exception("Error: Unknown Object. Status: " + str(resp.status))
        else:
            raise Exception("Error: Unknown Error. Status: " + str(resp.status))

    def delete_by_name(self):
        resp = rassrvr_delete_collection_by_name(self.transaction.database.stub,
                                                 self.transaction.database.connection.session.clientId, self.name)
        if resp.status == 0:
            return resp.status
        elif resp.status == 1 or resp.status == 3:
            raise Exception("Error: Unknown Client. Status: " + str(resp.status))
        elif resp.status == 2:
            raise Exception("Error: Unknown Object. Status: " + str(resp.status))
        else:
            raise Exception("Error: Unknown Error. Status: " + str(resp.status))

    def delete_by_id(self):
        resp = rassrvr_delete_collection_by_id(self.transaction.database.stub,
                                               self.transaction.database.connection.session.clientId, self.oid)
        if resp.status == 0:
            return resp.status
        elif resp.status == 1 or resp.status == 3:
            raise Exception("Error: Unknown Client. Status: " + str(resp.status))
        elif resp.status == 2:
            raise Exception("Error: Unknown Object. Status: " + str(resp.status))
        else:
            raise Exception("Error: Unknown Error. Status: " + str(resp.status))

    def insert(self, array):
        """
        Inserts an array in the collection
        :param Array array: the array to be inserted
        """
        if self.transaction.rw is not True:
            raise Exception("Transaction is read only. Can't insert MDD")

    @name.setter
    def name(self, value):
        self._name = value


class Transaction:
    def __init__(self, database, rw=False):
        """
        Class to represent a transaction on the selected database
        :param Database database: the database to which the transaction is bound to
        """
        self.database = database
        self.rw = rw
        self.begin()

    def begin(self):
        rassrvr_begin_transaction(self.database.stub, self.database.connection.session.clientId, self.rw)

    def commit(self):
        rassrvr_commit_transaction(self.database.stub, self.database.connection.session.clientId)

    def abort(self):
        rassrvr_abort_transaction(self.database.stub, self.database.connection.session.clientId)

    def query(self, query_str):
        """
        Returns a new query object initialized with this transaction and the query string
        :param str query_str: the query to be executed
        :rtype: Query
        :return: a new query object
        """
        query = Query(self, query_str)
        return query

    def get_collection(self, name):
        """
        Returns a Collection object using this transaction
        :param name: name of the collection
        :return:
        """
        collection = Collection(self, name)
        if not collection:
            raise Exception("Can't get or create Collection from name")
        return collection


class Query:
    def __init__(self, transaction, query_str):
        """
        Class to represent a rasql query that can be executed in a certain transaction
        :param transaction: the transaction to which the query is bound to
        :param query_str: the query as a string
        """
        self.transaction = transaction
        self.query_str = query_str
        self.mdd_constants = None
        self.exec_query_resp = None

    def eval(self):
        if "insert" in self.query_str:
            self._execute_update()
        elif "create" in self.query_str:
            self._execute_update()
        elif "drop" in self.query_str:
            self._execute_update()
        else:
            return self._execute_read()

    def _execute_update(self):
        if self.transaction.rw is False:
            raise Exception("Transaction does now have write access")

        if self.mdd_constants is not None:
            pass

        exec_update_query_resp = rassrvr_execute_update_query(self.transaction.database.stub,
                                                              self.transaction.database.connection.session.clientId,
                                                              self.query_str)
        if exec_update_query_resp.status == 2 or exec_update_query_resp.status == 3:
            raise Exception(
                "Error executing query: err_no = " + str(exec_update_query_resp.erroNo) + ", line_no = " + str(
                    exec_update_query_resp.lineNo) + ", col_no = " + str(
                    exec_update_query_resp.colNo) + ", token = " + exec_update_query_resp.token)
        if exec_update_query_resp.status == 1:
            raise Exception("Error: Unknown Client")
        if exec_update_query_resp.status > 3:
            raise Exception("Error: Transfer failed")
        return exec_update_query_resp.status

    def _execute_read(self):
        """
        Executes the query and returns back a result
        :return: the resulting array returned by the query
        :rtype: Array
        """
        exec_query_resp = rassrvr_execute_query(self.transaction.database.stub,
                                                self.transaction.database.connection.session.clientId, self.query_str)
        self.exec_query_resp = exec_query_resp
        if exec_query_resp.status == 4 or exec_query_resp.status == 5:
            raise Exception("Error executing query: err_no = " + str(exec_query_resp.err_no) + ", line_no = " + str(
                exec_query_resp.line_no) + ", col_no = " + str(
                exec_query_resp.col_no) + ", token = " + exec_query_resp.token)
        elif exec_query_resp.status == 0:
            return self._get_next_collection()
        elif exec_query_resp.status == 1:
            return self._get_next_element()
        elif exec_query_resp.status == 2:
            raise Exception("Query returned an empty collection")
        else:
            raise Exception("Unknown status code returned by ExecuteQuery")

    def _get_next_collection(self):
        mddstatus = 0
        tilestatus = 0
        array = []
        metadata = ArrayMetadata(spatial_domain=self.exec_query_resp.type_structure,
                                 band_types=get_type_structure_from_string(self.exec_query_resp.type_structure))
        while mddstatus == 0:
            mddresp = rassrvr_get_next_mdd(self.transaction.database.stub,
                                           self.transaction.database.connection.session.clientId)
            mddstatus = mddresp.status
            if mddstatus == 2:
                raise Exception("getMDDCollection - no transfer or empty collection")
            tilestatus = 2
            while tilestatus == 2 or tilestatus == 3:
                tileresp = rassrvr_get_next_tile(self.transaction.database.stub,
                                                 self.transaction.database.connection.session.clientId)
                tilestatus = tileresp.status
                if tilestatus == 4:
                    raise Exception("rpcGetNextTile - no tile to transfer or empty collection")
                else:
                    array.append(RPCMarray(domain=tileresp.domain,
                                           cell_type_length=tileresp.cell_type_length,
                                           current_format=tileresp.current_format,
                                           storage_format=tileresp.storage_format,
                                           data=convert_data_stream_from_bin(
                                               metadata.band_types,
                                               tileresp.data,
                                               tileresp.data_length,
                                               tileresp.cell_type_length)))

            if tilestatus == 0:
                break
        rassrvr_end_transfer(self.transaction.database.stub, self.transaction.database.connection.session.clientId)
        return Array(values=array, metadata=metadata)

    def _get_next_element(self):
        rpcstatus = 0
        array = []
        metadata = ArrayMetadata(spatial_domain=self.exec_query_resp.type_structure,
                                 band_types=get_type_structure_from_string(self.exec_query_resp.type_structure))
        while rpcstatus == 0:
            elemresp = rassrvr_get_next_element(self.transaction.database.stub,
                                                self.transaction.database.connection.session.clientId)
            rpcstatus = elemresp.status
            if rpcstatus == 2:
                raise Exception("getNextElement - no transfer or empty element")
            array.append(convert_data_stream_from_bin(metadata.band_types, elemresp.data, elemresp.data_length,
                                                      elemresp.data_length)[0])
        return Array(metadata=metadata, values=array)

    def _send_mdd_constants(self):
        exec_init_update_resp = rassrvr_init_update(self.transaction.database.stub,
                                                    self.transaction.database.connection.session.clientId)
        if exec_init_update_resp.status is not 1:
            raise Exception("Error: Transfer Failed. ExecInitUpdate returned with a non-zero status: " + str(
                exec_init_update_resp.status))

        for mdd in self.mdd_constants:
            insert_trans_mdd_resp = rassrvr_start_insert_trans_mdd(self.transaction.database.stub,
                                                                   self.transaction.database.connection.session.clientId,
                                                                   mdd.domain, mdd.type_length, mdd.type_name)
            if insert_trans_mdd_resp.status is 0:
                insert_tile_resp = rassrvr_insert_tile(self.transaction.database.stub,
                                                       self.transaction.database.connection.session.clientId,
                                                       self.transaction.rw,
                                                       mdd.domain, mdd.type_length, mdd.current_format,
                                                       mdd.storage_format, mdd.data,
                                                       mdd.data_length)
                if insert_tile_resp.status > 0:
                    raise Exception("Error: Transfer failed")
            elif insert_trans_mdd_resp.status is 2:
                raise Exception("Error: Database Class Undefined")
            elif insert_trans_mdd_resp.status is 3:
                raise Exception("Error: Invalid Type")
            else:
                raise Exception("Error: Transfer failed")


class RPCMarray:
    """
    Class to represent RPC Array
    """

    def __init__(self, domain=None, cell_type_length=None, current_format=None, storage_format=None, data=None):
        self.domain = domain
        self.cell_type_length = cell_type_length
        self.current_format = current_format
        self.storage_format = storage_format
        self.data = data

    def to_array(self):
        if type == "numpy":
            return np.frombuffer(self.data)
        elif type == "scipy":
            return sparse.csr_matrix(np.frombuffer(self.data))
        elif type == "pandas":
            raise NotImplementedError("No Support for Pandas yet")
        else:
            raise NotImplementedError("Invalid type: only valid types are 'numpy' (default), 'scipy', and 'pandas'")


class BandType:
    """
    Enum containing possible band types in rasdaman
    """
    INVALID = 0,
    CHAR = 1,
    USHORT = 2,
    SHORT = 3,
    ULONG = 4,
    LONG = 5,
    FLOAT = 6,
    DOUBLE = 7


class SpatialDomain:
    def __init__(self, *interval_parameters):
        """
        Class to represent a spatial domain in rasdaman
        :param list[tuple] interval_parameters: a list of intervals represented as tuples
        """
        pass


class ArrayMetadata:
    def __init__(self, spatial_domain, band_types):
        """
        Class to represent the metadata associated to an array
        :param SpatialDomain spatial_domain: the spatial domain in which the array is represented
        :param dict[str, BandType] band_types: a dictionary containing the name of each band and its type
        """
        self.spatial_domain = spatial_domain
        self.band_types = band_types


class Array:
    def __init__(self, metadata=None, values=None):
        """
        Class to represent an array produced by a rasdaman query
        :param ArrayMetadata metadata: the metadata of the array
        :param list[list[int | float]] values: the values of the array stored band-interleaved (we store a list of
        values for each band)
        """
        self.metadata = metadata
        self.values = values

    def __getitem__(self, item):
        """
        Operator overloading for [], it will slice the array on the first dimension available
        :param slice | int item: the slicing index
        :return: an array with one less dimensions
        :rtype: Array
        """
        pass

    def subset(self, spatial_domain):
        """
        Subsets the array based on the given spatial domain
        :param SpatialDomain spatial_domain: the spatial domain to restrict to
        :rtype: Array
        """
        pass

    def get(self):
        """
        Returns the array contents as a one dimensional list containing a tuple of each band value for the array cell
        :rtype: list[tuple(int | float)]
        """
        pass

    def point(self, *dimension_indices):
        """
        Returns the point at the given position
        :param list[int] dimension_indices: the indices on each of the existing axis. If one of the dimension index is
        not given, an exception should be thrown
        :rtype: int | float
        """

    def to_array(self, type="numpy"):
        """
        Returns the serialized array as a numpy, scipy, or pandas data structure
        :param type: valid option - "numpy", "scipy", "pandas"
        :return:
        """
        if type == "numpy":
            nparr = np.array([val.data for val in self.values])
            return nparr
        elif type == "scipy":
            return sparse.csr_matrix(np.frombuffer(self.values))
        elif type == "pandas":
            raise NotImplementedError("No Support for Pandas yet")
        else:
            raise NotImplementedError("Invalid type: only valid types are 'numpy' (default), 'scipy', and 'pandas'")


class RasCollection:
    def __init__(self, name):
        self._expression = None
        self._collection = name
        self._condition = None
        self._query = None

    @property
    def query(self):
        return self._query

    def __add__(self, other):
        pass

    def __radd__(self, other):
        """
        Reflected addition is the same as addition.
        :param other:
        :return regular addition:
        """
        return self.__add__(other)

    def __iadd__(self, other):
        pass

    def __sub__(self, other):
        pass

    def __rsub__(self, other):
        pass

    def __isub__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __rmul__(self, other):
        pass

    def __imul__(self, other):
        pass

    def __div__(self, other):
        pass

    def __rdiv__(self, other):
        pass

    def __idiv__(self, other):
        pass

    @query.setter
    def query(self, value):
        self._query = value


class RasExpression:
    def __init__(self, operation=None, left=None, right=None, parent=None):
        self._operation = operation
        self._left = left
        self._right = right
        self._parent = parent

    def add_left(self, left):
        self._left = left

    def add_right(self, right):
        self._right = right

    def add_operation(self, operation):
        self._operation = operation

    def add_parent(self, parent):
        self._parent = parent
