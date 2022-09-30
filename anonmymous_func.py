num = [ 1,2,3,4,5,6,7,8,9,3,4,5,6,4,2,5,7,8,6,5,3]
names = ['jhon','jack','rob','thakur','ashish']

num_sqr = list(map(lambda i: i ** 2,num))
print(num_sqr)

num_eq1 = list(map(lambda i: i+4 * i**2,num))
print(num_eq1)

num_names = tuple(map(lambda nm: nm.split()[0], names))
print(num_names)

last_names = tuple(map(lambda mn: mn.split()[-1], names))
print(last_names)