import unittest
from binary_search import binary_search

class TestBinarySearch(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsNone(binary_search([], 5))

    def test_single_element(self):
        self.assertEqual(binary_search([3], 3), 0)
        self.assertIsNone(binary_search([3], 5))

    def test_multiple_elements(self):
        lst = [1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(binary_search(lst, 1), 0)
        self.assertEqual(binary_search(lst, 4), 3)
        self.assertEqual(binary_search(lst, 7), 6)
        self.assertIsNone(binary_search(lst, 0))
        self.assertIsNone(binary_search(lst, 8))

if __name__ == '__main__':
    unittest.main()

