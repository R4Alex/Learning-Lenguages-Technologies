import my_module


def hello(arg):
	"""This is a dockstring"""
	print("hello ", arg, "!")


hello("Alejandro")

help(hello)


class Cla:
	"""This is a class docstring"""
	def __init__(self):
		"""This is the init docstring"""
		pass

	def method(self):
		"""Method's docstring"""
		pass

o = Cla()

help(o)


help(my_module)