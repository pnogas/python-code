#Given a binary search tree, design an algorithm which creates a linked list of all the nodes at each depth 
#(i.e., if you have a tree with depth D, you'll have D linked lists)

class Tree(object):
	def __init__(self, sorted_array):
		if sorted_array == []:
			self.data = None
			print "hi"
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

def treeToLists(tree, depth=-1, list_of_lists=[[]]):
	if depth == -1:
		#I don't like that this needs to be cleared... I guess this needs to be changed to a method of the tree object
		list_of_lists=[[]]
	current_depth = depth + 1
	if len(list_of_lists) <= current_depth:
		list_of_lists.append([])
	if tree.data != None:
		list_of_lists[current_depth].append(tree.data)
	if tree.left != None:
		treeToLists(tree.left, current_depth, list_of_lists)
	if tree.right != None:
		treeToLists(tree.right, current_depth, list_of_lists)
	if current_depth == 0:
		return list_of_lists

z = []
balenced_tree1 = Tree(z)

print "Test 1: [[]]"
print treeToLists(balenced_tree1) == [[]]

a = [1]
balenced_tree2 = Tree(a)

print "Test 2: [[1]]"
print treeToLists(balenced_tree2) == [[1]]

b = [1,2]
balenced_tree3 = Tree(b)

print "Test 3: [[2],[1]]"
print treeToLists(balenced_tree3) == [[2],[1]]

c = [1,2,3,4,5,6,7,8,9,10]
balenced_tree4 = Tree(c)

print "Test 4: [[6],[3,9],[2,5,8,10],[1,4,7]]"
print treeToLists(balenced_tree4) == [[6],[3,9],[2,5,8,10],[1,4,7]]

d = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
balenced_tree5 = Tree(d)
print treeToLists(balenced_tree5)
