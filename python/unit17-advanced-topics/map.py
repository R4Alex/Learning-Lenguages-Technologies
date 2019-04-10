
numbers = [2, 5, 23, 50	, 33]

def double(number):
	return number*2

map(double, numbers)

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]

list(map(lambda x,y : x*y, a,b))

c = [11, 12, 13, 14, 15]

list(map(lambda x,y,z : x*y*z, a,b,c))


class Person:

	def __init__(self, name, age):
		self.name = name
		self.age = age

	def __str__(self):
		return f"{self.name} is {self.age} years old"

people = [
	Person("juan", 35),
	Person("Martha", 36),
	Person("Eduardo", 12),
	Person("Manuel", 8)
]

def increment(person):
	person.age += 1
	return person

people = map(increment, people)

people = map(lambda person: Person(person.name, person.age+1), people)

for person in people:
	print(person)
