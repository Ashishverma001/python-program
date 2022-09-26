movies = ['DDLJ','batman','captain america','thor','iron man','kung-fu-panda','dr.starange'
         ,'wonder women','hulk','incaption']

print(len(movies))
print(movies)

movies.sort()
print(movies)

print('first movie:',movies[0])
print('last movie:',movies[-1])
print('first 3 movies:',movies[:3])
print('all movies except first 3:',movies[3:])
print('movies with name indexes:',movies[::2])