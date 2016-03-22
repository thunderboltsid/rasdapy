import ras
con = ras.Connection()
db = con.database("RASBASE")
txn = db.transaction()
q = txn.query("select rgb[40:42,40:41] from rgb")
# q = txn.query("select r from RAS_COLLECTIONNAMES as r")
foo = q.execute()
import pdb; pdb.set_trace()
