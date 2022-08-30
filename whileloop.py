from functools import total_ordering
from re import I


n = input("Enter a number:")
n = int(n)
total = 0 
i = 1 
while i<=n:
    total +=i 
    i +=1 
    print(total) 
    
