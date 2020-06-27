import sqlite3
conn = sqlite3.connect("my_friends.db")

#Create cursor object
c = conn.cursor()
#c.execute("SELECT * FROM friends")
#c.execute("SELECT * FROM friends WHERE first_name IS 'Rosa'")
c.execute("SELECT * FROM friends WHERE closeness > 5 ORDER BY 'closeness'")


#Option 1
#Interate over cursor
#for result in c:
#    print(result)

#Option 2,
#Fetch all results as list
print(c.fetchall())

#Fetch One result.
print(c.fetchone())

#Commit changes
conn.commit()
conn.close()
