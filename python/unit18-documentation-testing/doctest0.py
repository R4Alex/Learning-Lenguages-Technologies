
def sum(a, b):
	"""
	This function gets 2 parameters and return a sum

	>>> sum(5, 10)
	15

	>>> sum (-5,7)
	2

    text string:

    >>> sum('aa','bb')
    'aabb'

    Or list

    >>> a = [1, 2, 3]
    >>> b = [4, 5, 6]
    >>> sum(a,b)
    [1, 2, 3, 4, 5, 6]

	
	>>> sum(10, "Hello")
	Traceback (most recent call last):
      ...
    TypeError: unsupported operand type(s) for +: 'int' and 'str'

	"""
	return a + b


def palindrome(word):
	"""
	this function checks if the word is a palindrome

	>>> palindrome("girafarig")
	True

	>>> palindrome("radar")
	True

	>>> palindrome("somos")
	True

	>>> palindrome("holah")
	False

	>>> palindrome("Ana")
	True

	>>> palindrome("Atar a la rata")
	True
	"""
	return True if word.lower().replace(" ", "") == word[::-1].lower().replace(" ", "") else False


if __name__ == "__main__":
	import doctest
	# you can use this to check where the module is come from 
	# print(doctest.__file__ )
	doctest.testmod()


def double(list):
	"""
	double a list's value

	>>> l = [1, 2, 3, 4, 5]
	>>> double(l)
	[2, 4, 6, 8, 10]


	>>> l = []
	>>> for i in range(10):
	... 	l.append(i)
	>>> double(l)
	[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
	"""
	return [n*2 for n in list]


