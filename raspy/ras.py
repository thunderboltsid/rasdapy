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

# import numpy as np
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
        self.passwordHash = get_md5_string(password)
        self.channel = implementations.insecure_channel(hostname, port)
        self.stub = rasmgr.beta_create_RasMgrClientService_stub(self.channel)
        self.session = None
        self.connect()

    def disconnect(self):
        rasmgr_disconnect(self.stub, self.session.clientUUID, self.session.clientId)
        del self.session
        # TODO: Stop rasmgr_keep_alive

    def connect(self):
        self.session = rasmgr_connect(self.stub, self.username, self.passwordHash)
        # TODO: Keep running the rasmgr_keep_alive on a separate thread
        # rasmgr_keep_alive(self.stub, self.session.clientUUID, self.session.clientId)

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
        self.open()
        self.stub = rassrvr.beta_create_ClientRassrvrService_stub(self.connection.channel)

    def open(self):
        self.rasmgr_db = rasmgr_open_db(self.connection.stub, self.connection.session.clientUUID,
                                 self.connection.session.clientId, self.name)
        self.rassrvr_db = rassrvr_open_db(self.stub, self.connection.session.clientId, self.name)
        # TODO: Stop sending rasmgr_keep_alive messages
        # TODO: Start sending rassrvr_keep_alive messages

    def close(self):
        rasmgr_close_db(self.connection.stub, self.connection.session.clientUUID, self.connection.session.clientId,
                        self.rasmgr_db.dbSessionId)

    def transaction(self, rw=True):
        """
        Returns a new transaction object for this database
        :rtype: Transaction
        :return: a new transaction object
        """
        transaction = Transaction(self, rw=rw)
        return transaction

    def collections(self):
        """
        Returns all the collections for this database
        :rtype: list[Collection]
        """
        transaction = self.transaction()
        query = transaction.query("select r from RAS_COLLECTIONNAMES as r")
        result = query.execute()
        collection = [rassrvr_get_collection_by_name(self.stub, self.connection.session.clientId, name) for name in
                      result]
        return collection


class Collection:
    def __init__(self, transaction, name=None):
        """
        Constructor for the class
        :param Transaction transaction: the transaction for which the collections should be returned
        """
        self.transaction = transaction
        if name:
            self.data = rassrvr_get_collection_by_name(self.transaction.database.stub,
                                                      self.transaction.database.connection.session.clientId, name)

    def name(self):
        """
        Returns the name of the collection
        :rtype: str
        """
        pass

    def arrays(self):
        """
        Return all the arrays in this collection
        :rtype: Array
        """
        pass

    def insert(self, array):
        """
        Inserts an array in the collection
        :param Array array: the array to be inserted
        """
        pass

    def update(self, array):
        """
        Updates the array in the collection
        :param Array array: the array to be updated in the collection
        """


class Transaction:
    def __init__(self, database, rw=False):
        """
        Class to represent a transaction on the selected database
        :param Database database: the database to which the transaction is bound to
        """
        self.database = database
        self.rw = rw
        self.begin_transaction()

    def begin_transaction(self):
        rassrvr_begin_transaction(self.database.stub, self.database.connection.session.clientId, self.rw)

    def commit_transaction(self):
        rassrvr_commit_transaction(self.database.stub, self.database.connection.session.clientId)

    def abort_transaction(self):
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

    def execute(self, buffer_size=1048576):
        """
        Executes the query and returns back a result
        :return: the resulting array returned by the query
        :rtype: Array
        """
        result = rassrvr_execute_query(self.transaction.database.stub,
                                      self.transaction.database.connection.session.clientId, self.query_str)
        if result.status == 0 or result.status == 1:
            pass
        elif result.status == 4 or result.status == 5:
            raise Exception("Error executing query: err_no = " + str(result.err_no) + ", line_no = " + str(
                result.line_no) + ", col_no = " + str(result.col_no) + ", token = " + result.token)
        mddstatus = 0
        res = []
        while mddstatus == 0:
            array = []
            metadata = []
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
                array.append((tileresp.data, tileresp.data_length))
            if tilestatus == 0:
                break
            res.append(array)
        return Array(values=res, metadata=result)


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

    def toArray(self, type="numpy"):
        """
        Returns the serialized array as a numpy, scipy, or pandas data structure
        :param type: valid option - "numpy", "scipy", "pandas"
        :return:
        """
        if type == "numpy":
            return np.frombuffer(self.values)
        elif type == "scipy":
            return sparse.csr_matrix(np.frombuffer(self.values))
        elif type == "pandas":
            raise NotImplementedError("No Support for Pandas yet")
        else:
            raise NotImplementedError("Invalid type: only valid types are 'numpy' (default), 'scipy', and 'pandas'")
