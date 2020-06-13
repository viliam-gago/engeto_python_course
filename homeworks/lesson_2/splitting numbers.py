user = input('Give me some number: ')

if user == '':
    print('No input')
else:
    half1 = int(user[:int((len(user)) / 2)])
    half2 = int(user[int((len(user)) / 2):])
    if half1 % 2 == 0:
        print('First')
    elif half2 % 2 == 0:
        print('Second')
    elif half1 % 2 == 0 and half2 % 2 == 0:
        print('Succes')
    else:
        print('Neither')

