from pymongo import MongoClient

uri = "mongodb+srv://stanzir:eJV3aC9SvSuI3E5P@cluster0.szzqnxj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri)
db = client["persons_db"]
persons = db["persons"]

# Create a filter to find the target documents
filter = {"name": "Alice"}

# Try to find documents with the specified conditions
results = persons.find(filter)
for doc in results:
    print(doc)