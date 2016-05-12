from rasda import *
con = Connection()
db = con.database("RASBASE")
col = RasCollection("rgb")
col /= 3
col -= 10
col.use_db(db)
foo = col.eval()
import pdb; pdb.set_trace()
