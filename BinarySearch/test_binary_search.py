# Testing the implementation of Binary Search Algorithm

import unittest

from binary_search import binary_search

class TestBinarySearch(unittest.TestCase):
	def test_found(self):
		array = [1,4,2,3]
		x = 1
		self.assertTrue(binary_search(array,x))

	def test_not_found(self):
		array = [4,2,5,2]
		x = 6
		self.assertFalse(binary_search(array,x))

	def test_null(self):
		array = []
		x = 9
		self.assertFalse(binary_search(array,x))

if __name__ == '__main__': 
  unittest.main() 