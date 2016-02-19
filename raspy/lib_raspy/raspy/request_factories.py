#
# This file is part of rasdaman community.
#
# Rasdaman community is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Rasdaman community is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with rasdaman community.  If not, see <http://www.gnu.org/licenses/>.
#
# Copyright 2003, 2004, 2005, 2006, 2007, 2008, 2009 Peter Baumann / rasdaman GmbH.
#
# For more information please see <http://www.rasdaman.org>
# or contact Peter Baumann via <baumann@rasdaman.com>.

from stubs import client_rassrvr_service_pb2 as client
from stubs import rasmgr_client_service_pb2 as rasmgr


def make_connect_req(username, password):
    con_req = rasmgr.ConnectReq(userName=username, passwordHash=password)
    if not con_req:
        raise Exception("Can't create Connect request")
    return con_req


def make_disconnect_req(cuiid, cid):
    discon_req = rasmgr.DisconnectReq(clientUUID=cuiid, clientID=cid)
    if not discon_req:
        raise Exception("Can't create Disconnect request")
    return discon_req


def make_keep_alive_req(cuiid, cid):
    keep_alive_req = rasmgr.KeepAliveReq(clientUUID=cuiid, clientID=cid)
    if not keep_alive_req:
        raise Exception("Can't create KeepAlive request")
    return keep_alive_req


def make_open_db_req(cuiid, cid, dbname):
    open_db_req = rasmgr.OpenDbReq(clientUUID=cuiid, clientID=cid, databaseName=dbname)
    if not open_db_req:
        raise Exception("Can't create OpenDb request")
    return open_db_req


def make_close_db_req(cuuid, cid, dbsid):
    close_db_req = rasmgr.CloseDbReq(clientUUID=cuuid, clientID=cid, dbSessionId=dbsid)
    if not close_db_req:
        raise Exception("Can't create CloseDb request")
    return close_db_req


def make_begin_transaction_req(cid, rw):
    begin_transaction_req = client.BeginTransactionReq(client_id=cid, rw=rw)
    if not begin_transaction_req:
        raise Exception("Can't create BeginTransaction request")
    return begin_transaction_req


def make_commit_transaction_req(cid):
    commit_transaction_req = client.CommitTransactionReq(client_id=cid)
    if not commit_transaction_req:
        raise Exception("Can't create CommitTransaction request")
    return commit_transaction_req


def make_abort_transaction_req(cid):
    abort_transaction_req = client.AbortTransactionReq(client_id=cid)
    if not abort_transaction_req:
        raise Exception("Can't create AbortTransaction request")
    return abort_transaction_req


def make_execute_query_req(cid, query):
    execute_query_req = client.ExecuteQueryReq(client_id=cid, query=query)
    if not execute_query_req:
        raise Exception("Can't create ExecuteQuery request")
    return execute_query_req


def make_execute_http_query_req(cid, data, data_length):
    execute_http_query_req = client.ExecuteHttpQueryReq(client_id=cid, data=data, data_length=data_length)
    if not execute_http_query_req:
        raise Exception("Can't create ExecuteHttpQuery request")
    return execute_http_query_req


def make_get_collection_req(cid, colid):
    get_collection_req = client.GetCollectionByNameOrOidReq(client_id=cid, collection_identifier=colid, is_name=True)
    if not get_collection_req:
        raise Exception("Can't create GetCollectionByNameOrOid request")
    return get_collection_req


def make_get_next_mdd_req(cid):
    get_next_mdd_req = client.GetNextMDD(client_id=cid)
    if not get_next_mdd_req:
        raise Exception("Can't create GetNextMDD request")
    return get_next_mdd_req


def make_get_next_tile_req(cid):
    get_next_tile_req = client.GetNextTile(client_id=cid)
    if not get_next_tile_req:
        raise Exception("Can't create GetNextTile")
    return get_next_tile_req
