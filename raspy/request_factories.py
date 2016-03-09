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

from stubs import client_rassrvr_service_pb2 as rassrvr
from stubs import rasmgr_client_service_pb2 as rasmgr
from utils import get_md5_string


def make_rasmgr_connect_req(username, password):
    passwordHash = get_md5_string(password)
    con_req = rasmgr.ConnectReq(userName=username, passwordHash=passwordHash)
    if not con_req:
        raise Exception("Can't create Connect request")
    return con_req


def make_rasmgr_disconnect_req(cuiid, cid):
    discon_req = rasmgr.DisconnectReq(clientUUID=cuiid, clientId=cid)
    if not discon_req:
        raise Exception("Can't create Disconnect request")
    return discon_req


def make_rasmgr_keep_alive_req(cuiid):
    keep_alive_req = rasmgr.KeepAliveReq(clientUUID=cuiid)
    if not keep_alive_req:
        raise Exception("Can't create KeepAlive request")
    return keep_alive_req


def make_rasmgr_open_db_req(cuiid, cid, dbname):
    open_db_req = rasmgr.OpenDbReq(clientUUID=cuiid, clientId=cid, databaseName=dbname)
    if not open_db_req:
        raise Exception("Can't create OpenDb request")
    return open_db_req


def make_rasmgr_close_db_req(cuuid, cid, dbsid):
    close_db_req = rasmgr.CloseDbReq(clientUUID=cuuid, clientId=cid, dbSessionId=dbsid)
    if not close_db_req:
        raise Exception("Can't create CloseDb request")
    return close_db_req


# Start RasServer request creation


def make_rassrvr_open_db_req(cid, dbname):
    open_db_req = rassrvr.OpenServerDatabaseReq(client_id=cid, database_name=dbname)
    if not open_db_req:
        raise Exception("Can't create OpenDB request for Rassrvr")
    return open_db_req


def make_rassrvr_close_db_req(cid):
    close_db_req = rassrvr.CloseServerDatabaseReq(client_id=cid)
    if not close_db_req:
        raise Exception("Can't create CloseDB request for Rassrvr")
    return close_db_req


def make_rassrvr_keep_alive_req(cuuid, dbsid):
    return rassrvr.KeepAliveRequest(client_uuid=cuuid, session_id=dbsid)


def make_rassrvr_begin_transaction_req(cid, rw):
    begin_transaction_req = rassrvr.BeginTransactionReq(client_id=cid, rw=rw)
    if not begin_transaction_req:
        raise Exception("Can't create BeginTransaction request")
    return begin_transaction_req


def make_rassrvr_commit_transaction_req(cid):
    commit_transaction_req = rassrvr.CommitTransactionReq(client_id=cid)
    if not commit_transaction_req:
        raise Exception("Can't create CommitTransaction request")
    return commit_transaction_req


def make_rassrvr_abort_transaction_req(cid):
    abort_transaction_req = rassrvr.AbortTransactionReq(client_id=cid)
    if not abort_transaction_req:
        raise Exception("Can't create AbortTransaction request")
    return abort_transaction_req


def make_rassrvr_execute_query_req(cid, query):
    execute_query_req = rassrvr.ExecuteQueryReq(client_id=cid, query=query)
    if not execute_query_req:
        raise Exception("Can't create ExecuteQuery request")
    return execute_query_req


def make_rassrvr_execute_http_query_req(cid, data, data_length):
    execute_http_query_req = rassrvr.ExecuteHttpQueryReq(client_id=cid, data=data, data_length=data_length)
    if not execute_http_query_req:
        raise Exception("Can't create ExecuteHttpQuery request")
    return execute_http_query_req


def make_rassrvr_get_collection_req(cid, colid):
    get_collection_req = rassrvr.GetCollectionByNameOrOidReq(client_id=cid, collection_identifier=colid, is_name=True)
    if not get_collection_req:
        raise Exception("Can't create GetCollectionByNameOrOid request")
    return get_collection_req


def make_rassrvr_get_next_mdd_req(cid):
    get_next_mdd_req = rassrvr.GetNextMDDReq(client_id=cid)
    if not get_next_mdd_req:
        raise Exception("Can't create GetNextMDD request")
    return get_next_mdd_req


def make_rassrvr_get_next_tile_req(cid):
    get_next_tile_req = rassrvr.GetNextTileReq(client_id=cid)
    if not get_next_tile_req:
        raise Exception("Can't create GetNextTile request")
    return get_next_tile_req

def make_rassrvr_end_transfer_req(cid):
    ent_transfer_req = rassrvr.EndTransferReq(client_id=cid)
    if not ent_transfer_req:
        raise Exception("Can't create EndTransfer request")
    return ent_transfer_req