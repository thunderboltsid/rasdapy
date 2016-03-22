import unittest
import raspy.ras as ras


class TestDemoCollectionGreySet(unittest.TestCase):
    def setUp(self):
        self.hostname = "localhost"
        self.username = "rasadmin"
        self.password = "rasadmin"
        self.collName = "RasdaPyGrey"
        self.con = ras.Connection(hostname=self.hostname, username=self.username, password=self.password)
        self.db = self.con.database("RASBASE")

    def test_create_collection(self):
        txn = self.db.transaction(rw=True)
        q = txn.query("create collection " + self.collName + " GreySet")
        pass

    def test_insert_in_collection(self):
        txn = self.db.transaction(rw=True)
        q = txn.query("insert into " + self.collName + " values marray x in [0:100, 0:100] values 1c")
        pass

    def test_read_from_collection(self):
        txn = self.db.transaction(rw=False)
        q = txn.query("select " + self.collName + "[0:2,0:2] from " + self.collName)
        data = q.execute()
        txn.abort_transaction()
        self.assertIsInstance(data, ras.Array)

    def test_read_scalar_from_collection(self):
        txn = self.db.transaction(rw=False)
        q = txn.query("select avg_cells(" + self.collName + ") from " + self.collName)
        data = q.execute()
        txn.abort_transaction()
        self.assertIsInstance(data, ras.Array)

    def test_drop_collection(self):
        pass


class TestDemoCollectionRGBSet(unittest.TestCase):
    def setUp(self):
        self.hostname = "localhost"
        self.username = "rasadmin"
        self.password = "rasadmin"
        self.collName = "RasdaPyRGB"
        self.con = ras.Connection(hostname=self.hostname, username=self.username, password=self.password)
        self.db = self.con.database("RASBASE")

    def test_create_collection(self):
        txn = self.db.transaction(rw=True)
        q = txn.query("create collection " + self.collName + " RGBSet")
        pass

    def test_insert_in_collection(self):
        txn = self.db.transaction(rw=True)
        q = txn.query("insert into " + self.collName + " values marray x in [0:100, 0:100] values {1c, 2c, 3c}")
        pass

    def test_read_from_collection(self):
        txn = self.db.transaction(rw=False)
        q = txn.query("select " + self.collName + "[0:2,0:2] from " + self.collName)
        data = q.execute()
        txn.abort_transaction()
        self.assertIsInstance(data, ras.Array)

    def test_read_scalar_from_collection(self):
        txn = self.db.transaction(rw=False)
        q = txn.query("select avg_cells(" + self.collName + ") from " + self.collName)
        data = q.execute()
        txn.abort_transaction()
        self.assertIsInstance(data, ras.Array)

    def test_drop_collection(self):
        txn = self.db.transaction(rw=True)
        q = txn.query("drop collection " + self.collName)
        pass

if __name__ == "__main__":
    unittest.main()
