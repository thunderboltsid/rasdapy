import ras
con = ras.Connection()
db = con.database("RASBASE")
txn = db.transaction()