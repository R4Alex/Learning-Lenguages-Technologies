import unittest

def double(a): return a*2

class TestFixture(unittest.TestCase):
	def setUp(self):
		print("Setting up context")
		self.numbers = [1, 2, 3, 4, 5]

	def test(self):
		print("Doing test")
		r = [double(n) for n in self.numbers]
		self.assertEqual(r, [2, 4, 6, 8, 10])

	def tearDown(self):
		print("Destroying context")
		del(self.numbers)

if __name__ == '__main__':
	unittest.main()