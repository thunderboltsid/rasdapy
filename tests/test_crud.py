import unittest
from rasdapy import core


class TestDemoCollectionGreySet(unittest.TestCase):
    def setUp(self):
        self.hostname = "localhost"
        self.username = "rasadmin"
        self.password = "rasadmin"
        self.collName = "RasdaPyGrey"
        self.con = core.Connection(hostname=self.hostname,
                                username=self.username, password=self.password)
        self.db = self.con.database("RASBASE")

    def test_a_create_collection(self):
        txn = self.db.transaction(rw=True)
        q = txn.query("create collection " + self.collName + " GreySet")
        res = q.eval()
        txn.commit()
        self.assertEqual(res, None)

    def test_b_insert_in_collection(self):
        txn = self.db.transaction(rw=True)
        q = txn.query("insert into " + self.collName + " values marray x in [0:2, 0:2] values 1c")
        res = q.eval()
        txn.commit()
        self.assertEqual(res, None)

    def test_c_read_from_collection(self):
        txn = self.db.transaction(rw=False)
        q = txn.query("select " + self.collName + "[0:2,0:2] from " + self.collName)
        data = q.eval()
        txn.abort()
        self.assertIsInstance(data, core.Array)

    def test_d_read_scalar_from_collection(self):
        txn = self.db.transaction(rw=False)
        q = txn.query("select avg_cells(" + self.collName + ") from " + self.collName)
        data = q.eval()
        txn.abort()
        self.assertIsInstance(data, list)
        self.assertEqual(data, [1.0])

    def test_e_drop_collection(self):
        txn = self.db.transaction(rw=True)
        q = txn.query("drop collection " + self.collName)
        res = q.eval()
        txn.commit()
        self.assertEqual(res, None)


class TestDemoCollectionRGBSet(unittest.TestCase):
    def setUp(self):
        self.hostname = "localhost"
        self.username = "rasadmin"
        self.password = "rasadmin"
        self.collection_name = "RasdaPyRGBTest"
        self.con = core.Connection(hostname=self.hostname,
                                username=self.username, password=self.password)
        self.db = self.con.database("RASBASE")

    def test_a_create_collection(self):
        txn = self.db.transaction(rw=True)
        q = txn.query("create collection " + self.collection_name + " RGBSet")
        res = q.eval()
        txn.commit()
        self.assertEqual(res, None)

    def test_b_insert_in_collection(self):
        txn = self.db.transaction(rw=True)
        q = txn.query("insert into " + self.collection_name + " values marray x in [0:2, 0:2] values {1c, 2c, 3c}")
        res = q.eval()
        txn.commit()
        self.assertEqual(res, None)

    def test_c_read_from_collection(self):
        txn = self.db.transaction(rw=False)
        q = txn.query("select " + self.collection_name + "[0:2,0:2] from " + self.collection_name)
        data = q.eval()
        txn.abort()
        self.assertIsInstance(data, core.Array)

    def test_d_read_scalar_from_collection(self):
        txn = self.db.transaction(rw=False)
        q = txn.query("select avg_cells(" + self.collection_name + ") from " + self.collection_name)
        data = q.eval()
        txn.abort()
        self.assertIsInstance(data, list)
        self.assertEqual(data, [[1.0, 2.0, 3.0]])

    def test_e_drop_collection(self):
        txn = self.db.transaction(rw=True)
        q = txn.query("drop collection " + self.collection_name)
        res = q.eval()
        txn.commit()
        self.assertEqual(res, None)


if __name__ == "__main__":
    unittest.main()
