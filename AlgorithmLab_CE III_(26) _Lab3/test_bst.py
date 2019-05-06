import unittest
from Binary_Search_Tree import Binary_Search_Tree

class BinarySearchTestcase(unittest.TestCase):
        def test_bst(self):
            bst = Binary_Search_Tree()

            bst.add_node(10,"Apple")
            self.assertEqual(bst.size(),1)

            bst.add_node(20,"Ball")
            self.assertEqual(bst.size(),2)

            bst.add_node(15,"Cat")
            self.assertEqual(bst.size(),3)

            bst.add_node(30,"Dog")
            self.assertEqual(bst.size(),4)

            self.assertListEqual(bst.inorder_walk(),[10,15,20,30])

            self.assertListEqual(bst.preorder_walk(),[10,20,15,30])

            self.assertListEqual(bst.postorder_walk(),[15,30,20,10])



if __name__ == "__main__":
    unittest.main()
