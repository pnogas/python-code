# How would you design a stack which, in addition to push and pop, also has a function min which returns the minimum element? 
#Push, pop and min should all operate in O(1) time.

#you would simply need to store a variable called min and update it as needed.

class Stack:
	def __init__(self):
		self.minimum = None
		self.stack = []

	def push(self, item):
		self.stack.append(item)
		if self.minimum == None:
			self.minimum = item
		else:
			self.minimum = min(self.minimum, item)

	def pop(self):
		if self.stack == []:
			raise NameError("can't pop an empty stack")
		else:
			popped_data = self.stack[-1]
			del self.stack[-1]
			#I think this might violate the O(1) requirement
			if len(self.stack) > 0:
				self.minimum = min(self.stack)
			else:
				self.minimum = None
			return popped_data

	def min(self):
		return self.minimum

print "Test1: push 3,2,1,5,6; ask min;"
x = Stack()
x.push(3)
x.push(2)
x.push(1)
x.push(5)
x.push(6)
print x.min() == 1

print "Test2: pop 6,5,1; ask min;"
x.pop()
x.pop()
x.pop()
print x.min() == 2

print "Test3: pop 2,3 and error"
x.pop()
x.pop()
try:
	x.pop()
except NameError as e:
	print 'True'
