#You have two numbers represented by a linked list, where each node contains a single digit. 
#The digits are stored in reverse order, such that the 1's digit is at the head of the list. 
#Write a function that adds the two numbers and returns the sum as a linked list.
#EXAMPLE
#Input: (3 -> 1 -> 5) + (5 -> 9 -> 2)
#Output: 8 -> 0 -> 8

#Assume input of [] is possible but None is not
def addLinkedLists(a_node,b_node):
	list_sum = []
	node_sum = 0
	carry = 0
	#shortcut if one is empty
	if a_node == [] or b_node == []:
		return a_node + b_node
	if len(a_node) > len(b_node):
		b_node.extend([0] * (len(a_node) - len(b_node)) )
	elif len(a_node) < len(b_node):
		a_node.extend([0] * (len(b_node) - len(a_node)) )
	for i in range(0,len(a_node)):
		#At this point, I realized that there may not be much value in trying to adapt these to python...
		node_sum = a_node[i] + b_node[i] + carry
		if node_sum < 10:
			list_sum.append(node_sum)
			carry = 0
		elif node_sum > 9 and node_sum < 18:
			list_sum.append(int(str(node_sum)[1]))
			carry = 1
			#just realized I'm not checking for integer value here, but assume it's okay
		else:
			raise NameError('improper digit input')
	if carry == 1:
		list_sum.append(1)
	return list_sum

#improved version that doesn't modify the inital list
def addLinkedLists2(a_node,b_node):
	list_sum = []
	node_sum = 0
	carry = 0
	#shortcut if one is empty
	if a_node == [] or b_node == []:
		return a_node + b_node
	shortest_length = min(len(a_node),len(b_node))
	for i in range(0,shortest_length):
		node_sum = a_node[i] + b_node[i] + carry
		if node_sum < 10:
			list_sum.append(node_sum)
			carry = 0
		elif node_sum > 9 and node_sum < 18:
			list_sum.append(int(str(node_sum)[1]))
			carry = 1
			#just realized I'm not checking for integer value here, but assume it's okay
		else:
			raise NameError('improper digit input')
	if len(a_node) > len(b_node):
		for i in range(shortest_length, len(a_node)):
			list_sum.append(a_node[i] + carry)
			carry = 0
	elif len(b_node) > len(a_node):
		for i in range(shortest_length, len(b_node)):
			list_sum.append(b_node[i] + carry)
			carry = 0
	elif carry == 1:
		list_sum.append(1)
	return list_sum

#Assume that negative numbers are not included
print "Test 1: [],[1,2,3] "
print addLinkedLists2([],[1,2,3]) == [1,2,3]

print "Test 2: [4,5,6],[] "
print addLinkedLists2([4,5,6],[]) == [4,5,6]

print "Test 3: [4,5,6],[1,2,3] "
print addLinkedLists2([4,5,6],[1,2,3]) == [5,7,9]

print "Test 4: [4,5,6],[1,2] "
print addLinkedLists2(a,b) == [5,7,6]

print "Test 5: [4,5],[1,2,3,4,5] "
print addLinkedLists2([4,5],[1,2,3,4,5]) == [5,7,3,4,5]		
