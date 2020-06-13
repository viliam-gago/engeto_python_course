password = input('Type password: ').lower()
if password[0] in ['a','e','f','q','z']:
    print('Welcome!')
else:
    print('The input does not match')