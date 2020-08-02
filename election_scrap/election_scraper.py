import matplotlib.pyplot as plt
import pandas as pd
import requests, csv
from bs4 import BeautifulSoup


def get_link():
    url = input('Please paste the link of desired region:  ')
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    return soup


def scrap_in_region(soup):
    tables = soup.find_all(class_='table')
    list_municip = []

    for i, table in enumerate(tables):
        i = str(int(i) + 1)
        hrefs = table.find_all('a')
        stats = [[item.string, item.get('href')] for item in hrefs if item.string.isnumeric()]
        names = table.find_all('td', {'headers': f't{i}sa1 t{i}sb2'})

        for s, n in zip(stats, names):
            s.insert(1, n.string)
        list_municip.extend(stats)

    return list_municip


def prepare_municip_page(municip):
    municip_page = requests.get('https://volby.cz/pls/ps2017nss/' + municip[2])
    municip_soup = BeautifulSoup(municip_page.text, 'html.parser')
    return municip_soup


def get_party_names(region_data):
    region_data = scrap_in_region(soup)
    first_municip = region_data[0]
    first_municip_soup = prepare_municip_page(first_municip)
    inner = first_municip_soup.find('div', id="inner")
    row_id = (1, 2)
    party_names = get_list(inner, row_id)

    return party_names


def get_votes(municip_soup):
    inner = municip_soup.find('div', id="inner")
    row_id = (2, 3)
    votes = get_list(inner, row_id)

    return votes


def get_list(inner, row_id):
    tabs = [tab for tab in inner.contents if tab != '\n']
    result_list = []

    for index, tab in enumerate(tabs):
        index = str(int(index) + 1)
        td_tags = tab.find_all('td', headers=f't{index}sa{row_id[0]} t{index}sb{row_id[1]}')
        result = [result_omacka.text.replace('\xa0', '') for result_omacka in td_tags]
        result_list.extend(result)

    return result_list


def get_total(municip_soup):
    table = municip_soup.find('table', id="ps311_t1")
    registered = table.find('td', headers="sa2").text.replace('\xa0', '')
    envelopes = table.find('td', headers="sa5").text.replace('\xa0', '')
    valid = table.find('td', headers="sa6").text.replace('\xa0', '')

    return registered, envelopes, valid


def print_head(party_names):
    head = ['CODE', 'LOCATION', 'REGISTERED', 'ENVELOPES', 'VALID', *party_names]
    with open('elections.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(head)

def plotting(res):
    # parties = res.index
    # numbers = res.votes
    # plt.tight_layout()
    # plt.bar(parties, numbers)
    # plt.xticks(parties, numbers, rotation='vertical')
    #
    #
    # plt.savefig('elections.png')

    plt.figure(figsize=(6, 6))
    plt.axes([0.2, 0.41, 0.6, 0.5])
    plt.bar(result.index, result.votes)
    plt.xticks(rotation='vertical')
    plt.ylabel('Number of votes')
    plt.title('Votes per party')
    plt.show()


if __name__ == '__main__':
    soup = get_link()
    region_data = scrap_in_region(soup)
    party_names = get_party_names(region_data)
    print_head(party_names)

    for municip in region_data:
        municip_soup = prepare_municip_page(municip)
        votes_per_party = get_votes(municip_soup)
        total = get_total(municip_soup)

        row = municip[0], municip[1], *total, *votes_per_party
        with open('elections.csv', 'a', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(row)

    data = pd.read_csv('elections.csv')
    result = pd.DataFrame(data.sum(), columns=['votes'])
    result.drop(index=['CODE', 'LOCATION', 'REGISTERED', 'ENVELOPES', 'VALID'], inplace=True)
    result = result.sort_values('votes', ascending=False)
    plotting(result)

    print(result)

