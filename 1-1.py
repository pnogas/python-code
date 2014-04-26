#Implement an algorithm to determine if a string has all unique
#characters. What if you can not use additional data structures?
from sets import Set

def areCharactersUnique(s):
	used = Set()
	for char in s:
		if char in used:
			return False
		else:
			used.add(char)
	return True

print "Test1: abcdef"
print areCharactersUnique("abcdef") == True

print "Test2: abcdea"
print areCharactersUnique("abcdea") == False

print "Test3: a"
print areCharactersUnique("abcdef") == True

print "Test4: ''"
print areCharactersUnique("") == True

### to do later - get a test in unicode working.
