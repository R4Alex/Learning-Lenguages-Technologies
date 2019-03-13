import sqlite3

connection = sqlite3.connect("example.db")

cursor = connection.cursor()

cursor.execute("CREATE TABLE users (name VARCHAR(100), age INTEGER, email VARCHAR(100))")

cursor.execute("INSERT INTO users VALUES ('Alex', 24, 'email@example.com ')")

cursor.execute("SELECT * FROM users")

# this command get the last result, but it works like a pile
users_inserted = cursor.fetchone()
print(users_inserted)

users_list = [
	('Mario',51,'mario@example.com'),
	('Mercedes',38,'mario@example.com'),
	('Juan',19,'juan@example.com'),
]

cursor.executemany("INSERT INTO users values (?, ?, ?)", users_list)

cursor.execute("SELECT * FROM users")

users = cursor.fetchall()

for user in users:
	print(user)

connection.commit()
connection.close()
