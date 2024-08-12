from pymongo import MongoClient

uri = "mongodb+srv://stanzir:eJV3aC9SvSuI3E5P@cluster0.szzqnxj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri)
db = client["persons_db"]
persons = db["persons"]

filter = {"name": "Alice"}

# Define the update, using operator $set
update = {"$set": {"contact": "0410203040", "employed": True}}

persons.update_one(filter, update)