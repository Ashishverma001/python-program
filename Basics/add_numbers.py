ans = 0 

while True:
    num = input('enter anumber:')
    if num.isnumeric():
        ans += int(num)
    else:
        break
print('total =',ans)