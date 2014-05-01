#Imagine a (literal) stack of plates. If the stack gets too high, it might topple. 
#Therefore, in real life, we would likely start a new stack when the previous stack exceeds some threshold. 
#Implement a data structure SetOfStacks that mimics this. 
#SetOfStacks should be composed of several stacks, and should create a new stack once the previous one exceeds capacity. 
#SetOfStacks.push() and SetOfStacks.pop() should behave identically to a single stack (that is, pop() should return the same values as it would if there were just a single stack).

#FOLLOW UP
#Implement a function popAt(int index) which performs a pop operation on a specific sub-stack.

class SetOfStacks:
	def __init__(self, capacity):
		self.stacks = []
		if capacity < 1:
			raise NameError("Can't have stacks of that height")
		else:
			self.capacity = capacity

	def push(self, item):
		if self.stacks == []:
			self.stacks.append([item])
		else:
			if len(self.stacks[-1]) >= self.capacity:
				self.stacks.append([item])
			else:
				self.stacks[-1].append(item)

	def pop(self):
		if self.stacks == []:
			raise NameError("can't pop an empty stack")
		else:
			popped_data = self.stacks[-1][-1]
			if len(self.stacks[-1]) == 1:
				del self.stacks[-1]
			else:
				del self.stacks[-1][-1]
			return popped_data

	def popAt(self, index):
		if self.stacks == []:
			raise NameError("can't pop an empty stack")
		elif index-1 > len(self.stacks):
			raise NameError("index is out of range")
		else:
			popped_data = self.stacks[index-1][-1]
			if len(self.stacks[index-1]) == 1:
				del self.stacks[-1]
			elif len(self.stacks) == index:
				del self.stacks[-1][-1]
			else:
				self.stacks[index-1][-1] = self.stacks[index][0]
				
				for i in range(index, len(self.stacks)):
					for j in range(0, len(self.stacks[i])-1 ):
						self.stacks[i][j] = self.stacks[i][j+1]
					if i < len(self.stacks) -1:
						self.stacks[i][-1] = self.stacks[i+1][0]
				del self.stacks[-1][-1]
				if len(self.stacks[-1]) == 0:
					del self.stacks[-1]
		return popped_data
'''
print "Test 1: make a stack with limit 3. push [1,2,3],[4,5,6],[7,8]"
x = SetOfStacks(3)
x.push(1)
x.push(2)
x.push(3)
x.push(4)
x.push(5)
x.push(6)
x.push(7)
x.push(8)
print x.stacks == [[1,2,3],[4,5,6],[7,8]]

print "Test 2: pop 8"
print x.pop() == 8 and x.stacks == [[1,2,3],[4,5,6],[7]]

print "Test 3: pop 7"
print x.pop() == 7 and x.stacks == [[1,2,3],[4,5,6]]

print "Test 4: pop 6,5,4"
x.pop()
x.pop()
x.pop()
print x.stacks == [[1,2,3]]

print "Test 5: pop 3,2,1"
x.pop()
x.pop()
x.pop()
print x.stacks == []

try:
	x.pop()
except NameError as e:
	print "Test 6: pop too much"
	print 'True'
'''
print "Test 1b: make a stack with limit 4."
print "push [1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14]"
x = SetOfStacks(4)
for i in range (1,15):
	x.push(i)
print x.stacks == [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14]]

print "Test 2b: pop 12 from stack 3"
print x.popAt(3) == 12 and x.stacks == [[1,2,3,4],[5,6,7,8],[9,10,11,13],[14]]

print "Test 3b: pop 8 from stack 2"
print x.popAt(2) == 8 and x.stacks == [[1,2,3,4],[5,6,7,9],[10,11,13,14]]

print "Test 4b: pop 4 from stack 1"
print x.popAt(1) == 4 and x.stacks == [[1,2,3,5],[6,7,9,10],[11,13,14]]