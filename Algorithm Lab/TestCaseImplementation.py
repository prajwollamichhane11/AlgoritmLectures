#Generating the Test Cases and testing for Linear and Binary Search Implementations
# Author: Prajwol Lamichhane

import unittest
from BinarySearch import BinarySearch
from LinearSearch import LinearSearch

class SearchTestcase(unittest.TestCase):

    def test_BinarySearch(self):

        A = [0,1,2,3,4,5]
        A = list(range(6))

        #Tests for element which are on the list
        self.assertEqual(BinarySearch(A, 0), 0)
        self.assertEqual(BinarySearch(A, 1), 1)
        self.assertEqual(BinarySearch(A, 2), 2)
        self.assertEqual(BinarySearch(A, 3), 3)
        self.assertEqual(BinarySearch(A, 4), 4)
        self.assertEqual(BinarySearch(A, 5), 5)


        #Tests for element which are not on the list
        #self.assertEqual(test_BinarySearch(A, 10), -1)
        #self.assertEqual(test_BinarySearch(A, 11), -1)


    def test_LinearSearch(self):

        A = [0,1,2,3,4,5]
        A = list(range(6))

        #Tests for element which are on the list
        self.assertEqual(LinearSearch(A, 0), 0)
        self.assertEqual(LinearSearch(A, 1), 1)
        self.assertEqual(LinearSearch(A, 2), 2)
        self.assertEqual(LinearSearch(A, 3), 3)
        self.assertEqual(LinearSearch(A, 4), 4)
        self.assertEqual(LinearSearch(A, 5), 5)


        #Tests for element that are not on the list
        #self.assertEqual(linear_search(A, 10), -1)
        #self.assertEqual(linear_search(A, 11), -1)

if __name__ == "__main__":
    unittest.main()
