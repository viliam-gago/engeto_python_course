week = ['Monday','Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
choice = input('Please enter the number of the day: ')

if choice not in ['1', '2', '3', '4', '5', '6', '7']:
    print('Enter only numbers between 1 and 7')
elif choice == '':
    print('No input provided')
else:
    print(week[int(choice)-1])