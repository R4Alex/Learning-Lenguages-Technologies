import sqlite3

connection = sqlite3.connect("example.db")

cursor = connection.cursor()

cursor.execute('''
	CREATE TABLE users (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		ssn VARCHAR(9) UNIQUE,
		name varchar(100),
		age INTEGER,
		email varchar(100)
	)
''')

users_list = [
	('1111111A', 'Alex', 24, 'alex@example.com'),
	('2222222B', 'Mario', 51, 'mario@example.com'),
	('3333333C', 'Mercedes', 38, 'mario@example.com'),
	('4444444D', 'Juan', 19, 'juan@example.com'),
]

cursor.executemany("INSERT INTO users values (null, ?, ?, ?, ?)", users_list)

cursor.execute('''
	CREATE table products (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		name varchar (100) not null,
		trademark varchar(50) not null,
		price FLOAT not null
	)
''')

products = [
	('Keyboard', 'Logitech', 19.95), 
	('19" Screen', 'LG', 89.95)
]

cursor.executemany("INSERT INTO products VALUES (null, ?, ?, ?)", products)

connection.commit()
connection.close()

