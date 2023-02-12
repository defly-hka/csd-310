import pymongo
from pymongo import MongoClient
destination = pymongo.MongoClient("mongodb+srv://admin:admin@cluster0.rrg4zed.mongodb.net/PyTech")
PySports = destination["PySports"]
teams = PySports["teams"]
db=destination.PySports

pip: install mysql-connector-python 

SELECT player_id, first_name, last_name, team_name
FROM pysports
INNER JOIN team
	ON player.team_id = team.team_id;
    
#left outer join
SELECT player_id, first_name, last_name, team_name
FROM pysports
LEFT OUTER JOIN team
	ON player.team_id = team.teamid;

#right outer join
SELECT player_id, first_name, last_name, team_name
 FROM pysports
RIGHT OUTER JOIN team
	ON player.team_id = team.teamid;

SELECT first_name, last_name
FROM pysports
WHERE player_id = 3; 


