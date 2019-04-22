import unittest
from InsertionSort import insertionSort
from MergeSort import mergesort


class SortingTestCase(unittest.TestCase):
    """Testing Insertion and Merge Sort"""

    def test_insertion_sort(self):

        A = [0,9,8,3,7,6]
        sorted_A = [0,3,6,7,8,9]

        #Tests for sorting of the list
        self.assertEqual(insertionSort(A), sorted_A)


    def test_merge_sort(self):

        A = [0,9,8,3,7,6]
        sorted_A = [0,3,6,7,8,9]


        #Tests for the sorting of the list
        self.assertEqual(insertionSort(A), sorted_A)



if __name__ == "__main__":
    unittest.main()
