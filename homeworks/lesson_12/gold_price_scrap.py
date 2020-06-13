import requests, csv, bs4, os
from time import strftime


URL = 'https://markets.businessinsider.com/commodities/gold-price'

#main function ----------------------------
def gold_price(URL):
    price = get_price(URL)

    time = get_time()

    write(price, time)

#---------------------------------------------


def get_price(URL):
    get_request = requests.get(URL)
    soup = bs4.BeautifulSoup(get_request.text, 'html.parser')

    price = soup.find('span', {'class':'push-data'}).contents[0]
    price = price.replace(',', '')
    return price


def get_time():
    time = strftime("%d.%m.%Y  %H:%M")
    return time


def write(price, time):
    filename = '../../../CODING/12egeto_scraping/gold_value.csv'
    with open(filename, 'a') as file:
        file_writer = csv.writer(file, delimiter='|', lineterminator='\r')

        if os.path.getsize('../../../CODING/12egeto_scraping/gold_value.csv') == 0:
            file_writer.writerow(['Price', 'Time'])

        file_writer.writerow([price, time])

        print('Actual gold value was saved into: {}'.format(filename))



gold_price(URL)









