from rasda import *
con = Connection(hostname="192.168.0.103", username="rasadmin", password="rasadmin")
db = con.database("RASBASE")
col = RasCollection("rgb")
# col = col[0:2]
# col /= 3
# col -= 10
col.use_db(db)
import pdb; pdb.set_trace()
foo = col.eval()
