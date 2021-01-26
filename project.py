from bst import *

import random

#----------------------------------#
#				 A1                #
#----------------------------------#
def a1(s, n, t):
	# input: source, size, target
	# outout: source tree that is identical to target

	counter = Counter()

	# 1
	q = s.copy()

	# 2, 3
	h = math.ceil(math.log(n+1, 2))
	rooti = 0
	if (pow(2, h-1) <= n and n <= (pow(2, h-1) + pow(2, h-2) - 1)):
		rooti = n - pow(2, h-2)
	if ((pow(2, h-1) + pow(2, h-2)) <= n and n <= (pow(2, h) - 1)):
		rooti = pow(2, h-1) - 1

	# 4
	while (q.root.val != q[rooti].val):	
		q.rot(q[rooti].p.index, rooti)
		counter.inc()

	# 5
	while (len(leftForearm(q.root)) < len(q.root.left)):
		lq = leftForearm(q.root)
		for node in lq:
			if (node.left != None):
				q.rot(node.index, node.left.index)
				counter.inc()

	while (len(rightForearm(q.root)) < len(q.root.right)):
		rq = rightForearm(q.root)
		for node in rq:
			if (node.right != None):
				q.rot(node.index, node.right.index)
				counter.inc()

	# 6
	s = h
	
	lq = leftForearm(q.root)
	rq = rightForearm(q.root)
	
	if (pow(2, h-1) <= n and n <= (pow(2, h-1) + pow(2, h-2) - 2)):
		k = n - pow(2, h-1) + 1
		for i in range(0, k):
			q.rot(lq[i].index, lq[i].right.index)
			lq.pop(i)
			counter.inc()

		s = h - 1
	
	for j in range(s - 2, 0, -1):
		k = pow(2, j) - 1
		for i in range(0, k):
			q.rot(lq[i].index, lq[i].right.index)
			lq.pop(i)
			counter.inc()


	if (n == (pow(2, h-1) + pow(2, h-2) - 1)): s = h - 1

	if ((pow(2, h-1) + pow(2, h-2)) <= n and n <= (pow(2, h) - 2)):
		k = n - pow(2, h-1) - pow(2, h-2) + 1
		p = len(rq)

		for i in range(p - 3, p - 2*k, -2):
			q.rot(rq[i].index, rq[i].left.index)
			rq.pop(i)
			counter.inc()

		s = h - 1
	
	for j in range(s - 2, 0, -1):
		k = pow(2, j) - 1
		for i in range(0, k):
			q.rot(rq[i].index, rq[i].left.index)
			rq.pop(i)
			counter.inc()


	return (q, counter.count)



