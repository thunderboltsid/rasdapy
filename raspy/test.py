import ras
con = ras.Connection(username="rasadmin", password="rasadmin")
db = con.database("RASBASE")
txn = db.transaction()
q = txn.query("select mr from mr")
# q = txn.query("select r from RAS_COLLECTIONNAMES as r")
example = q.execute()
import pdb; pdb.set_trace()
