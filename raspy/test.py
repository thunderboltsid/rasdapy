import ras
# con = ras.Connection(hostname="192.168.0.106")
con = ras.Connection(port=50051)
db = con.database("RASBASE")
txn = db.transaction()