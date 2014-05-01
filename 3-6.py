#Write a program to sort a stack in ascending order. You should not make any assumptions about how the stack is implemented. 
#The following are the only functions that should be used to write this program: push | pop | peek | isEmpty.

class Stack:
	def __init__(self):
		self.stack = []

	def push(self, item):
		self.stack.append(item)

	def pop(self):
		if self.stack == []:
			raise NameError("can't pop an empty stack")
		else:
			popped_data = self.stack[-1]
			del self.stack[-1]
			return popped_data

	def peek(self):
		if self.stack == []:
			raise NameError("can't pop an empty stack")
		else:
			return self.stack[-1]

	def isEmpty(self):

		if self.stack == []:
			return True
		else:
			return False

def sortStack(stack):
	temp_stack = Stack()
	temp_value = None
	while not stack.isEmpty():
		temp_value = stack.pop()
		while (not temp_stack.isEmpty()) and temp_stack.peek() < temp_value:
			stack.push(temp_stack.pop())
		temp_stack.push(temp_value)
	return temp_stack

x = Stack()
x.push(2)
x.push(5)
x.push(3)
x.push(4)

print 'Test1: [2,5,3,4]'
print sortStack(x).stack == [2,3,4,5]	