from raspy.utils import get_md5_string
from raspy.request_factories import make_rassrvr_end_transfer_req, make_rassrvr_abort_transaction_req, \
    make_rassrvr_begin_transaction_req, make_rassrvr_close_db_req, make_rassrvr_commit_transaction_req, \
    make_rassrvr_execute_http_query_req, make_rassrvr_execute_query_req, make_rassrvr_get_collection_req, \
    make_rassrvr_get_next_mdd_req, make_rassrvr_get_next_tile_req, make_rassrvr_keep_alive_req, make_rassrvr_open_db_req
import unittest


class RasmgrRequestCreationTest(unittest.TestCase):
    def setUp(self):
        self.username = "rasguest"
        self.password = get_md5_string("rasguest")
        self.clientUUID = "loksa-321mlk-sdfklsm-321"
        self.clientId = 6660
        self.dbname = "RASBASE"
        self.dbsid = "ras_786"
        self.rw = True
        self.query = "select mr[100:140, 40:80] from mr"
        self.data = '\xac'
        self.data_length = 1
        self.colid = "mr"

    def test_opendb(self):
        req = make_rassrvr_open_db_req(self.clientId, self.dbname)
        self.assertEqual(req.client_id, self.clientId)
        self.assertEqual(req.database_name, self.dbname)

    def test_closedb(self):
        req = make_rassrvr_close_db_req(self.clientId)
        self.assertEqual(req.client_id, self.clientId)

    def test_keep_alive(self):
        req = make_rassrvr_keep_alive_req(self.clientUUID, self.dbsid)
        self.assertEqual(req.client_uuid, self.clientUUID)
        self.assertEqual(req.session_id, self.dbsid)

    def test_begin_transaction(self):
        req = make_rassrvr_begin_transaction_req(self.clientId, self.rw)
        self.assertEqual(req.client_id, self.clientId)
        self.assertEqual(req.rw, self.rw)

    def test_commit_transaction(self):
        req = make_rassrvr_commit_transaction_req(self.clientId)
        self.assertEqual(req.client_id, self.clientId)

    def test_abort_transaction(self):
        req = make_rassrvr_abort_transaction_req(self.clientId)
        self.assertEqual(req.client_id, self.clientId)

    def test_execute_query(self):
        req = make_rassrvr_execute_query_req(self.clientId, self.query)
        self.assertEqual(req.client_id, self.clientId)
        self.assertEqual(req.query, self.query)

    def test_execute_http_query(self):
        req = make_rassrvr_execute_http_query_req(self.clientId, self.data)
        self.assertEqual(req.client_id, self.clientId)
        self.assertEqual(req.data, self.data)

    def test_get_collection(self):
        req = make_rassrvr_get_collection_req(self.clientId, self.colid)
        self.assertEqual(req.client_id, self.clientId)
        self.assertEqual(req.collection_identifier, self.colid)

    def test_get_next_mdd(self):
        req = make_rassrvr_get_next_mdd_req(self.clientId)
        self.assertEqual(req.client_id, self.clientId)

    def test_get_next_tile(self):
        req = make_rassrvr_get_next_tile_req(self.clientId)
        self.assertEqual(req.client_id, self.clientId)

    def test_end_transfer(self):
        req = make_rassrvr_end_transfer_req(self.clientId)
        self.assertEqual(req.client_id, self.clientId)


if __name__ == "__main__":
    unittest.main()
