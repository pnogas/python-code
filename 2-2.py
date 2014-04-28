#Implement an algorithm to find the nth to last element of a SINGLY linked list.

def fromNToLast(l,n):
	try:
		return l[len(l)-n]
	except:
		print "index outside of list range"	
	

print "Test 1: [],0 "
print fromNToLast([],1)

print "Test 2: [1],1"
print fromNToLast([1],1) == 1

print "Test 3: [1],0"
print fromNToLast([1],0)

print "Test 4: [1],-1"
print fromNToLast([1],-1)

print "Test 5: [1,2,3,4],2"
print fromNToLast([1,2,3,4],2) == 3

print "Test 6: [1,2,4,5,6,7,8],7"
print fromNToLast([1,2,4,5,6,7,8],7) == 1

print "Test 7: [1,2,4,5,6,7,8],0"
print fromNToLast([1,2,4,5,6,7,8],0)

print "Test 8: [1,2,4,5,6,7,8],-2"
print fromNToLast([1,2,4,5,6,7,8],-2)
