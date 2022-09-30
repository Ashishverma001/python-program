# WAP to enter P R T and return amt 

from re import I


def amount():
    p = int(input("Enter Principle Amount = "))
    r = float(input("Enter the rate of intreast = "))
    t = int(input("Enter time in yrs = "))
    si = (p*r*t)/100
    amt = p + si
    return amt , si 

x,y = amount()
print("Total Payable Amount =  ",x)
print("Total Intrest = ",y)

