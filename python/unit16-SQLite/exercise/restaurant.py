import sqlite3
import os

def create_database(cursor):
	try:
		cursor.execute('''
			CREATE TABLE category(
	                id INTEGER PRIMARY KEY AUTOINCREMENT,
	                name VARCHAR(100) UNIQUE NOT NULL)''')

		cursor.execute('''
			CREATE TABLE plate(
	                id INTEGER PRIMARY KEY AUTOINCREMENT,
	                name VARCHAR(100) UNIQUE NOT NULL, 
	                category_id INTEGER NOT NULL,
	                FOREIGN KEY(category_id) REFERENCES category(id))''')

		print("Tables Created")
	except:
		print("Tables already exits")

connection = sqlite3.connect("restaurant.db")
cursor = connection.cursor()

create_database(cursor)



connection.commit()
connection.close()
#os.remove("restaurant.db")
