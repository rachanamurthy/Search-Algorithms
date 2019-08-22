# Testing Linear Search Algorithm

import unittest

from linear_search import linear_search

class TestLinearSearch(unittest.TestCase):
	def test_found(self):
		array = [3, 2, 3, 4, 1]
		self.assertTrue(linear_search(array,2))

	def test_not_found(self):
		array = [1, 2]
		self.assertFalse(linear_search(array,4))

	def test_null_case(self):
		array = []
		self.assertFalse(linear_search(array,1))

if __name__ == '__main__': 
  unittest.main() 