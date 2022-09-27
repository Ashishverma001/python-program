# 1
my_string = "Hellow World"
print(my_string)

# 2 
my_string1 = input("Enter the string:")
print(my_string1)

# 3
name = "python is great"
lname = name[-5:]
print(lname)

# 4
my_string2 ="python is everthing"
print(*my_string2.split(),sep='\n')

# 5 
my_string3 = "Hellow world" 
print(my_string3[::-1])
 
# 6 
my_string4 = "who are you"
print(my_string4.upper)

# 7
my_string5 = "how it is going"
print(my_string5.lower)

# 8 
WORD =['pthhon','is','easy','to','learn']
content = " ".join(WORD)
print(content)

# 9
data = ''
while True:
    line = input()
    if not line:
        break
    data += line + '\n'
print('--->OUTPUT<---')
print(len(data),'char')

# 10
my_string6 = "to move to newline '\\n' is used "
print(my_string6)

# 11 
a = 11 
print("the variable is ",a)

# 12
s1 = 'pthon'
s2 = 'is'
s3 = 'great'
s = s1 + s2 + s3
print(s)

# 13 
a = '#'
print(a*20)

# 14 
for i in range(1,9+1):
    print(i,".") 

# 15 
my_string7 = input("Enter the sentence: ")
print(my_string7.split(),sep='\n')

# 16
my_string8 = input("Enter the sentence: ")
if my_string8[len(my_string8)-1]=='?':
    print("The entered string has'?'in the end of the string")
else:
    print("The enter sentence does not have '?'in it")

# 17 
my_string9 = input("Enter the sentence: ")
print(my_string9,count('e'))

# 18 
my_string10 = input("Enter the number: ")
print(my_string10.isnumeric())

# 19 
text = "    this is some string    "
sen = text.lstrip()
print(sen.rstrip())

# 20 
my_string11 = input("Enter the sentence: ")
for i in my_string10:
    if i.isupper():
        print("found")

# 21 
names = ' Joe, David, Mark, Tom, Chrise, Robert,'
l = []
l = names.split(',')
print(l)

#22
text = 'this is some text'
a = text.split( )
a.insert(1,'aye')
a.insert(3,'aye')
a.insert(5,'aye')
a.insert(7,'aye')
print(a)

# 23 
str = input("enter the string to check the 'Fyi' in the string")
if 'Fyi' in str:
    print("Yes,entered string have 'Fyi' in the string")
else:
    print("No,entered string does not have 'Fyi' in the string")

# 24 
#text = '%p34@y!-!t68h#&on404'

text = '%p34@y!-!t68h#&on404'
from string import punctuation
for p in punctuation:
    text = text.replace(p,'')
    print(text)

# 25 
str1 = "this is a paragraph the everage which is written just for thr purpose of providing the cotent to the everage word length be calculated"
w = str1.split()
print("number of word in the given string is ",len(w))