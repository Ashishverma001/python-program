email = input("enter your email=>")

if "@" in email:
    if len(email) >= 11:
        if '.com' in email or 'org' in email:
            print("your gmail look valid ")
        else:
            print('invalid domain')
    else:
        print('length of the gmail not valid')
else:
    print('your email does not have @')
