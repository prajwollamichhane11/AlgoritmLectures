class Node:
	def __init__(self,value):
		self.left = None
		self.right = None
		self.parent = None
		self.key = value

class BinarySearchTree:
	def __init__(self):
		self.root = None
		self.size = 0

	def Insert(self,a):
		if self.root == None:
			self.root = Node(a)
			self.size += 1

		else:
			self.InsertNode(self.root,a)

	def InsertNode(self,currentNode, a):
		if(currentNode.key > a):
			if(currentNode.left):
				self.InsertNode(currentNode.left,a)
			else:
				currentNode.left = Node(a)
				currentNode.left.parent = currentNode
				self.size += 1
		else:
			if(currentNode.right):
				self.InsertNode(currentNode.right,a)
			else:
				currentNode.right = Node(a)
				currentNode.right.parent = currentNode
				self.size += 1


	def SearchKey(self,searchParameter):
		if(self.root):
			self.Search(self.root,searchParameter)
		else:
			print("The tree is empty.")

	def Search(self, node, searchParameter):
		if (node):
			if node.key == searchParameter:
				print("The Node Exists")

			else:
				if (node.key > searchParameter):
					self.Search(node.left,searchParameter)
				else:
					self.Search(node.right,searchParameter)

		else:
			print("Node doesnot Exist.")


	def SmallestKey(self):
		if self.root:
			self.Small(self.root)
		else:
			print("Tree is empty")

	def Small(self, node):
		if node.left == None:
			print("Smallest Node:" + str(node.key))
		else:
			self.Small(node.left)

	def LargestKey(self):
		if self.root:
			self.Large(self.root)

	def Large(self, node):
		if node.right == None:
			print("Large Found")
		else:
			Large(node.right)

	def Preorder(self):
		if self.root:
			self.PreorderTraversal(self.root)

	def PreorderTraversal(self,node):
		if node == None:
			return
		else:
			print(node.key)
			self.PreorderTraversal(node.left)
			self.PreorderTraversal(node.right)

	def size():
		return self.size


tree = BinarySearchTree()
A= [25, 15, 50, 10, 22, 35, 70, 4, 12, 18, 24, 31, 44, 66, 90]
for i in A:
	tree.Insert(i)








