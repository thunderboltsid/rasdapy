from raspy.utils import get_md5_string
from raspy.request_factories import make_rasmgr_close_db_req, make_rasmgr_connect_req, make_rasmgr_disconnect_req, \
    make_rasmgr_open_db_req, make_rasmgr_keep_alive_req
import unittest


class RasmgrRequestCreationTest(unittest.TestCase):
    def setUp(self):
        self.username = "rasguest"
        self.password = get_md5_string("rasguest")
        self.clientUUID = "loksa-321mlk-sdfklsm-321"
        self.clientId = 6660
        self.dbname = "RASBASE"
        self.dbsid = "ras_786"

    def test_rasmgr_connect(self):
        req = make_rasmgr_connect_req(self.username, self.password)
        self.assertEqual(req.userName, self.username)
        self.assertEqual(req.passwordHash, get_md5_string(self.password))

    def test_rasmgr_disconnect(self):
        req = make_rasmgr_disconnect_req(self.clientUUID, self.clientId)
        self.assertEqual(req.clientUUID, self.clientUUID)
        self.assertEqual(req.clientId, self.clientId)

    def test_rasmgr_opendb(self):
        req = make_rasmgr_open_db_req(self.clientUUID, self.clientId, self.dbname)
        self.assertEqual(req.clientUUID, self.clientUUID)
        self.assertEqual(req.clientId, self.clientId)
        self.assertEqual(req.databaseName, self.dbname)

    def test_rasmgr_closedb(self):
        req = make_rasmgr_close_db_req(self.clientUUID, self.clientId, self.dbsid)
        self.assertEqual(req.clientUUID, self.clientUUID)
        self.assertEqual(req.clientId, self.clientId)
        self.assertEqual(req.dbSessionId, self.dbsid)

    def test_rasmgr_keep_alive(self):
        req = make_rasmgr_keep_alive_req(self.clientUUID)
        self.assertEqual(req.clientUUID, self.clientUUID)


if __name__ == "__main__":
    unittest.main()