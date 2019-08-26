
list = [number for number in range(0, 6) if number % 2 == 0]

print(list)

# custom generator function

def get_even_numbers(n):
	 for number in range(n + 1):
	 	if number % 2 == 0:
	 		yield number

print(get_even_numbers(10))

even_numbers = get_even_numbers(10)

print(next(even_numbers))
print(next(even_numbers))

# you can't use normal list has iterators
list = [0, 1, 2, 3]
#next(list)

# but you can convert list in iterators
list_iterable = iter(list)

print(list_iterable)
next(list_iterable)

# you can also use it on strings
