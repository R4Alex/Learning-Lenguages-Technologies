# Trditional
list = []
for letter in 'house':
	list.append(letter)
print(list)

# with list comprehensions
list = [letter for letter in 'house']
print(list)
print()


# Example 2
# Traditional
list = []

for number in range(0, 11):
	list.append(number**2)
print(list)

# with list comprehensions
list = [number**2 for number in range(0,11)]
print(list)
print()


# Exercise
# Traditional
list = []
for number in range(0, 11):
	if number % 2 == 0:
		list.append(number)
print(list)

# comprehensions
list = [number for number in range(0,11) if number%2 == 0]
print(list)
print()


# Exercise 2
# Traditional
list = []
for number in range(0, 11):
	list.append(number**2)

even_numbers = []

for number in list:
	if number % 2 == 0:
		even_numbers.append(number)
print(even_numbers)


# comprehensions
# You can nest this kind of lists
# oneline
list = [number for number in [number**2 for number in range(0,11)] if number%2 == 0]

# A little code improve
list = [number**2 for number in range(0,11)]
list = [number for number in list if number%2 == 0]

print(list)
