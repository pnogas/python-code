#You have two very large binary trees: T1, with millions of nodes, and T2, with hundreds of nodes. 
#Create an algorithm to decide if T2 is a subtree of T1

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

def isASubtree(T1, T2):
	if T2 == None or T2.data == None:
		return True
	else:
		return traverseBigTree(T1,T2)

def traverseBigTree(T1,T2):
	if T1 == None:
		return False
	if T1.data == T2.data:
		if checkChildren(T1,T2):
			return True
	return isASubtree(T1.right, T2) or isASubtree(T1.left, T2)

def checkChildren(T1,T2):
	if (T1 == None and T2 == None) or (T1.data == None and T2.data == None):
		return True
	elif T1 == None or T2 == None or T1.data == None or T2.data == None:
		return False
	elif T1.data != T2.data:
		return True
	else:
		return checkChildren(T1.right,T2.right) and checkChildren(T1.left, T2.left)

T1 = Tree([])
T2 = Tree([0])
print "Test1: T1 = [], T2 = [0]"
print isASubtree(T1,T2) == False

T1 = Tree([])
T2 = Tree([])
print "Test2: T1 = [], T2 = []"
print isASubtree(T1,T2) == True

T1 = Tree([0])
T2 = Tree([])
print "Test3: T1 = [0], T2 = []"
print isASubtree(T1,T2) == True

T1 = Tree([1])
T2 = Tree([1])
print "Test4: T1 = [1], T2 = [1]"
print isASubtree(T1,T2) == True

T1 = Tree([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
T1 = Tree([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
print "Test5: T1 = T2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]"
print isASubtree(T1,T2) == True

T1 = Tree([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
T2 = Tree([5,6,7])
print "Test6: T1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15], T2 = [5,6,7]"
print isASubtree(T1,T2) == True

T1 = Tree([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
T2 = Tree([2,4,6])
print "Test7: T1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15], T2 = [2,4,6]"
print isASubtree(T1,T2) == False

T1 = Tree([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
T2 = Tree([1,2,3,4,5,6,7])
print "Test8: T1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15], T2 = [1,2,3,4,5,6,7]"
print isASubtree(T1,T2) == True

T1 = Tree([1,2,3,4,5,6,7,8,9,10])
T2 = Tree([])
T2.data = 8
T2.left = Tree([])
T2.left.data = 7
print "Test9: T1 = [1,2,3,4,5,6,7,8,9,10], T2 = [7,8,_]"
print isASubtree(T1,T2) == True