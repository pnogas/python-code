#Write a method to decide if two strings are anagrams or not.

def areStringsAnagrams(s1,s2):
	return set(s1.lower().replace(" ","")) == set(s2.lower().replace(" ",""))

print "Test1: 'hello' & 'olhel'"
print areStringsAnagrams('hello','olhel') == True

#not specified if Caps or Spaces matter but I assume they do not.
print "Test2: 'Doctor Who' & 'Torchwood'"
print areStringsAnagrams('Doctor Who', 'Torchwood') == True

print "Test3: 'Doctor Who' & 'Torchweod'"
print areStringsAnagrams('Doctor Who', 'Torchweod') == False