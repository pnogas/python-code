#Write a method to replace all spaces in a string with '%20'.

def replaceSpaces(s):
	return s.replace(" ","%20")

print "Test1: 'hello'"
print replaceSpaces('hello') == 'hello'

print "Test2: 'hello there '"
print replaceSpaces('hello there ') == "hello%20there%20"

print "Test2: ' '"
print replaceSpaces(' ') == "%20"

print "Test2: ''"
print replaceSpaces('') == ""