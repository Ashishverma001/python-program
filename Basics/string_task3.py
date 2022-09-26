# creat a string and print it.
from ssl import ALERT_DESCRIPTION_HANDSHAKE_FAILURE
import string


WORD = 'ASHISH'
spacing = 20

ljust = WORD.ljust(spacing,"*")
print(ljust)

# take a string input and print it's length.
str = input("Enter a string:")
Counter = 0
for s in str:
    Counter = Counter+1
print("length of the input string is:",Counter)

# print the last word of the string.
