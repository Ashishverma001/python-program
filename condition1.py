
from secrets import choice


fruits = ('apple','banana','cherry')

choice = input("enter a fruit :")

if choice in fruits:
    print(f'{choice} was found in the list')
    print('very good choice btw')
    print('all the best for your life')
