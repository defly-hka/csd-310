import pymongo
from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.rrg4zed.mongodb.net/PyTech"
client = MongoClient(url)
db=client["pytech"]
collection = db["students"]

list = db.students.find({})
for names in list:
 print(names)
 
 results = collection.find_one({"_id"=1007})
 
 for x in results:
    print (x)
    