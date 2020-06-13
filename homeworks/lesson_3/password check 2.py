data = {'user1': 'password1', 'Mark': '1234', 'Danny': 'qwert'}

name = input('Please enter username: ')
password = input('Please enter password: ')

if name in list(data.keys()) and password == data[name]:
    print('Permission granted')
else:
    print('Password or username wrong')

