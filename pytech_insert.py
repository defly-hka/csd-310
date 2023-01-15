import pymongo
from pymongo import MongoClient
import PyTech
destination = pymongo.MongoClient("mongodb+srv://admin:admin@cluster0.rrg4zed.mongodb.net/PyTech")
PyTech = destination["PyTech"]
students = PyTech["students"]
db=destination.PyTech
harry ={
  "first_name": "Harry",
  "last_name":"Potter",
  } 
ron ={
    "first_name":"Ronald",
    "last_name":"Weasley",
}
hermione ={
    "first_name":"Hermione",
    "last_name":"Granger",
}
harry_student_id = students.insert_one(harry).inserted_id(1007)
ron_student_id=students.insert_one(ron).inserted_id(1008)
hermione_student_id=students.insert_one(hermione).inserted_id(1009)
print(harry_student_id)
print(ron_student_id)
print(hermione_student_id)