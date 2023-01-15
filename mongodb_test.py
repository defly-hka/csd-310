import pymongo
from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.rrg4zed.mongodb.net/PyTech"
client = MongoClient(url)
db=client.pytech
print(db.students)
