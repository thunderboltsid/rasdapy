from request_factories import *
_TIMEOUT_SECONDS = 30


def rasmgr_connect(stub, username, password):
    connection = stub.Connect(make_connect_req(username, password), _TIMEOUT_SECONDS)
    if not connection:
        raise Exception("Remote function 'Connect' did not return anything")
    return connection


def rasmgr_disconnect(stub, cuiid, cid):
    return stub.Disconnect(make_disconnect_req(cuiid, cid), _TIMEOUT_SECONDS)


def rasmgr_keep_alive(stub, cuiid, cid):
    return stub.KeepAliveReq(make_keep_alive_req(cuiid, cid), _TIMEOUT_SECONDS)


def rasmgr_open_db(stub, cuiid, cid, dbname):
    resp = stub.OpenDb(make_open_db_req(cuiid, cid, dbname), _TIMEOUT_SECONDS)
    if not resp:
        raise Exception("Remote function 'OpenDb' did not return anything")
    return resp


def rasmgr_close_db(stub, cuuid, cid, dbsid):
    return stub.CloseDb(make_close_db_req(cuuid, cid, dbsid), _TIMEOUT_SECONDS)


def client_begin_transaction(stub, cid, rw):
    return stub.BeginTransaction(make_begin_transaction_req(cid, rw), _TIMEOUT_SECONDS)


def client_commit_transaction(stub, cid):
    return stub.CommitTransaction(make_commit_transaction_req(cid), _TIMEOUT_SECONDS)


def client_abort_transaction(stub, cid):
    return stub.AbortTransaction(make_abort_transaction_req(cid), _TIMEOUT_SECONDS)


def client_execute_query(stub, cid, query):
    resp = stub.ExecuteQuery(make_execute_query_req(cid, query), _TIMEOUT_SECONDS)
    if not resp:
        raise Exception("Remote function 'ExecuteQuery' did not return anything")
    return resp


def client_execute_http_query(stub, cid, data, data_length):
    resp = stub.ExecuteHttpQuery(make_execute_http_query_req(cid, data, data_length), _TIMEOUT_SECONDS)
    if not resp:
        raise Exception("Remote function 'ExecuteHttpQuery' did not return anything")
    return resp


def client_get_collection_by_name(stub, cid, name):
    resp = stub.GetCollectionByNameOrOid(make_get_collection_req(cid, name), _TIMEOUT_SECONDS)
    if not resp:
        raise Exception("Remote function 'GetCollectionByNameOrOid' did not return anything")
    return resp


def client_get_next_mdd(stub, cid):
    resp = stub.GetNextMDD(cid)
    if not resp:
        raise Exception("Remote function 'GetNextMDD' did not return anything")
    return resp


def client_get_next_tile(stub, cid):
    resp = stub.GetNextTile(cid)
    if not resp:
        raise Exception("Remote function 'GetNextTile' did not return anything")
    return resp
