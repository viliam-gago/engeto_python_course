import json

with open('data.json') as file:
    data = json.load(file)

    name = data.get('name')
    weather = data['weather'][0]['main']
    temp = data.get('main').get('temp')
    temp_max = data.get('main')['temp_max']
    temp_min = data['main']['temp_min']
    wind_sp = data['wind']['speed']

    line = ('#'*25)

    print(line,'\n{}'.format(name), '\n' + '-'*2*len(name))
    print('{}'.format(weather))
    print('Current temperature: {} C\nMinimum temperature: {} C\nMaximum temperature: {} C'.format(temp, temp_min, temp_max))
    print('Wind speed: {:>9} m/s '.format(wind_sp))
    print(line)

