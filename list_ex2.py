from statistics import mean, median, mode
from xml.dom.minidom import Element


books =['start with why','steelheart','don quixote','beloved'
        ,'the great gatsby']

books.append('start with why')
books.append('steelheart')
books.append('don quixote')
books.append('beloved')
books.append('the great gatsby')

print('idx\t| book')
for i,b in enumerate(books):
    print(f'{i}\t| {b}')

books[5] ='The Well of Ascession' #update
books[4] ='The Hero of Age'
books[3] ='You Can Win'

print('idx\t| book')
for i,b in enumerate(books):
    print(f'{i}\t| {b}')

books.insert(3,'legions:Skin deep')
books.insert(5,'Elantris')

print('idx\t| book')
for i,b in enumerate(books):
    print(f'{i}\t| {b}')

books.remove('steelheart')
books.remove('Elantris')

print('idx\t| book')
for i,b in enumerate(books):
    print(f'{i}\t| {b}')


