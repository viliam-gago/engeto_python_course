time = input('Please enter your time in HH : MM format: ')

time = time.split(' : ')


if int(time[0]) > 12:
    new_hour = int(time[0]) - 12
else:
    new_hour = int(time[0])

daytime = ['AM','PM'][int(time[0]) >= 12]
print('Converted to English: ', time[0], ':', int(time[1]), daytime)

