#Just to test a 3-way tree

class Tree(object):
	def __init__(self):
		self.left = None
		self.right = None
		self.data = None
		self.middle = None

def isTreeBalenced(tree):
	if abs(maxDistance(tree) - minDistance(tree)) < 2:
		return True
	else:
		return False

def maxDistance(tree):
	if tree == None or (tree.left == None and tree.right == None and tree.middle == None):
		return 0

	elif tree.left == None:
		if tree.middle == None:
			return 1 + maxDistance(tree.right)
		elif tree.right == None:
			return 1 + maxDistance(tree.middle)
		else:
			return 1 + max(maxDistance(tree.right), maxDistance(tree.middle))

	elif tree.right == None:
		if tree.middle == None:
			return 1 + maxDistance(tree.left)
		else:
			return 1 + max(maxDistance(tree.left), maxDistance(tree.middle))

	elif tree.middle == None:
		return 1 + max(maxDistance(tree.left), maxDistance(tree.right))

	else: 
		#keep adding and ", maxDistance(tree.direction)" for non-binary case
		return 1 + max(maxDistance(tree.left), maxDistance(tree.right), maxDistance(tree.middle))

def minDistance(tree):
	if tree == None or (tree.left == None and tree.right == None and tree.middle == None):
		return 0

	elif tree.left == None:
		if tree.middle == None:
			return 1 + minDistance(tree.right)
		elif tree.right == None:
			return 1 + minDistance(tree.middle)
		else:
			return 1 + min(minDistance(tree.right), minDistance(tree.middle))

	elif tree.right == None:
		if tree.middle == None:
			return 1 + minDistance(tree.left)
		else:
			return 1 + min(minDistance(tree.left), minDistance(tree.middle))

	elif tree.middle == None:
		return 1 + min(minDistance(tree.left), minDistance(tree.right))

	else: 
		#keep adding and ", maxDistance(tree.direction)" for non-binary case
		return 1 + min(minDistance(tree.left), minDistance(tree.right), minDistance(tree.middle))

root = Tree()

print "Test 0: empty tree"
print isTreeBalenced(root) == True

root.left = Tree()
root.left.left = Tree()
root.left.right = Tree()
root.left.middle = Tree()
root.right = Tree()
root.right.left = Tree()
root.right.right = Tree()
root.right.middle = Tree()
root.middle = Tree()
root.middle.left = Tree()
root.middle.right = Tree()
root.middle.middle = Tree()

print "Test 1: full 3-way tree of depth 2"
print isTreeBalenced(root) == True

root.middle.middle.middle = Tree()

print "Test 2: add a leaf on the middle"
print isTreeBalenced(root) == True

root.middle.middle.middle.right = Tree()

print "Test 3: add a leaf too many on the right of the middle"
print isTreeBalenced(root) == False

root.middle.middle.middle.right = None
root.left.left = None

print "Test 4: trim too long middle & also clip left>left"
print isTreeBalenced(root) == True