import unittest
from recursionActivitySelector import recursionActivitySelector
from iterativeActivitySelector import iterativeActivitySelector

class Greedy_algorithm_testcase(unittest.TestCase):
    
    def testcase(self):
        self.assertListEqual(recursionActivitySelector([1,5,6,7,4,8],[2,8,5,3,6,7],-1,6),[0,1,5])           
        self.assertListEqual(iterativeActivitySelector([1,5,6,7,4,8],[2,8,5,3,6,7]),[0,1,5])

if __name__ == '__main__':
    unittest.main()

