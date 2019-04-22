#Generating the Test Cases and testing for Linear and Binary Search Implementations
# Author: Prajwol Lamichhane

import unittest
from BinarySearch import BinarySearch
from LinearSearch import LinearSearch

class SearchTestcase(unittest.TestCase):

    def test_BinarySearch(self):

        A = [0,1,2,3,4,5]

        #Tests for element which are on the list
        self.assertEqual(BinarySearch(A, 0), 0)
        self.assertEqual(BinarySearch(A, 1), 1)
        self.assertEqual(BinarySearch(A, 2), 2)

        #Tests for element which are not on the list
        self.assertEqual(BinarySearch(A, 10), -1)
        self.assertEqual(BinarySearch(A, 11), -1)


    def test_LinearSearch(self):

        A = [0,1,2,3,4,5]

        #Tests for element which are on the list
        self.assertEqual(LinearSearch(A, 0), 1)
        self.assertEqual(LinearSearch(A, 1), 1)
        self.assertEqual(LinearSearch(A, 2), 1)
        self.assertEqual(LinearSearch(A, 3), 1)
        self.assertEqual(LinearSearch(A, 4), 1)
        self.assertEqual(LinearSearch(A, 5), 1)


        #Tests for element that are not on the list
        self.assertEqual(LinearSearch(A, 10), -1)
        self.assertEqual(LinearSearch(A, 11), -1)

if __name__ == "__main__":
    unittest.main()
