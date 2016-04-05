import ras
con = ras.Connection(username="rasadmin", password="rasadmin")
db = con.database("RASBASE")
txn = db.transaction(rw=True)
q = txn.query("select rgb from rgb")
# q = txn.query("select r from RAS_COLLECTIONNAMES as r")
example = q.execute()
import pdb; pdb.set_trace()
