import ras
con = ras.Connection()
db = con.database("RASBASE")
txn = db.transaction()
q = txn.query("select rgb from rgb")
# q = txn.query("select r from RAS_COLLECTIONNAMES as r")
foo = q.execute()
import pdb; pdb.set_trace()