#----------------------------------#
#				 A2                #
#----------------------------------#
def a2(s, n, t):
	# input: source, size, target
	# outout: source tree that is identical to target

	counter = Counter()

	# 1
	q = s.copy()

	# 2, 3
	h = math.ceil(math.log(n+1, 2))
	rooti = 0
	if (pow(2, h-1) <= n and n <= (pow(2, h-1) + pow(2, h-2) - 1)):
		rooti = n - pow(2, h-2)
	if ((pow(2, h-1) + pow(2, h-2)) <= n and n <= (pow(2, h) - 1)):
		rooti = pow(2, h-1) - 1

	# 4
	while (q.root.val != q[rooti].val):	
		q.rot(q[rooti].p.index, rooti)
		counter.inc()

	# identify identical subtree and do work
	updateMark(q, t)

	fls = [] 	# nodes not supposed to be on left forearm
	frs = []	# nodes not supposed to be on right forearm

	for node in q.root.preorder:
		if (node.flag == True):
			if (node.index == t.root.index):
				return (q, counter.count)

			elif (node.index < rooti): 
				if (isIn(node, leftForearm(t.root))):
					fls.extend(node.left.inorder)
				else:
					fls.extend(node.inorder)

			else: 
				if (isIn(node, rightForearm(t.root)) and node.right != None):
					frs.extend(node.right.inorder)
				else:
					frs.extend(node.inorder)
	
	# 5	
	while (len(leftForearm(q.root)) < (len(q.root.left) - len(fls))):
		lq = leftForearm(q.root)
		for node in lq:
			if (node.left != None and node.left.flag == False and node.flag == False):
				q.rot(node.index, node.left.index)
				counter.inc()

	while (len(rightForearm(q.root)) < (len(q.root.right) - len(frs))):
		rq = rightForearm(q.root)
		for node in rq:
			if (node.right != None and node.right.flag == False and node.flag == False):
				q.rot(node.index, node.right.index)
				counter.inc()
	
	# 6
	s = h

	lq = q.root.left.inorder
	rq = q.root.right.inorder
	rq.reverse()
	lt = leftForearm(t.root)
	rt = rightForearm(t.root)
	
	if (pow(2, h-1) <= n and n <= (pow(2, h-1) + pow(2, h-2) - 2)):
		k = n - pow(2, h-1) + 1
		for i in range(0, k):
			if (isIn(lq[i], fls) == False):
				q.rot(lq[i].index, lq[i].right.index)
				lq.pop(i)
				counter.inc()
			else:
				lq.pop(i)
				continue
		s = h - 1
	
	for j in range(s - 2, 0, -1):
		k = pow(2, j) - 1
		for i in range(0, k):
			if (isIn(lq[i], fls) == False):
				q.rot(lq[i].index, lq[i].right.index)
				lq.pop(i)
				counter.inc()
			else:
				lq.pop(i)
				continue

	if (n == (pow(2, h-1) + pow(2, h-2) - 1)): s = h - 1

	if ((pow(2, h-1) + pow(2, h-2)) <= n and n <= (pow(2, h) - 2)):
		k = n - pow(2, h-1) - pow(2, h-2) + 1
		p = len(rq)

		for i in range(p - 3, p - 2*k, -2):
			if (isIn(rq[i], frs) == False):
				q.rot(rq[i].index, rq[i].left.index)
				rq.pop(i)
				counter.inc()
			else:
				rq.pop(i)
				continue
		s = h - 1
	
	for j in range(s - 2, 0, -1):
		k = pow(2, j) - 1
		for i in range(0, k):
			if (isIn(rq[i], frs) == False):
				q.rot(rq[i].index, rq[i].left.index)
				rq.pop(i)
				counter.inc()
			else:
				rq.pop(i)
				continue

	return (q, counter.count)



#----------------------------------#
#				 A3                #
#----------------------------------#
def a3(s, n, t):
	# input: source, size, target
	# outout: source tree that is identical to target

	q = s.copy()
	c = 0



	# 2, 3
	h = math.ceil(math.log(n+1, 2))
	rooti = 0
	if (pow(2, h-1) <= n and n <= (pow(2, h-1) + pow(2, h-2) - 1)):
		rooti = n - pow(2, h-2)
	if ((pow(2, h-1) + pow(2, h-2)) <= n and n <= (pow(2, h) - 1)):
		rooti = pow(2, h-1) - 1

	# 4
	while (q.root.val != q[rooti].val):	
		q.rot(q[rooti].p.index, rooti)
		c += 1

	updateMark(q, t)
	if (q.root.flag == True):
		return (q, 0)

	equalNodes = []

	for node in q.root.preorder:
		if (node.flag == False and node.equal == True):
			equalNodes.append(node)

	for node in equalNodes:

			tempT = BST()
			for key in t[node.index].preorder:
				tempT.insert(Node(key.val))

			tempS = BST()
			for key in q.discard(node):
				tempS.insert(Node(key))

			result = a1(tempS, len(tempS), tempT)
			resultTree = result[0]
			c += result[1]

			for node in resultTree.root.preorder:
				q.insert(Node(node.val))
	
	resultA2 = a2(q, len(q), t)

	c += resultA2[1]

	return (resultA2[0], c)


