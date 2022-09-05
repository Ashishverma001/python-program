email = input("enter your email=>")

if "@"  not in email:
    print('your email does not have @')
elif len(email) < 11:
        print('length of the gmail not valid')
elif'.com' not in email and '.org'  not in  email:
    print('invail domain')
else:
    print('your email look valid')
