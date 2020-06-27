--SQL commands
CREATE TABLE dogs (
  name TEXT,
  breed TEXT,
  age INTEGER
);

CREATE TABLE cats (
  name TEXT,
  breed TEXT,
  age INTEGER
);

INSERT INTO cats (name, breed, age) VALUES ("Blue", "Scottish Fold", 3);

SELECT * FROM cats;
SELECT * FROM dogs WHERE name IS "Piggy";
SELECT name FROM dogs WHERE name IS "Piggy";
SELECT * FROM dogs WHERE breed IS NOT "Chihuahua";
SELECT * FROM dogs WHERE breed IS NOT "Chihuahua" AND breed IS NOT "Pug";
SELECT * FROM dogs WHERE name LIKE "%gg%";


--sqlite3 commands.
.tables

--To run a file with SQL commands.
.read basics.sql


--By default it will not save the data in a file, only in the memory. To persist the data, the option is run the command with a file or to open a file form the sqlite.

.open dog_db.sb
--OR
sqlite3 cats_db.db
