x = [1,1,2,2,2,2,2,3,3,3,3,3,3,4,4,5,5,6,6,6,6,6,6,7,7,8,8,]

x_one = x.count(1)
x_two = x.count(2)
x_three = x.count(3)
x_six = x.count(6)
print('1 occurred',x_one,'times')
print('2 occurred',x_two,'times')
print('3 ocurred',x_three,'times')
print('6 occured',x_six,'times')

y = {23,44,56,67,76,88,98,73}
z =[1,3,4,5,6,1]

print('x adding y')
x.extend(y)
print(x)
print('x adding z')
x.extend(z)
print(x)
xyz = x + y + z
print(xyz)

a = ['apple','cherry','banana','dragonfruit','elaichi']
v = a.pop(3) # pop can remove value from the index
print(a)
print(v)
lv = a.pop( )# pop removes last value by defaults
print(a)
print(lv)