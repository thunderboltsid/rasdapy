# Import library
from lib.rasda import *

# Initialize Connection and database instance
con = Connection()
db = con.database("RASBASE")

# List Collections on database
print(db.collections)

# Initialize collection of your choice
col = RasCollection("rgb")

# Perform operations
col /= 3
col -= 10

# Specify database to use
col.use_db(db)

# Verify query
str(col.query)

# Evaluate query
data = col.eval()

# Access the array in numpy format
arr = data.to_array()

# Convert to image
data.to_image("example_rgb.png")

# Use condensers
avg = col.avg_cells().eval()

