from pymongo import MongoClient

uri = "mongodb+srv://stanzir:eJV3aC9SvSuI3E5P@cluster0.szzqnxj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri)
db = client["persons_db"]
persons = db["persons"]

# Create filters to find the target documents
filter_adult = {"age": {"$gt": 18}}
filter_minor = {"age": {"$lt": 18}}

# Define the updates, using operator $set
update_adult = {"$set": {"isAdult": True}}
update_minor = {"$set": {"isAdult": False}}

persons.update_many(filter_adult, update_adult)
persons.update_many(filter_minor, update_minor)