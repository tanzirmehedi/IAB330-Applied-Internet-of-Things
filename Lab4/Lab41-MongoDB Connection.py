from pymongo import MongoClient

uri = "mongodb+srv://stanzir:eJV3aC9SvSuI3E5P@cluster0.szzqnxj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a connection using the uri
client = MongoClient(uri)

# Print all databases on this connected cluster
databases = client.list_database_names()
print("All available databases:")
for db in databases:
    print(db)

# Get the database named "sample_mflix"
mflix_db = client['sample_mflix']

# List all collections in this database
collections = mflix_db.list_collection_names()
print("All collections in the database:")
for c in collections:
    print(c)