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

from request_factories import *

_TIMEOUT_SECONDS = 30


def rasmgr_connect(stub, username, password):
    connection = stub.Connect(make_rasmgr_connect_req(username, password), _TIMEOUT_SECONDS)
    if not connection:
        raise Exception("Remote function 'Connect' did not return anything")
    return connection


def rasmgr_disconnect(stub, cuuid, cid):
    return stub.Disconnect(make_rasmgr_disconnect_req(cuuid, cid), _TIMEOUT_SECONDS)


def rasmgr_keep_alive(stub, cuuid):
    return stub.KeepAlive(make_rasmgr_keep_alive_req(cuuid), _TIMEOUT_SECONDS)


def rasmgr_open_db(stub, cuuid, cid, dbname):
    resp = stub.OpenDb(make_rasmgr_open_db_req(cuuid, cid, dbname), _TIMEOUT_SECONDS)
    if not resp:
        raise Exception("Remote function 'OpenDb' did not return anything")
    return resp


def rasmgr_close_db(stub, cuuid, cid, dbid):
    return stub.CloseDb(make_rasmgr_close_db_req(cuuid, cid, dbid), _TIMEOUT_SECONDS)


# Start RasServer RPCs


def rassrvr_open_db(stub, cid, dbname):
    resp = stub.OpenServerDatabase(make_rassrvr_open_db_req(cid, dbname), _TIMEOUT_SECONDS)
    if not resp:
        raise Exception("Remote function 'OpenDB' did not return anything")
    return resp


def rassrvr_close_db(stub, cid):
    return stub.CloseServerDatabase(make_rassrvr_close_db_req(cid), _TIMEOUT_SECONDS)


def rassrvr_create_db(stub, cid, dbname):
    return stub.CreateDatabase(make_rassrvr_create_db_req(cid, dbname), _TIMEOUT_SECONDS)


def rassrvr_destroy_db(stub, cid, dbname):
    return stub.DestroyDatabase(make_rassrvr_destroy_db_req(cid, dbname), _TIMEOUT_SECONDS)


def rassrvr_begin_transaction(stub, cid, rw):
    return stub.BeginTransaction(make_rassrvr_begin_transaction_req(cid, rw), _TIMEOUT_SECONDS)


def rassrvr_commit_transaction(stub, cid):
    return stub.CommitTransaction(make_rassrvr_commit_transaction_req(cid), _TIMEOUT_SECONDS)


def rassrvr_abort_transaction(stub, cid):
    return stub.AbortTransaction(make_rassrvr_abort_transaction_req(cid), _TIMEOUT_SECONDS)


def rassrvr_is_transaction_open(stub, cid):
    resp = stub.IsTransactionOpen(make_rassrvr_is_transaction_open_req(cid), _TIMEOUT_SECONDS)
    if not resp:
        raise Exception("Remote function 'IsTransactionOpen' did not return anything")
    return resp


def rassrvr_start_insert_mdd(stub, cid, coll_name, domain, type_len, type_name, oid):
    resp = stub.StartInsertMDD(make_rassrvr_start_insert_mdd(cid, coll_name, domain, type_len, type_name, oid),
                               _TIMEOUT_SECONDS)
    if not resp:
        raise Exception("Remote function 'StartInsertMDD' did not return anything")
    return resp


def rassrvr_start_insert_trans_mdd(stub, cid, domain, type_len, type_name):
    resp = stub.StartInsertTransMDD(make_rassrvr_start_insert_trans_mdd(cid, domain, type_len, type_name),
                                    _TIMEOUT_SECONDS)
    if not resp:
        raise Exception("Remote function 'StartInsertTransMDD' did not return anything")
    return resp


def rassrvr_insert_tile(stub, cid, persistent, domain, type_len, current_format, storage_format, data, data_len):
    resp = stub.InsertTile(
        make_rassrvr_insert_tile_req(cid, persistent, domain, type_len, current_format, storage_format, data, data_len),
        _TIMEOUT_SECONDS)
    if not resp:
        raise Exception("Remote function 'InsertTile' did not return anything")
    return resp


def rassrvr_end_insert_mdd(stub, cid, persistence):
    resp = stub.InsertMDD(rassrvr_end_insert_mdd(cid, persistence), _TIMEOUT_SECONDS)
    if not resp:
        raise Exception("Remote function 'EndInsertMDD' failed")
    return resp


