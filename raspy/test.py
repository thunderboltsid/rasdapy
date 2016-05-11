from rasda import *
con = Connection(hostname="martoaga", username="rasadmin", password="rasadmin")
db = con.database("RASBASE")
col = RasCollection("a")
col = col.avg_cells()
col.use_db(db)
foo = col.eval()
import pdb; pdb.set_trace()