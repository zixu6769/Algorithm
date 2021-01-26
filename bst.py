
# https://awesomeopensource.com/project/joowani/binarytree
# pip install binarytree
from binarytree import Node

import random
import math

class Node(Node):

	def __init__(self, value):
		self.val = value
		self.p = None
		self.left = None
		self.right = None
		self.index = None
		self.interval = None
		self.flag = False
		self.equal = False

	def p(self):
		return self.p

	def left(self):
		return self.left

	def right(self):
		return self.right

	def index(self):
		return self.index

	def interval(self):
		return self.interval

	def flag(self):
		return self.flag

	def equal(self):
		return self.equal


class BST(list):
	
	def __init__(self):
		super().__init__()
		self.root = None

	@classmethod
	def fromList(cls, keys):
		# almost complete tree

		tree = BST()
		keys.sort()
		n = len(keys)
		h1 = math.ceil(math.log(n+1, 2))
		h2 = math.floor(math.log(n+1, 2))

		if (h1 > h2):
			extraLeaves = []
			tempKeys = keys.copy()
			numOfExtra = n - (pow(2, h2) - 1)
			index = 0

			for i in range(0, numOfExtra):
				extraLeaves.append(keys[index])
				tempKeys.remove(keys[index])
				index += 2

			tree.root = tree.balanceInsert(tempKeys, 0, len(tempKeys)-1, None, None)

			for key in extraLeaves:
				tree.insert(Node(key))

		else:
			tree.root = tree.balanceInsert(keys, 0, len(keys)-1, None, None)

		tree.updateIndex()
		tree.updateInterval()

		return tree



	######### Methods ######### 

	def discard(self, node):
		if (self.root.index == node.index):
			self.root = None

		elif (node.index < node.p.index):
			node.p.left = None
		else:
			node.p.right = None
		removed = []
		for key in node.preorder:
			removed.append(key.val)
			self.remove(key)
		return removed

	def updateIndex(self):
		for j in range(1, len(self)):
			key = self[j]
			i = j - 1
			while (i >= 0 and self[i].val > key.val):
				self[i + 1] = self[i]
				i -= 1
			self[i + 1] = key

		for i in range(0, len(self)):
			self[i].index = i


	def updateInterval(self):
		nodes = self.root.postorder
		for node in nodes:
			if (node.left == None and node.right ==None):
				node.interval = (node.index, node.index)
			elif (node.right == None):
				node.interval = (node.left.interval[0], node.index)
			elif (node.left == None):
				node.interval = (node.index, node.right.interval[1])
			else:
				node.interval = (node.left.interval[0], node.right.interval[1])

	def insert(self, z):
		
		y = None
		x = self.root
		while (x != None):
			y = x
			if (z.val < x.val):
				x = x.left
			else:
				x = x.right
		z.p = y
		if (y == None):
			self.root = z # tree is empty
		elif (z.val < y.val):
			y.left = z
		else:
			y.right = z

		self.append(z)

	def balanceInsert(self, keys, l, r, node, p):
		# helper function for building balanced tree
		if (l > r): return node
		mid = (l + r) // 2
		node = Node(keys[mid])
		self.append(node)
		node.p = p
		node.left = self.balanceInsert(keys, l, mid-1, node.left, node)
		node.right = self.balanceInsert(keys, mid+1, r, node.right, node)
		return node

	def copy(self):
		tree = BST()
		nodes = self.root.preorder
		for node in nodes:
			tree.insert(Node(node.val))
		tree.updateIndex()
		tree.updateInterval()
		return tree


	def rot(self, parent, child):

		if (parent > child):

			self[parent].left = self[child].right
			if (self[child].right != None):
				self[child].right.p = self[parent]
			self[child].p = self[parent].p
			if (self[parent].p == None):
				self.root = self[child]
			elif(self[parent] == self[parent].p.right):
				self[parent].p.right = self[child]
			else:
				self[parent].p.left = self[child]
			self[child].right = self[parent]
			self[parent].p = self[child]

		else:
			
			self[parent].right = self[child].left
			if (self[child].left != None):
				self[child].left.p = self[parent]
			self[child].p = self[parent].p
			if (self[parent].p == None):
				self.root = self[child]
			elif (self[parent] == self[parent].p.left):
				self[parent].p.left = self[child]
			else:
				self[parent].p.right = self[child]
			self[child].left = self[parent]
			self[parent].p = self[child]
