
# defalut perameter must come after required paramrter
def total(a,b=3, c=0):
    return a + b + c 

# Named parameters must come after positional parameter
print(total(10))
print(total(a=5))

print(total(100,50))
print(total(a=100,b=50))
print(total(a=50,b=100)) # swapped and working 

print(total(10,10,10))
print(total(a=10,b=10,c=10))
print(total(a=10,c=10,b=10))
print(total(10, c=10,b=10))


# Polymorphism 

