#creating user and extra user for deletion
CREATE USER 'pysportsUser'@'localhost' IDENTIFIED WITH mysql_native_password BY 'WatchSticksLanyardMouse808(*)' ;
CREATE USER 'pysportsUserDel'@'localhost' IDENTIFIED WITH mysql_native_password BY 'WatchSticksLanyardMouse808(*)' ;
# granting privileges 
GRANT ALL PRIVILEGES ON pysports.* TO 'pysportsUser'@'localhost';
#drop user
DROP USER IF EXISTS 'pysportsUserDel'@'localhost';
#creating tables
CREATE TABLE team (
team_id	     INT            NOT NULL  AUTO_INCREMENT, 
team_name    VARCHAR(75)    NOT NULL,
mascot       VARCHAR(75)    NOT NULL,
PRIMARY KEY(team_id)
);

#Adding team records
INSERT INTO team(team_name, mascot)
	VALUES ('Team Hypnotoad', 'Toad');
INSERT INTO team(team_name, mascot)
	VALUES ('Niblonians', 'Nibbler');
    
#deleting player value
DROP TABLE IF EXISTS player;

#selecting team
SELECT team_id FROM team WHERE team_name = 'Niblonians'
