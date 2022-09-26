from helper import read

data = read('pride_n_prejudice.txt')
from string import ascii_lowercase

msg = "we will be seeing the horizon"

words = msg.split()
print(words)

words = msg.split('e')
print(words)

#replaced 
updated_msg = msg.replace('seeing','vewing ')
print(updated_msg)

updated_msg = msg.replace('e','')
print(updated_msg)

#join 
path = ['user','mypc','document','data','file.txt']

content = "/".join(path)
print(content)

#strip()
name ="   ashish  "
cleaned_name = name.strip()
print(cleaned_name)
print(len(name),len(cleaned_name))

# WAP to find frequency of all the vowels in the 'data'.

for vowel in 'aeiou':
    print(f'{vowel} => {data.lower().count(vowel)}times')
 
#WAP to remove all the punctuations from the string.
str = 'he@#11%o! & (!@wo!@r,l!d)'
from string import punctuation 
for p in punctuation:
   str= str.replace(p,'')
print(str)