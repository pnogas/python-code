#You have two numbers represented by a linked list, where each node contains a single digit. 
#The digits are stored in reverse order, such that the 1’s digit is at the head of the list. 
#Write a function that adds the two numbers and returns the sum as a linked list.
#EXAMPLE
#Input: (3 -> 1 -> 5) + (5 -> 9 -> 2)
#Output: 8 -> 0 -> 8

def addLinkedLists(list_a,list_b):
	list_sum = []
	a_current_node = 0
	if len(list_a) >= len(list_b):

