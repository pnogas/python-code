#Describe how you could use a single array to implement three stacks.

2 stacks would be easiest and most efficent. have one start at the front of the array and push items towards the end.
have the other stack start at the end of the array and push items towards the start and simply have a collision detection mechanism

As for 3 stacks:
have the first 3 entries in the array be the indicies of each stack. 
Since no other information is given, assume that all stacks are of equal maximum length and that dynamic size adjustment is not used for simplicity
so if we had an array of length 18 we could have 3 stacks of maximum length (height?) 5. again you would just have to check the index to see if a push / pop makes it go out of bounds
example. stack 1 = 1,2 <- top
stack 2 = a,b,c,d,e <- top (assuming array can mix types / an array of generic objects)
stack 3 = 5,5,5,5 <- top
[4,12,16,1,2,null,null,null, a,b,c,d,e, 5,5,5,5,null]