from pymongo import MongoClient

uri = "mongodb+srv://stanzir:eJV3aC9SvSuI3E5P@cluster0.szzqnxj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri)
db = client["persons_db"]
persons = db["persons"]

# Create a dict object
alice = {"name": "Shawon", "age": 25, "contact": "0400123456"}

# Pass the dict as the input
persons.insert_one(alice)