### Helper Methods ### 

class Counter(object):
	def __init__(self):
		self.count = 0
	def inc(self):
		self.count += 1


def isIn(node, l):
	# input: a node and a list of nodes
	# output: True if the node is in the list

	if (len(l) == 0): return False
	for ele in l:
		if (ele.val == node.val):
			return True
	return False


def flipCoin(p):
	# input: probablity 0 ~ 1
	# output: p probablity to return True

    r = random.random()
    return r < p


def sFromT(t):
	# input: a almost balanced tree t
	# output: a randomly rotated tree s

	s = t.copy()
	for i in range(0, len(s)):
		if (flipCoin(0.01) == True):
			continue
		elif(flipCoin(0.5) == True and s.root.index != i):
			s.rot(s[i].p.index, i)
		else:
			continue
	s.updateInterval()
	return s


def randList(size):
	# input: size of the list
	# output: a list contatins size number of random int (1, 2size)

	randomList = []

	def uniqueInsert():
		n = random.randint(1,size * 5)
		if (n not in randomList):
			randomList.append(n)
		else:
			uniqueInsert()

	for i in range(0, size):
		uniqueInsert()

	return randomList


def rightForearm(node):
	# input: a node from bst
	# output: a list of nodes of the right forearm starting at this node

	start = node.right
	result = []

	def next(current, list):
		if (current != None):
			list.append(current)
			next(current.left, result)

	next(start, result)
	return result


def leftForearm(node):
	# input: a node from bst
	# output: a list of nodes of the left forearm starting at this node

	start = node.left
	result = []

	def next(current, list):
		if (current != None):
			list.append(current)
			next(current.right, result)

	next(start, result)
	return result

def updateMark(s, t):
	s.updateIndex()
	s.updateInterval()
	t.updateIndex()
	t.updateInterval()
	
	for node in s:
		node.flag = False
		node.equal = False
	for node in t:
		node.flag = False
		node.equal = False

	markMaxSubtree(s, t.root)
	markEqualSubtree(s, t.root.left)
	markEqualSubtree(s, t.root.right)


def markMaxSubtree(s, rootT):
	# input: source Tree, root of target Tree
	# modify: flag the root of max subtree as True

	if (rootT == None): return None
	if (rootT.interval == s[rootT.index].interval):
		sNodes = s[rootT.index].preorder
		tNodes = rootT.preorder
		flag = True

		for i in range(0, len(sNodes)):
			if (sNodes[i].val != tNodes[i].val):
				flag = False
				break

		if (flag == True):
			if (rootT.left != None or rootT.right != None):
				rootT.flag = True
				s[rootT.index].flag = True
		else:
			markMaxSubtree(s, rootT.left)
			markMaxSubtree(s, rootT.right)
	else:
		markMaxSubtree(s, rootT.left)
		markMaxSubtree(s, rootT.right)


def markEqualSubtree(s, rootT):
	# input: source Tree, root of target Tree
	# modify: flag the root of equivalent subtree as True

	if(s.root.flag == True): return None
	if (rootT == None): return None
	if (rootT.interval == s[rootT.index].interval):
		if (rootT.left != None or rootT.right != None and rootT.flag == False):
			s[rootT.index].equal = True
	else:
		s[rootT.index].equal = False
		markEqualSubtree(s, rootT.left)
		markEqualSubtree(s, rootT.right)


def hasIdentical(s, t):
	# input: tree s, tree t
	# output: True if the two tree has identical subtree

	markMaxSubtree(s, t.root)
	for node in s:
		if (node.flag == True):
			return True
	return False

def hasEquivalent(s, t):
	# input: tree s, tree t
	# output: True if the two tree has equivalent subtree

	markEqualSubtree(s, t.root)
	for node in s:
		if (node.equal == True):
			return True
	return False
	






	






	
