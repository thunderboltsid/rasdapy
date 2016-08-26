# Import library
from rasdapy.core import Connection
from rasdapy.surface import RasCollection

# Initialize Connection and database instance
con = Connection(hostname="138.201.18.85")

db = con.database("RASBASE")
# List Collections on database
print(db.collections)

# Initialize collection of your choice
col = RasCollection("rgb")

# Perform operations
col /= 3
col -= 10

# Specify database to use

# Verify query
str(col.query)

col.use_db(db)
# Evaluate query
data = col.eval()

# Access the array in numpy format
arr = data.to_array()

# Convert to image
data.to_image("example_rgb.png")

# Use condensers
avg = col.avg_cells().eval()

