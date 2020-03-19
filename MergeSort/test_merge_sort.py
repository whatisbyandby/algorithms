import unittest
from MergeSort.merge_sort import merge_sort


class MergeSortTest(unittest.TestCase):

    def test_sorted(self):
        test_array = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        result = merge_sort(test_array)
        self.assertEqual(result, [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_already_sorted(self):
        test_array = [1, 2, 3, 4, 5]
        result = merge_sort(test_array)
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_with_zeros(self):
        test_array = [0, 0, 0, 0, 0]
        result = merge_sort(test_array)
        self.assertEqual(result, [0, 0, 0, 0, 0])

    def test_not_equal(self):
        test_array = [9, 0, 3, 2]
        result = merge_sort(test_array)
        self.assertNotEqual(result, [9, 0, 3, 2])


if __name__ == "__main__":
    unittest.main()
