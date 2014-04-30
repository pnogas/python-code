#Given a circular linked list, implement an algorithm which returns node at the beginning of the loop.
#DEFINITION
#Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node, so as to make a loop in the linked list.
#EXAMPLE
#input: A -> B -> C -> D -> E -> C [the same C as earlier]
#output: C

#again, this feels like it doens't translate well to python
def returnLoopNode(loop_list):
	for i in range(0,len(loop_list)):
		if loop_list[i] in (loop_list[:i] + loop_list[i+1:]):
			return loop_list[i]
	raise NameError('no loops in list')

print "Test 1: [1,2,3,4,5,3] "
print returnLoopNode([1,2,3,4,5,3]) == 3

print "Test 2: ['a','b','c','d','b'] "
print returnLoopNode(['a','b','c','d','b']) == 'b'

print "Test 3: [1,2,3,4] "
try:
	returnLoopNode([1,2,3,4])
except NameError as e:
	print 'True'

print "Test 4: ['a','b','b'] "
print returnLoopNode(['a','b','b']) == 'b'

print "Test 5: ['a','a','b','c'] "
print returnLoopNode(['a','a','b','c']) == 'a'
