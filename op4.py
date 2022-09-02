from ast import Not
from pickle import TRUE


print('LOGICAL OPERATORS')
a = 10 
b = 9
c = 11 

print(a > b and a > c)
print(a > b and a < c)
print(a > b or a > c)
print(a > b or a < c)
print(a > b or a > c)
print(a < b and a < c)
print(a < b and a > c)

print(not a >b)
print( not False)
print( not TRUE)