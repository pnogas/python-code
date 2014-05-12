#Given a sorted (increasing order) array, write an algorithm to create a binary tree with minimal height.

class Tree(object):
	def __init__(self, sorted_array):
		if sorted_array == []:
			self.data = None
		else:
			self.data = sorted_array[len(sorted_array)/2]

		if sorted_array[:len(sorted_array)/2] != []:
			self.left = Tree(sorted_array[:len(sorted_array)/2])
		else:
			self.left = None

		if sorted_array[(len(sorted_array)/2)+1:] != []:
			self.right = Tree(sorted_array[(len(sorted_array)/2)+1:])
		else:
			self.right = None

#not a full test set but, but it works for now...
a = []
balenced_tree = Tree(a)
print "Test 1: []"
print balenced_tree.data == None and \
balenced_tree.left == None and \
balenced_tree.right == None 

a = [1]
balenced_tree = Tree(a)
print "Test 2: [1]"
print balenced_tree.data == 1 and \
balenced_tree.left == None and \
balenced_tree.right == None

a = [1,2]
balenced_tree = Tree(a)
print "Test 3: [1,2]"
print balenced_tree.data == 2 and \
balenced_tree.left.data == 1 and \
balenced_tree.right == None

a = [1,2,3,4,5,6,7,8,9,10]
balenced_tree = Tree(a)
print "Test 4: [1,2,3,4,5,6,7,8,9,10]"
print balenced_tree.data == 6 and \
balenced_tree.left.data == 3 and \
balenced_tree.right.data == 9 and \
balenced_tree.left.left.data == 2 and \
balenced_tree.left.right.data == 5 and \
balenced_tree.right.left.data == 8 and \
balenced_tree.right.right.data == 10 and \
balenced_tree.left.left.left.data == 1 and \
balenced_tree.left.right.left.data == 4 and \
balenced_tree.right.left.left.data == 7