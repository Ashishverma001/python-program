x = 10
y = 10 
z = x
c = 5
d = 10 

print(x is y) 
print(x is c)
print(x is z)
print(y is z)
print(y is x)
print(c is x)
print(c is c)
print(c is d)
print(x is d)

x = [1,2,3]
y = [1,2,3]
z = x

print(x is y)
print(x is z)
print(z is y)
