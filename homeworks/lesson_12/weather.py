import requests
import sys


def url_parts():
    key = 'fdf17ab7c9a938e63181d6d9d915d879'
    pre_identificator = sys.argv[1].replace('-','')

    if pre_identificator in ['lon', 'lat']:
        id_1 = sys.argv[2]
        pre_id = sys.argv[3]
        id_2 = sys.argv[4]
        identificator = id_1 + '&' + pre_id + '=' + id_2
    elif pre_identificator in ['q', 'id']:
        identificator = sys.argv[2]
    else:
        print('''
        You have to choose from <identificators> below:
            -q
            -id
            -lon
            -lat
            
        Query example: weather.py <identificator> <city_name> -o <option>''')
        quit()

    pre_mode = sys.argv[-2]
    mode = sys.argv[-1]

    if pre_mode != 'o' or mode not in ['weather', 'forecast']:
        print('''
        You have to choose from <options> below:
            -o weather
            -o forecast
            
        Query example: weather.py <identificator> <city_name> -o <option>''')
        quit()
    url_settings = [mode, pre_identificator, identificator, key]

    return url_settings


def set_url(url_settings):
    url_p = 'http://api.openweathermap.org/data/2.5/'
    url = url_p + '{}?{}={}&appid={}&units=metric'.format(*url_settings)

    return url


# -----------------------GET JSON
def extract_json(url):
    res = requests.get(url)
    data = res.json()

    return data


# ----------------------------------SCRAP DATA
def scrap_data(data):
    description = data['weather'][0]['description']
    clouds = str(data['clouds']['all'])
    wind = str(data['wind']['speed'])
    temp_max = str(data['main']['temp_max'])
    temp_min = str(data['main']['temp_min'])
    hum = str(data['main']['humidity'])

    return description, clouds, wind, temp_max, temp_min, hum


# --------------------------------------

# ------------------------PREPARE TABLE
def prepare_table(description, clouds, wind, temp_max, temp_min, hum):
    stats = [description, clouds + ' %', wind + ' m/s', temp_max + ' °C', temp_min + ' °C', hum + ' %']
    head = ['DESCRIPTION', 'CLOUDS', 'WIND', 'TEMP_MAX', 'TEMP_MIN', 'HUMIDITY']

    return head, stats


# -----------------------------PRINT TABLE
def print_table(head, stats):
    template = '|{:^15}|{:^10}|{:^10}|{:^10}|{:^10}|{:^10}|'
    print(template.format(*head))
    print(template.format(*stats))


if __name__ == '__main__':
    url_settings = url_parts()
    url = set_url(url_settings)
    data = extract_json(url)
    data_scraped = scrap_data(data)
    head, stats = prepare_table(*data_scraped)
    print_table(head, stats)



