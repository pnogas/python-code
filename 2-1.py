#Write code to remove duplicates from an unsorted linked list.
#FOLLOW UP How would you solve this problem if a temporary buffer is not allowed?

'''def removeDuplicates2(linked_list):
	buff = set()
	for entry in linked_list:
		if entry in buff:
			linked_list.previous().next() = entry.next()
			linked_list.next().previous() = entry.previous()
			# how to delete the entry?
		else:
			buff.union(set(entry))
	return linked_list''' #it seems that python doesn't really do linked lists, but if it did, it would probably look similar to this.

def removeDuplicates(linked_list):
	buff = list()
	for entry in linked_list:
		if entry not in buff:
			buff.append(entry)
	return buff

print "Test 1: []"
print removeDuplicates([]) == []

print "Test 2: [1]"
print removeDuplicates([1]) == [1]

print "Test 3: [1,2,3,4]"
print removeDuplicates([1,2,3,4]) == [1,2,3,4]

print "Test 4: [1,2,4,1,3,4,1]"
print removeDuplicates([1,2,4,1,3,4,1]) == [1,2,4,3]