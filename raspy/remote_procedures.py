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


def rasmgr_keep_alive(stub, cuuid, cid):
    return stub.KeepAlive(make_rasmgr_keep_alive_req(cuuid, cid), _TIMEOUT_SECONDS)


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


def rassrvr_begin_transaction(stub, cid, rw):
    return stub.BeginTransaction(make_rassrvr_begin_transaction_req(cid, rw), _TIMEOUT_SECONDS)


def rassrvr_commit_transaction(stub, cid):
    return stub.CommitTransaction(make_rassrvr_commit_transaction_req(cid), _TIMEOUT_SECONDS)


def rassrvr_abort_transaction(stub, cid):
    return stub.AbortTransaction(make_rassrvr_abort_transaction_req(cid), _TIMEOUT_SECONDS)


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


def rassrvr_get_collection_by_name(stub, cid, name):
    resp = stub.GetCollectionByNameOrOid(make_rassrvr_get_collection_req(cid, name), _TIMEOUT_SECONDS)
    if not resp:
        raise Exception("Remote function 'GetCollectionByNameOrOid' did not return anything")
    return resp


def rassrvr_keep_alive(stub, client_uuid, session_id):
    resp = stub.KeepAlive(make_rassrvr_keep_alive_req(client_uuid, session_id), _TIMEOUT_SECONDS)
    if not resp:
        raise Exception("Remote function 'KeepAlive' from RasServer did not return anything")
    return resp


def rassrvr_get_next_mdd(stub, cid):
    resp = stub.GetNextMDD(cid)
    if not resp:
        raise Exception("Remote function 'GetNextMDD' did not return anything")
    return resp


def rassrvr_get_next_tile(stub, cid):
    resp = stub.GetNextTile(cid)
    if not resp:
        raise Exception("Remote function 'GetNextTile' did not return anything")
    return resp
