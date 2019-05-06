#Binary Search Tree in Python

class Binary_Search_Tree:

    def __init__(self):
        self._size = 0
        self._root = None

    class _BSTNode:
        def __init__(self,key,value):
            self.key = key
            self.value = value
            self.right = None
            self.left = None

    def add_node(self,key,value):
        z = self._BSTNode(key,value)
        y = None
        x = self._root
        while (x != None):
            y = x
            if(key < x.key) :
                x = x.left
            else:
                x = x.right
        if (y == None):
            self._root = z
        elif (z.key < y.key):
            y.left = z
        else:
            y.right = z
        self._size += 1

    def is_empty(self):
        return self._size == 0

    def size(self):
        return self._size

    def inorder_walk(self):
        nodes = []
        self._inorder_walk(self._root,nodes)
        return nodes

    def _inorder_walk(self,subtree,nodes):
        if subtree:
            self._inorder_walk(subtree.left,nodes)
            nodes.append(subtree.key)
            self._inorder_walk(subtree.right,nodes)

    def preorder_walk(self):
        nodes = []
        self._preorderwalk(self._root,nodes)
        return nodes

    def _preorderwalk(self,subtree,nodes):
        if subtree:
            nodes.append(subtree.key)
            self._preorderwalk(subtree.left,nodes)
            self._preorderwalk(subtree.right,nodes)

    def postorder_walk(self):
        nodes = []
        self._postorderwalk(self._root,nodes)
        return nodes

    def _postorderwalk(self,subtree,nodes):
        if subtree:
            self._postorderwalk(subtree.left,nodes)
            self._postorderwalk(subtree.right,nodes)
            nodes.append(subtree.key)
