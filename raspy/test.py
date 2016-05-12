from rasda import *
con = Connection()
db = con.database("RASBASE")
col = RasCollection("rgb")
col /= 3
col -= 10
col = col.avg_cells()
col.use_db(db)
foo = col.eval()
import pdb; pdb.set_trace()
