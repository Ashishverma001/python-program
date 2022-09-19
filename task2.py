# wap to create numerical list of 10 values, from the users and then display
# sum,mean,meadian,mode

import math
from ssl import ALERT_DESCRIPTION_HANDSHAKE_FAILURE, ALERT_DESCRIPTION_UNKNOWN_PSK_IDENTITY
from unicodedata import name

x =[1,2,3,4,5,6,7,8,9]
print("sum=>",sum(x))
print("mean=>",sum(x)/len(x))
if len(x) % 2 == 0:
    x.sort
    idx = len(x)//2
    value = x[idx] + x[idx+1]
    print("meadian=>",value/2)
else:
    value = x[len(x)//2]
    print("meadian=>",value/2)


 # wap to create a list  of 5 names from users and then display each name in reverse.
names = []
for i in range(5):
    names.append(input("name=>"))

for name in names:
    print(name[::-1])
# wap  to print fibnacci series usings the concept of list(0,1,1,2,3,5,8,11...)
fib = [0,1]
for i in range(15):
    fib.append(fib[-1] + fib[-2])
print(fib)

# wap to gentrate a new list that contains squares of each numbers from existing  list  
 #x=[2,3,4,5] => {4,8,16,25} 
x = [1,2,3,4,5,5,7,8]
x2 = []
for num in x:
    x2.append(num ** 2)
print(x)
print(x2)

#wap to generate anew list from an existing list of numbers that contains only odd numders.
x = [1,2,3,4,5,6,7,8,9]

xodd = []
for i in x:
    if i % 2 != 0: 
        xodd.append(i)

print(xodd)

#wap to generate a new list by adding 2 list elementwise.
x =[1,2,3,4,5,6]
y =[6,7,8,2,1,1,4]
z =[]

for i,j in zip(x,y):
    z.append(i+j)
print(x)
print(y)
print(z)

