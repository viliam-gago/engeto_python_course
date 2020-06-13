user = input('Give me something: ')

if user.isalpha():
    print('Letters only')
elif user.isnumeric():
    print('Numbers only')
else:
    print('Mixed')