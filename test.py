from project import *
import sys

### Testing Methods ### 


def t0():
	
	print('')
	print(' *** Verifying Theorem 1 *** ')
	print('')
	print(' -> size 1000 trees')
	print('')
	for i in range(0, 5): test1(1000, i)

	print('')
	print(' -> size 1100 trees')
	print('')
	for i in range(0, 5): test1(1100, i)

	print('')
	print(' -> size 1200 trees')
	print('')
	for i in range(0, 5): test1(1200, i)
	
	print('')
	print(' *** Verifying Theorem 2 *** ')
	print('')
	print(' -> size 1000 trees')
	print('')
	for i in range(0, 5): test2(1000, i)

	print('')
	print(' -> size 1100 trees')
	print('')
	for i in range(0, 5): test2(1100, i)

	print('')
	print(' -> size 1200 trees')
	print('')
	for i in range(0, 5): test2(1200, i)
	
	print('')
	print(' *** Verifying Theorem 3 *** ')
	print('')
	print(' -> size 1000 trees')
	print('')
	for i in range(0, 5): test3(1000, i)

	print('')
	print(' -> size 1100 trees')
	print('')
	for i in range(0, 5): test3(1100, i)

	print('')
	print(' -> size 1200 trees')
	print('')
	for i in range(0, 5): test3(1200, i)


def test1(size, itr):
	# verify theorem 1

	t = BST.fromList(randList(size))
	s = sFromT(t)

	# variables for theorem 1
	n = len(s)
	h = math.ceil(math.log(n+1, 2))
	csRootT = 0
	p = 0
	rooti = 0

	# fill the variables
	rooti = t.root.index
	csRootT = len(leftForearm(s[rooti])) + len(rightForearm(s[rooti]))
	if (pow(2, h-1) <= n and n <= (pow(2, h-1) + pow(2, h-2) - 2)): p = 1
	elif (n == (pow(2, h-1) + pow(2, h-2) - 1)): p = 0
	else: p = -1

	expectedRot = 2*n - 2*math.floor(math.log(n, 2)) - csRootT + p
	expectedTree = t.root.preorder

	result = a1(s, len(s), t)
	resultRot = result[1]
	resultTree = result[0].root.preorder

	correct = True

	for i in range(0, len(expectedTree)):
		if (resultTree[i].val != expectedTree[i].val):
			correct = False

	if (correct == True):
		print('Test ' + str(itr + 1) + ' passes: Rotations are off by ' + str(abs(expectedRot - resultRot)) + ' ' + str((expectedRot, resultRot)))
	else:
		print('Test ' + str(itr + 1) + ' fails: S is not identical to T!')


def test2(size, itr):
	# verify theorem 2

	t = BST.fromList(randList(size))
	s = sFromT(t)
	while (hasIdentical(s, t) == False):
		s = sFromT(t)

	# variables for theorem 2
	n = len(s)
	h = math.ceil(math.log(n+1, 2))
	csRootT = 0
	p = 0
	rooti = 0
	ni = 0

	# fill the variables
	rooti = t.root.index
	csRootT = len(leftForearm(s[rooti])) + len(rightForearm(s[rooti]))
	if (pow(2, h-1) <= n and n <= (pow(2, h-1) + pow(2, h-2) - 2)): p = 1
	elif (n == (pow(2, h-1) + pow(2, h-2) - 1)): p = 0
	else: p = -1

	markMaxSubtree(s, t.root)

	for node in s.root.preorder:
		if (node.flag == True):
			if (isIn(node, leftForearm(s[rooti])) or isIn(node, rightForearm(s[rooti]))): 
				for key in node:
					if (key.left == None and key.right == None):
						continue
					else:
						ni += 1
			else:
				ni += len(node)

	expectedRot = 2*n - 2*math.floor(math.log(n, 2)) - csRootT + p - 2*ni
	expectedTree = t.root.preorder

	result = a2(s, len(s), t)
	resultRot = result[1]
	resultTree = result[0].root.preorder

	correct = True

	for i in range(0, len(expectedTree)):
		if (resultTree[i].val != expectedTree[i].val):
			correct = False

	if (correct == True):
		print('Test ' + str(itr + 1) + ' passes: Rotations are off by ' + str(abs(expectedRot - resultRot)) + ' ' + str((expectedRot, resultRot)))
	else:
		print('Test ' + str(itr + 1) + ' fails: S is not identical to T!')



def test3(size, itr):
	# verify theorem 3

	t = BST.fromList(randList(size))
	s = sFromT(t)

	# variables for theorem 3
	n = len(s)
	h = math.ceil(math.log(n+1, 2))
	csRootT = 0
	ni = 0
	g = 0
	logni = 0

	# fill the variables
	rooti = t.root.index
	csRootT = len(leftForearm(s[rooti])) + len(rightForearm(s[rooti]))

	updateMark(s, t)
			
	for node in s.root.preorder:
		ni = 0
		if (node.equal == True and node.flag == False):
			g += 1
			if (isIn(node, leftForearm(s[rooti])) or isIn(node, rightForearm(s[rooti]))): 
				for key in node:
					if (key.left == None and key.right == None):
						continue
					else:
						ni += 1
			else:
				ni = len(node)

			logni += math.floor(math.log(ni, 2))

	expectedRot = 2*n - 2*math.floor(math.log(n, 2)) - csRootT  - 2*logni + g + 1
	expectedTree = t.root.preorder

	result = a3(s, len(s), t)
	resultRot = result[1]
	resultTree = result[0].root.preorder

	correct = True

	for i in range(0, len(expectedTree)):
		if (resultTree[i].val != expectedTree[i].val):
			correct = False

		if (resultRot > expectedRot):
			correct = False

	if (correct == True):
		print('Test ' + str(itr + 1) + ' passes: Rotations are off by ' + str(abs(expectedRot - resultRot)) + ' ' + str((expectedRot, resultRot)))
	else:
		print('Test ' + str(itr + 1) + ' fails: Rotations are off by ' + str(abs(expectedRot - resultRot)) + ' ' + str((expectedRot, resultRot)))


def t1():
	t = BST.fromList(randList(random.randint(3,30)))
	s = sFromT(t)
	print('')
	print('---------- T ----------')
	print(t.root)
	print('---------- S ----------')
	print(s.root)
	print('---------- A1 ----------')
	result = a1(s, len(s), t)
	print('Rotations: ' + str(result[1]))
	print(result[0].root)

def t2():
	t = BST.fromList(randList(random.randint(3,30)))
	s = sFromT(t)
	print('')
	print('---------- T ----------')
	print(t.root)
	print('---------- S ----------')
	print(s.root)
	print('---------- A2 ----------')
	result = a2(s, len(s), t)
	print('Rotations: ' + str(result[1]))
	print(result[0].root)

def t3():
	t = BST.fromList(randList(random.randint(3,30)))
	s = sFromT(t)
	print('')
	print('---------- T ----------')
	print(t.root)
	print('---------- S ----------')
	print(s.root)
	print('---------- A3 ----------')
	result = a3(s, len(s), t)
	print('Rotations: ' + str(result[1]))
	print(result[0].root)

if __name__ == '__main__':
	globals()[sys.argv[1]]()
