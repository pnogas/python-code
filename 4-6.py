#Design an algorithm and write code to find the first common ancestor of two nodes in a binary tree. 
#Avoid storing additional nodes in a data structure. NOTE: This is not necessarily a binary search tree

#copy again from 4-3
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

def numberOfDesiredNodes(tree, node1, node2):
	desired_nodes_found = 0
	if tree == None:
		return desired_nodes_found
	if tree == node1 or tree == node2:
		desired_nodes_found += 1
	desired_nodes_found += numberOfDesiredNodes(tree.left, node1, node2)
	#A shortcut to avoid searching another half tree unnecessarily  
	if desired_nodes_found == 2:
		return desired_nodes_found
	else:
		desired_nodes_found += numberOfDesiredNodes(tree.right, node1, node2)
		return desired_nodes_found

def commonAncestor(tree, node1, node2):
	#1. null case
	if tree == None:
		return None
	#2. shortest possible answer
	#(probably not the most efficent but it seems more readable and understandable than the long way I was going to do it)
	if tree == node1:
		if tree.left == node2 or tree.right == node2:
			return tree
	if tree == node2:
		if tree.right == node1 or tree.right == node1:
			return tree
	#3. see if both nodes are on one side
	nodes_on_left = numberOfDesiredNodes(tree.left, node1, node2)
	if nodes_on_left == 2:
		if tree.left == node1 or tree.left == node2:
			return tree.left
		else:
			return commonAncestor(tree.left,node1,node2)
	#this was put after checking the left side to avoid checking the right side if it is not necessary.
	nodes_on_right = numberOfDesiredNodes(tree.right, node1, node2)
	if nodes_on_right == 2:
		if tree.right == node1 or tree.right == node2:
			return tree.right
		else:
			return commonAncestor(tree.right,node1, node2)
	#4.Last option is one on each side
	if nodes_on_right == 1 and nodes_on_left == 1:
		return tree
	#5. error on input? I don't think it should ever get here if the input makes sesnse...
	return "Error, no common ancestor!" 


data = [1,2,3,4,5,6,7,8,9,10]
a = Tree(data)

print "       6       "
print "    /     \    "
print "   3       9   "
print "  / \     / \  "
print " 2   5   8  10 "
print "/   /   /      "
print "1  4   7       "
print " "
print "Test 1: nodes 6,3"
print commonAncestor(a, a, a.left) ==  a

print "Test 2: nodes 3,9"
print commonAncestor(a, a.left, a.right)  ==  a

print "Test 3: nodes 1,2"
print commonAncestor(a, a.left.left.left, a.left.left) ==  a.left.left

print "Test 4: nodes 1,4"
print commonAncestor(a, a.left.left.left, a.left.right.left) ==  a.left

print "Test 5: nodes 1,10"
print commonAncestor(a, a.left.left.left, a.right.right) ==  a