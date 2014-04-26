#Assume you have a method isSubstring which checks if one word a substring of another. 
#Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring 
#(i.e. 'waterbottle' is a rotation of 'erbottlewat').

#uhhhh... seems like isSubstring pretty much does the work. I guess you need to make sure that the number of each lettter are correct.
def isRotation(s1,s2):
	return len(s1)==len(s2) and isSubstring(s1,s2)

#needed to make this myself. Not sure if it should be taking out spaces or not...
def isSubstring(s1,s2):
	return set(s1.lower().replace(" ","")).issubset(set(s2.lower().replace(" ",""))) or set(
		s2.lower().replace(" ","")).issubset(set(s1.lower().replace(" ","")))

print "Test isSubstring 1: 'waterbottle' & 'water'"
print isSubstring('waterbottle', 'water')

print "Test isSubstring 1: 'water' & 'waterbottle'"
print isSubstring('water', 'waterbottle')

print "Test isRotation 1: 'waterbottle' 'erbottlewat'"
print isRotation('waterbottle', 'erbottlewat')

print "Test isRotation 2: '' ''"
print isRotation('', '')

#this is the one to fix....
print "Test isRotation 3: 'waterbottle' 'erbtttlewat'"
print isRotation('waterbottle', 'erbtttlewat')
