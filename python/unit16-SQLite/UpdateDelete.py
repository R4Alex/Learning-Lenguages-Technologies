import sqlite3

connection = sqlite3.connect("example.db")

cursor = connection.cursor()

cursor.execute("SELECT * from users where id=1")
user = cursor.fetchone()
print(user)

cursor.execute("UPDATE users SET name='Alex Santillan', age=24 where id=1")

#cursor.execute("DELETE from users")
cursor.execute("DELETE from users where id=1")


connection.commit()
connection.close()