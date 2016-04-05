import unittest
import raspy.ras as ras
import numpy as np


# class TestDemoCollectionGreySet(unittest.TestCase):
#     def setUp(self):
#         self.hostname = "localhost"
#         self.username = "rasadmin"
#         self.password = "rasadmin"
#         self.collName = "RasdaPyGrey"
#         self.con = ras.Connection(hostname=self.hostname, username=self.username, password=self.password)
#         self.db = self.con.database("RASBASE")
#
#     def test_create_collection(self):
#         txn = self.db.transaction(rw=True)
#         q = txn.query("create collection " + self.collName + " GreySet")
#         res = q.eval()
#         txn.commit()
#         self.assertEqual(res, 0)
#
#     def test_insert_in_collection(self):
#         txn = self.db.transaction(rw=True)
#         q = txn.query("insert into " + self.collName + " values marray x in [0:100, 0:100] values 1c")
#         res = q.eval()
#         txn.commit()
#         self.assertEqual(res, 0)
#
#     def test_read_from_collection(self):
#         txn = self.db.transaction(rw=False)
#         q = txn.query("select " + self.collName + "[0:2,0:2] from " + self.collName)
#         data = q.eval()
#         txn.abort()
#         self.assertIsInstance(data, ras.Array)
#         self.assertEqual(data.values, [[1, 1, 1, 1, 1, 1, 1, 1, 1]])
#
#     def test_read_scalar_from_collection(self):
#         txn = self.db.transaction(rw=False)
#         q = txn.query("select avg_cells(" + self.collName + ") from " + self.collName)
#         data = q.eval()
#         txn.abort()
#         self.assertIsInstance(data, ras.Array)
#
#     def test_drop_collection(self):
#         txn = self.db.transaction(rw=True)
#         q = txn.query("drop collection " + self.collName)
#         res = q.eval()
#         txn.commit()
#         self.assertEqual(res, 0)


class TestDemoCollectionRGBSet(unittest.TestCase):
    def setUp(self):
        self.hostname = "localhost"
        self.username = "rasadmin"
        self.password = "rasadmin"
        self.collection_name = "RasdaPyRGBTest"
        self.con = ras.Connection(hostname=self.hostname, username=self.username, password=self.password)
        self.db = self.con.database("RASBASE")
        self.values = \
            [[[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]]], [
                [[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]]]

    def test_a_create_collection(self):
        txn = self.db.transaction(rw=True)
        q = txn.query("create collection " + self.collection_name + " RGBSet")
        res = q.eval()
        txn.commit()
        self.assertEqual(res, 0)

    def test_b_insert_in_collection(self):
        txn = self.db.transaction(rw=True)
        q = txn.query("insert into " + self.collection_name + " values marray x in [0:2, 0:2] values {1c, 2c, 3c}")
        res = q.eval()
        txn.commit()
        self.assertEqual(res, 0)

    def test_c_read_from_collection(self):
        txn = self.db.transaction(rw=False)
        q = txn.query("select " + self.collection_name + "[0:2,0:2] from " + self.collection_name)
        data = q.eval()
        txn.abort()
        self.assertIsInstance(data, ras.Array)
        self.assertEqual(data.values, )

    def test_d_read_scalar_from_collection(self):
        txn = self.db.transaction(rw=False)
        q = txn.query("select avg_cells(" + self.collection_name + ") from " + self.collection_name)
        data = q.eval()
        txn.abort()
        self.assertIsInstance(data, ras.Array)

    def test_e_drop_collection(self):
        txn = self.db.transaction(rw=True)
        q = txn.query("drop collection " + self.collection_name)
        res = q.eval()
        txn.commit()
        self.assertEqual(res, 0)


if __name__ == "__main__":
    unittest.main()