def rassrvr_insert_collection(stub, cid, coll_name, type_name, oid):
    resp = stub.InsertCollection(rassrvr_insert_collection(cid, coll_name, type_name, oid), _TIMEOUT_SECONDS)
    if not resp:
        raise Exception("Remote function 'InsertCollection' failed")
    return resp


def rassrvr_delete_collection_by_name(stub, cid, coll_name):
    resp = stub.DeleteCollectionByName(make_rassrvr_delete_collection_by_name_req(cid, coll_name), _TIMEOUT_SECONDS)
    if not resp:
        raise Exception("Remote function 'DeleteCollectionByName' failed")
    return resp


def rassrvr_delete_collection_by_id(stub, cid, oid):
    resp = stub.DeleteCollectionByOid(make_rassrvr_delete_collection_by_name_req(cid, oid), _TIMEOUT_SECONDS)
    if not resp:
        raise Exception("Remote function 'DeleteCollectionByOid' failed")
    return resp


def rassrvr_remove_object_from_collection(stub, cid, coll_name, oid):
    resp = stub.RemoveObjectFromCollection(make_rassrvr_remove_object_from_collection_req(cid, coll_name, oid),
                                           _TIMEOUT_SECONDS)
    if not resp:
        raise Exception("Remote function 'RemoveObjectFromCollection' failed")
    return resp


def rassrvr_get_collection_by_name(stub, cid, name):
    resp = stub.GetCollectionByNameOrOid(make_rassrvr_get_collection_by_name_or_id_req(cid, name, True),
                                         _TIMEOUT_SECONDS)
    if not resp:
        raise Exception("Remote function 'GetCollectionByNameOrOid' did not return anything")
    return resp


def rassrvr_get_collection_by_id(stub, cid, oid):
    resp = stub.GetCollectionByNameOrOid(make_rassrvr_get_collection_by_name_or_id_req(cid, oid, False),
                                         _TIMEOUT_SECONDS)
    if not resp:
        raise Exception("Remote function 'GetCollectionByNameOrOid' did not return anything")
    return resp


def rassrvr_get_collection_oids_by_id(stub, cid, coll_id):
    resp = stub.GetCollOidsByNameOrOid(make_rassrvr_get_collection_oids_by_name_or_id(cid, coll_id, False),
                                       _TIMEOUT_SECONDS)
    if not resp:
        raise Exception("Remote function 'GetCollOidsByNameOrOid' did not return anything")
    return resp


def rassrvr_get_collection_oids_by_name(stub, cid, coll_name):
    resp = stub.GetCollOidsByNameOrOid(make_rassrvr_get_collection_oids_by_name_or_id(cid, coll_name, True),
                                       _TIMEOUT_SECONDS)
    if not resp:
        raise Exception("Remote function 'GetCollOidsByNameOrOid' did not return anything")
    return resp


def rassrvr_execute_query(stub, cid, query):
    resp = stub.ExecuteQuery(make_rassrvr_execute_query_req(cid, query), _TIMEOUT_SECONDS)
    if not resp:
        raise Exception("Remote function 'ExecuteQuery' did not return anything")
    return resp


def rassrvr_execute_http_query(stub, cid, data, data_length):
    resp = stub.ExecuteHttpQuery(make_rassrvr_execute_http_query_req(cid, data, data_length), _TIMEOUT_SECONDS)
    if not resp:
        raise Exception("Remote function 'ExecuteHttpQuery' did not return anything")
    return resp


def rassrvr_keep_alive(stub, client_uuid, session_id):
    resp = stub.KeepAlive(make_rassrvr_keep_alive_req(client_uuid, session_id), _TIMEOUT_SECONDS)
    if not resp:
        raise Exception("Remote function 'KeepAlive' from RasServer did not return anything")
    return resp


def rassrvr_get_next_mdd(stub, cid):
    resp = stub.GetNextMDD(make_rassrvr_get_next_mdd_req(cid), _TIMEOUT_SECONDS)
    if not resp:
        raise Exception("Remote function 'GetNextMDD' did not return anything")
    return resp


def rassrvr_get_next_tile(stub, cid):
    resp = stub.GetNextTile(make_rassrvr_get_next_tile_req(cid), _TIMEOUT_SECONDS)
    if not resp:
        raise Exception("Remote function 'GetNextTile' did not return anything")
    return resp


def rassrvr_end_transfer(stub, cid):
    resp = stub.EndTransfer(make_rassrvr_end_transfer_req(cid), _TIMEOUT_SECONDS)
    if not resp:
        raise Exception("Remote function 'EndTransfer' did not return anything")
    return resp
