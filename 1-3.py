#Design an algorithm and write code to remove the duplicate 
#characters in a string without using any additional buffer.
# NOTE: One or two additional variables are fine.
#An extra copy of the array is not.

def removeDuplicateCharacters (s):
	return ''.join([j for i, j in enumerate(s) if j not in s[:i]])

print "Test1: hello"
print removeDuplicateCharacters("hello") == "helo"

print "Test2: ''"
print removeDuplicateCharacters("") == ""

print "Test3: the dog is two"
print removeDuplicateCharacters('the dog is two') == 'the dogisw'
