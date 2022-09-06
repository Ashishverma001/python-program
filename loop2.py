#range(100)//in loops
#range(1,10)//this will tell us loop from where the loop start end.
#range(1.16,2)//start from 1,end 16,step 2.
 
from argparse import Namespace
from dataclasses import dataclass
from tkinter.font import names
from unicodedata import name


for i in range(100):
    print(i, end =' ')

for i in range(1,10):
    print(i, end =' ')

for i in range(1,12,3):
    print(i, end =' ')

#reverse loop.
for i in range(100,0,-1):
    print(i, end =' ')


#enumerate() and zip() are two functions in loops.
#enumerate()// it will give you a counter for each value in the loop.
print('=>')
data = ['apple','banana','cherry',]
for i in enumerate(data):
    print(i)

#zip()//use to cobine two etrables.
Names = ['apple','banana','cherry']
price = [100,80,67]

for n,p in zip(Names, price):
    price(f'{n} => ${p}')
