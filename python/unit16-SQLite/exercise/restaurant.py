import sqlite3
import os


def create_database():
	connection = sqlite3.connect("restaurant.db")
	cursor = connection.cursor()
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
		connection.commit()
	except:
		print("Tables already exits")
	connection.close()


def add_category():
	connection = sqlite3.connect("restaurant.db")
	cursor = connection.cursor()
	cat = input("Category Name: ")

	try:
		query = "INSERT INTO category VALUES (null, '{}')".format(cat)
		cursor.execute(query)
		connection.commit()
		print("Category {} Added".format(cat))
	except:
		print("Error. Category already exists")
	connection.close()


def add_plate():
	connection = sqlite3.connect("restaurant.db")
	cursor = connection.cursor()

	cursor.execute("SELECT * FROM category")

	categories = cursor.fetchall()

	for category in categories:
		print("{}. {}".format(category[0], category[1]))

	category_id = input("Select a Category:")

	plate_name = input("Which plate you want to add?")

	try:
		query = "INSERT INTO plate VALUES (null, '{}', '{}')".format(plate_name, category_id)
		cursor.execute(query)

	except sqlite3.IntegrityError:
		print("The plato {} already exits.".format(plate_name))
	else:
		print("Plate {} added".format(plate_name))

	connection.commit()
	connection.close()


def show_menu():
	connection = sqlite3.connect("restaurant.db")
	cursor = connection.cursor()

	cursor.execute("select * from category")

	categories = cursor.fetchall()

	for category in categories:
		print(category[1] + ":")
		plates = cursor.execute("select name from plate where category_id='{}'".format(category[0]))
		for plate in plates:
			print("\t" + plate[0])

	connection.close()


print("Welcome to your restaurant!")

message = "Menu:\n1. Add a Category\n2. Add a Plate\n3. Show Menu\n4. Exit\n"

#while True:
option = input(message)

if option == '1':
	add_category()
elif option == '2':
	add_plate()
elif option == '3':
	show_menu()
else:
	exit()
