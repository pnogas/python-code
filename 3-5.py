#Implement a MyQueue class which implements a queue using two stacks.

#copy stack from 3-2 put add a length attribute (could just pop until an error occurs, but that seems too messy)
class Stack:
	def __init__(self):
		self.stack = []
		self.length = 0

	def push(self, item):
		self.stack.append(item)
		self.length += 1

	def pop(self):
		if self.stack == []:
			raise NameError("can't pop an empty stack")
		else:
			popped_data = self.stack[-1]
			del self.stack[-1]
			self.length -= 1
			return popped_data


class MyQueue:
	def __init__(self):
		self.queue_stack = Stack()
		self.temp_stack = Stack()	 

	def	enqueue(self, item):
		self.queue_stack.push(item)

	def dequeue(self):
		for i in range(0, self.queue_stack.length - 1):
			self.temp_stack.push(self.queue_stack.pop())
		popped_item = self.queue_stack.pop()

		for i in range(0, self.temp_stack.length):
			self.queue_stack.push(self.temp_stack.pop())
		return popped_item

print "Test 1: enqueue 1,2,3 and dequeue 1,2"
x = MyQueue()
x.enqueue(1)
x.enqueue(2)
x.enqueue(3)
print x.dequeue() == 1
print x.dequeue() == 2

