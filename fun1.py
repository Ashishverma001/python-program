from random import randint# from libary_name import function_name 


# non perametrized non-returing function

# example 1:

def hellow(): # defing the function 
    print('HALO AMIGOS')
    print('SAY HI')
    print('👏👏👏')
hellow() # calling the function 

# example 2:
def roll_dice():
    dices = ['1','2','3','4','5','6']
    print(" => ", dices [randint(0,5)])

roll_dice()

# function Returing value  

# examle 1:
def getsalary():
    val =int(input("Enter the salary = "))
    fine = 0.09 
    last = val * fine 
    return last  

x = getsalary()
print("your final salary is = ", x)

# Parametrized function 

def word_count(msg):
    word = msg.split()
    return len(word)

print(word_count("I AM IRONMAN"))
