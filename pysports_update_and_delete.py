import pymongo
from pymongo import MongoClient
destination = pymongo.MongoClient("mongodb+srv://admin:admin@cluster0.rrg4zed.mongodb.net/PyTech")
PySports = destination["PySports"]
teams = PySports["teams"]
db=destination.PySports

pip: install mysql-connector-python 

#Update player info
UPDATE player
SET team_id = 2
	first_name = 'Turanga',
    last_name = 'Leela'
WHERE first_name = 'Nibbler';

#Deleting 

DELETE FROM player
WHERE first_name = 'Nibbler';

#Inserting

INSERT INTO player (first_name, last_name, team_name, team_id)
	VALUES ('Bender', 'Rodriguez', 'Planet Express Crew', 1); 
