import unittest


class Test(unittest.TestCase):
	def test(self):
		raise AssertionError()

	def test2(self):
		1/0

	def test_double(self):
		self.assertEqual(double(10), 20)
		self.assertEqual(double('Ab'), 'AbAb')

	def test_sum(self):
		self.assertEqual(sum(15, -15), 0)
		self.assertEqual(sum('Ab','cd'), 'Abcd')

	def test_is_even(self):
		self.assertEqual(is_even(11), False)
		self.assertEqual(is_even(12), True)



def double(a): return a*2
def sum(a, b): return a+b
def is_even(a): return True if a%2 == 0 else False


class TestStringMethods(unittest.TestCase):

	def test_upper(self):
		self.assertEqual('hello'.upper(), 'HELLO')

	def test_isupper(self):
		self.assertTrue('HELLO'.isupper())
		self.assertFalse('hola'.isupper())

	def test_split(self):
		s = 'Hello world'
		self.assertEqual(s.split(" "), ['Hello', 'world'])


if __name__ == "__main__":
	unittest.main()