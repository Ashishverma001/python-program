from telnetlib import PRAGMA_HEARTBEAT


A = {1,2,3,4,5}
B = {4,5,6,7,8}

# use | operator
print(A | B)

# use union function
A.union(B)
{1,2,3,4,5,6,7,8,9}
print(A)

# use union function on B 
B.union(A)
{1,2,3,4,5,6,7,8,9}
print(B)

# SET INTERSECTION 

A = {1,2,3,4,5,6}
B = {4,5,6,7,8,9}

# use & operator 
print(A & B)

A.intersection(B)
print(A)

# SET DEFFERRENCE

A = {1,2,3,4,5,6}
B = {4,5,6,7,8,9}

# use - operator om A 
print(A - B)

A.difference(B)
print(A)
#{1,2,3}

#use - operator on B 
B - A
print(B - A)
#{8,6,7}

# SET SYMMETRIC DIFFERENCE

# use ^ operator
print(A ^ B)

# use symmatric_difference function on A 
A.symmetric_difference(B)
print(A)

