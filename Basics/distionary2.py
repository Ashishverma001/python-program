from pprint import pprint
from unicodedata import name

movies ={}
movies['Top Gun: maverick'] = 8.3
movies['Everything Everywhere All at onnce'] = 8.1
movies['Spider-man:no way home'] = 8.2

pprint(movies)

for item in movies:
    print(item)

print('only values')
for item in movies: 
    print(movies[item])

print('both key and values')
for key in movies:
    print(key, movies[key])

print('using dict.items() method')
for k,v in movies.items():
    print(k,v)


# user input
for i in range(3):
    name = input("Movie Name :")
    rating = float(input('Movie Rating : '))
    movies[name] = rating

print('using dict.items() method')
for k,v in movies.items():
    print(k,v)
