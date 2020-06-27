import sqlite3
conn = sqlite3.connect("users.db")

#query = "CREATE TABLE users (username TEXT, password TEXT)"

u = input("Please enter your username...")
p = input("Please enter your password...")
c = conn.cursor()

#BAD idea because a SQL Injection
#query = f"SELECT * FROM users WHERE username='{u}' AND password = '{p}'"
#c.execute(query)

query = f"SELECT * FROM users WHERE username=? AND password =?"
c.execute(query, (u,p))

result = c.fetchone()
if(result):
    print("WELCOME BACK")
else:
    print("FAILED LOGIN")

conn.commit()
conn.close()
