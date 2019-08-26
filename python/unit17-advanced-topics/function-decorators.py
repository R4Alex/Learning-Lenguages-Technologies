# scope of variables and functions
def hello():

	number = 50

	def welcome():
		return "Hello!"

	print(locals())
	print(globals())
	return welcome

list = [1, 2]

hello()


def hello2():
	return "hello!"

def test(funcion):
	print(funcion()) 


test(hello2)

print("\n\n")


def hello3():
	print("Hello")

def bye():
	print("Bye")


def monitor(function):

	def decorate():
		print("\t *Function: ", function.__name__, " init")
		function()
		print("\t *Function: ", function.__name__, " ends\n")

	return decorate

monitor(hello3)()


# Decorator Funciontions
@monitor
def bye():
	print("bye")

bye()


''' Error
@monitor
def wave(text):
	print(text)

wave("Hello")
'''

def monitor_args(function):

	def decorate(*args, **kwargs):
		print("\t *Function: ", function.__name__, " init")
		function(*args, **kwargs)
		print("\t *Function: ", function.__name__, " ends\n")

	return decorate

@monitor_args
def wave(text):
	print(text)

wave("Hello")