import ras
con = ras.Connection(username="rasadmin", password="rasadmin")
db = con.database("RASBASE")
txn = db.transaction()
q = txn.query("select avg_cells(mean_summer_airtemp) from mean_summer_airtemp")
# q = txn.query("select r from RAS_COLLECTIONNAMES as r")
example = q.execute()
import pdb; pdb.set_trace()
