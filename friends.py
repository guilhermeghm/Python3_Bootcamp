import sqlite3

#Open the DB connection.
conn = sqlite3.connect("my_friends.db")

#Create cursor object.
c = conn.cursor()

#Execute the SQL commands.
c.execute("CREATE TABLE friends (first_name TEXT, last_name TEXT, closeness INTEGER);")

#insert_query = '''INSERT INTO friends
#                    VALUES ('Merriwether', 'Lewis', 7)'''

#BAD option, don't use this.
#form_first = "Dana"
#insert_query = f"INSERT INTO friends (first_name) VALUES ('{form_first}')"

#c.execute(insert_query)

#Best way!
data = ("Steve", "Irwin", 9)
insert_query = "INSERT INTO friends VALUES (?,?,?)"

c.execute(insert_query, data)

#Commit changes.
conn.commit()

#Close the DB connection.
conn.close()
