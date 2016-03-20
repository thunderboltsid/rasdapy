import ras
con = ras.Connection()
db = con.database("RASBASE")
txn = db.transaction()
# q = txn.query("select mr[100:150,40:80] from mr")
q = txn.query("select r from RAS_COLLECTIONNAMES as r")
foo = q.execute()
import pdb; pdb.set_trace()
