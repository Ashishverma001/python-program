from ctypes.wintypes import WORD
from fnmatch import fnmatchcase


a = 'Excalibur'
print(a)

b = 'smallfoot'
print(b)

c ='''once upon a time,ther was 
a person that used to sleep.
THE end'''
print(c)

print(a[0])#first char 
print(a[2])#thied char 
print(a[-1])#last char
print(a[-3])#third last char 

print(a[0],a[2],a[3])


name='vijay Deenanath chauhan'
for i,c in enumerate(name):
    print(i,c)
mame=name[6 : -8]
print(name)
fnmae = name[:5]
print(name)
lname = name[-7:]
print(mame)
print(fnmae)
print(lname)

#reverse the string 
print( name[::-1])

print(name[:5][::-1])

# every even idx char
print(name[::2])# vijy

#ever odd idx char
x = chr(65)
print(x)
x = chr(2365)
print(x)
x =chr(16368)
print(x)

# for i in range(15000,2000)
#   print(i,char)

#ordinal
y = ord('A')
print(y)
y = ('a')
print(y)
y = ('{')
print("y") 

w1 = 'this'
w2 = 'is'
w3 = 'Amazing'
msg = w1 + w2 + w3 
print(msg)

#adding space btw strings  
msg = w1 + ' ' + w2 + ' ' + w3
print(msg) 

#duplication
WORD ='hi'
print(WORD * 3)