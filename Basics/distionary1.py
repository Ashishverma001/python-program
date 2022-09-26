# dictionary with integer keys 
my_dict = {1: 'apple', 2: 'ball'}

print(my_dict)

val = ['Rajendra singh', 30,10, 'account','Staff officer', 600000,7,]

val_dict = {
    'employee':'Rajendra singh','age': 30,
    'experience': 10 ,'dept':'Accounts',
    'designation':'system officer','salary': 50000,
    'team_size': 6
      
}

# displaying a dict
print(val_dict)

# retreval of value 
ans = val_dict['designation'] # key in sqr brackets
print(ans)
print(val_dict['salary']) # correct
print(val_dict['experience']) # incorrect 

# adding a data inside dict 
val_dict['employee'] = 'Acme.inc'

print(val_dict)

from pprint import pp 

pp(val_dict) # use to give output in a good and clean way.