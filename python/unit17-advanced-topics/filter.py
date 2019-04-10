numbers = [2, 5, 10, 23, 50, 33]

def multiple(number):
	if number % 5 == 0:
		return True

filt = filter(multiple, numbers)

print(list(filt))

# using lambda function

l = filter(lambda number: number%5==0, numbers)

print(list(l))

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

children = filter(lambda person: person.age <= 18, people)

for person in children:
	print(person)