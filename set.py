my_set = set([1,2,3,2])
print(my_set)

my_set = {1,2,3,4,5,4,2}
print(my_set)


# MODIFYING A SET
# initialize my_set
my_set = {1,3}
print(my_set)

#add an element 
my_set = {1,2,3}
print(my_set)

#add multiple element 
my_set.update ([2,3,4])
print(my_set)

#add list and set
my_set.update([5,4],{1,4,3})
print(my_set)

# REMOVING ITEMS FROM SET

#initialize my_set
my_set = {1,2,3,4,5,6}
print(my_set)

#discard an element
my_set.discard(4)
print(my_set)

my_set.discard(5)
print(my_set)

#pops a random item 
my_set.pop()
print(my_set)

#clear my_set
my_set.clear()
print(my_set)