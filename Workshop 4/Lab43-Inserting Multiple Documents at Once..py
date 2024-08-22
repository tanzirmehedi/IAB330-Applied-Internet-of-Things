from pymongo import MongoClient

uri = "mongodb+srv://stanzir:eJV3aC9SvSuI3E5P@cluster0.szzqnxj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri)
db = client["persons_db"]
persons = db["persons"]

# Create a list of dict objects
alice = {"name": "Alice", "age": 35, "contact": "0450403201", "favColor": "Red"}
bob = {"name": "bob", "age": 23, "contact": "0400888999", "address": "123 Random Road"}
carl = {"name": "Carl", "age": 17, "contact": "0433444555", "isStudent": True}
lst = [alice, bob, carl]

# Pass the list as the input
persons.insert_many(lst)