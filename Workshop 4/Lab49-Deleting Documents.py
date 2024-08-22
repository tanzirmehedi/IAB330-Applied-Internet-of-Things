from pymongo import MongoClient

uri = "mongodb+srv://stanzir:eJV3aC9SvSuI3E5P@cluster0.szzqnxj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri)
db = client["persons_db"]
persons = db["persons"]

# Deletes the first "Alice" found
persons.delete_one({"name": "Alice"})

# Deletes the first student found
persons.delete_one({"$and": [{"name": "Carl"}, {"isStudent": True}]})

# Deletes all adults
persons.delete_many({"isAdult": True})