from pymongo import MongoClient
import students
client = MongoClient("mongodb+srv://admin:admin@cluster0.rrg4zed.mongodb.net/pytech")
db =client.PyTech

list = db.students.find({})
for names in list:
 print(names)
 
 

harry_id =db.students.find_one({"first_name":"harry"})
print(harry_id["harry_student_id"])