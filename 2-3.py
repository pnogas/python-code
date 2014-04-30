#Implement an algorithm to delete a node in the middle of a single linked list, given
#only access to that node.
#EXAMPLE
#Input: the node ‘c’ from the linked list a->b->c->d->e
#Result: nothing is returned, but the new linked list looks like a->b->d->e

def deleteNode(linked_list,node):
	for element in linked_list:
		if element == node:
			if element.previous() && element.next():
				linked_list.previous().next() = entry.next()
				linked_list.next().previous() = entry.previous()
			#last node
			elif element.previous() && not element.next():
				linked_list.previous().next() = None
			#first node
			elif not element.previous() && element.next():
				linked_list.next().previous() = None
			else:
				print "error with linked list pointers?"
				raise Exception("error with linked list pointers?")
# still really don't know how to delete the node itself, but at least now it's out of the list
#again, maybe not best to be trying to implement this in python...



