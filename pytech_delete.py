import pymongo
from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.rrg4zed.mongodb.net/PyTech"
client = MongoClient(url)
db=client["pytech"]
collection = db["students"]

list = db.students.find({})
for names in list:
 print(names)
results = collection.find_one(["_id" = 1008])

updateOne = ({"_id": 1008},{set :{"last_name":"Granger"}})
updateOne = ({"_id":1008},{set : {"_id":1010}})

find = {"id":1010}
collection.delete_one(find)