#Write code to reverse a C-Style String.
#(C-String means that abcd is represented as five characters
# including the null character.)

def reverseCStyleString(s):
	reversed_string = ""
	for char in s:
		reversed_string = char + reversed_string
	return reversed_string

print "Test1: hello"
print reverseCStyleString("hello") == "olleh"

print "Test2: ob"
print reverseCStyleString("ob") == "bo"

print "Test3: ''"
print reverseCStyleString('') == ''

## To do later, utf-8?