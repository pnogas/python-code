#Implement a function to check if a tree is balanced. For the purposes of this question,
#a balanced tree is defined to be a tree such that no two leaf nodes differ in distance from the root by more than one

class Tree(object):
	def __init__(self):
		self.left = None
		self.right = None
		self.data = None

#not necessarily a binary tree so I'll implement it as binary and comment how to extend it

def isTreeBalenced(tree):
	if abs(maxDistance(tree) - minDistance(tree)) < 2:
		return True
	else:
		return False

def maxDistance(tree):
	#keep adding and "tree.direcrection == None" for non-binary case
	if tree == None or tree.left == None and tree.right == None:
		return 0
	#seems messy to have to do this type of checking if the tree is more than binary. elif cases grow exponentially... :(
	elif tree.left == None and tree.right != None:
		return 1 + maxDistance(tree.right)
	elif tree.right == None and tree.left != None:
		return 1 + maxDistance(tree.left)
	else: 
		#keep adding and ", maxDistance(tree.direction)" for non-binary case
		return 1 + max(maxDistance(tree.left), maxDistance(tree.right))

def minDistance(tree):
	#keep adding and "tree.direcrection == None" for non-binary case
	if tree == None or tree.left == None and tree.right == None:
		return 0
	#seems messy to have to do this type of checking if the tree is more than binary. elif cases grow exponentially... :(
	elif tree.left == None and tree.right != None:
		return 1 + minDistance(tree.right)
	elif tree.right == None and tree.left != None:
		return 1 + minDistance(tree.left)
	else: 
		#keep adding and ", minDistance(tree.direction)" for non-binary case
		return 1 + min(minDistance(tree.left), minDistance(tree.right))

root = Tree()
root.data = "root"

print "Test 0: empty tree"
print isTreeBalenced(root) == True

root.left = Tree()
root.left.data = "left"
root.left.left = Tree()
root.left.left.data = "left left"
root.left.right = Tree()
root.left.right.data = "left right"
root.right = Tree()
root.right.data = "right"
root.right.left = Tree()
root.right.left.data = "right left"
root.right.right = Tree()
root.right.right.data = "right right"

print "Test 1: full binary tree of depth 2"
print isTreeBalenced(root) == True

root.left.left.left = Tree()
root.left.left.left.data = "left, left, left"

print "Test 2: add a leaf on the left"
print isTreeBalenced(root) == True

root.left.left.left.left = Tree()
root.left.left.left.left.data = "left, left, left, left"

print "Test 3: add a leaf too many on the left"
print isTreeBalenced(root) == False

root.left.left.left.left = None
root.right.left = None

print "Test 4: trim too long left & also clip right>left"
print isTreeBalenced(root) == True