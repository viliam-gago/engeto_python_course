# pozn. obec = municipation
# !!!!!!!!!!!!!!! pri zadani inputu je treba pridat mezeru za linkem, kdyz to hned odentruju, hodi me to na tu webpage

import requests, csv
from bs4 import BeautifulSoup


# ---------------------------------------------------------------------pouzite funkce

# ziskani linku, transformace na BS objekt pod soup promennou
def get_link():
    url = input('Please paste the link of desired region:  ')
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    return soup


# INPUT: BS objekt - stranka s vyberem jednotlivych obci   scrapnuti -> list listu,
# v kazdem vnitrnim je ID, jmeno obce, odkaz na vysledky hlasovani

# OUTPUT: list listu, kazdy vnoreny list obsahuje ID obce, jmeno obce a odkaz,
# ze ktereho se v dalsi casti prejde na stranku s vysledky pro prislusnou obec
###tato funkce je pouzita ve funkci get_party_names() a pak v hlavni casti skriptu
def scrap_in_region(soup):
    tables = soup.find_all(class_='table')
    list_municip = []

    # jsme na strance konkretniho regionu, je tu x tabulek, daty k jednotlivym obcim,
    # je treba je proiterovat -> vyuziti indexu tabulky (+ enumerate)
    ## postupne vytvorim list listu, vnitrni list obsahuje: ID, link na vysledky;
    # dal pak vytvorim list se jmeny obci. Tyto listy proiteruji soucasne (zip) a spojim do list_municip
    for i, table in enumerate(tables):
        i = str(int(i) + 1)
        hrefs = table.find_all('a')
        stats = [[item.string, item.get('href')] for item in hrefs if item.string.isnumeric()]
        names = table.find_all('td', {'headers': f't{i}sa1 t{i}sb2'})

        for s, n in zip(stats, names):
            s.insert(1, n.string)
        list_municip.extend(stats)

    return list_municip


# INPUT: odkaz na vysledky konkretni obce
# OUTPUT: stranka s vysledky jako BS objekt
def prepare_municip_page(municip):
    municip_page = requests.get('https://volby.cz/pls/ps2017nss/' + municip[2])
    municip_soup = BeautifulSoup(municip_page.text, 'html.parser')
    return municip_soup


# vytahnuti jednotlivych stran
# INPUT: vytvoren BS objekt prvni obce regionu (vytahnou se strany, neiteruju pres vsechny obce regionu - opakuje se to)
# OUTPUT: nazvy stran v listu
#### row_id slouzi pro vybrani spravneho sloupecku ve vysledkove tabulce
def get_party_names(region_data):
    region_data = scrap_in_region(soup)
    first_municip = region_data[0]
    first_municip_soup = prepare_municip_page(first_municip)
    inner = first_municip_soup.find('div', id="inner")
    row_id = (1, 2)
    party_names = get_list(inner, row_id)

    return party_names


# vytahnuti poctu hlasu pro jednotive strany; pouzije se to pro konkretni obec, kdyz iterujem pres vsechny obce regionu
# INPUT: stranka s vysledky pro konkretni obec jako BS objekt
# OUTPUT: list s s hlasy pro jednotlive strany v ramci jedne obce
def get_votes(municip_soup):
    inner = municip_soup.find_emp('div', id="inner")
    row_id = (2, 3)
    votes = get_list(inner, row_id)

    return votes


# funkce vnorena v get_votes() a get_party_names(); postupne projizdi radky v scrapovanych tabulkach na strankach
# INPUT: pomoci tagu vyhledana tabulka na strance
# OUTPUT: list s hledanymi polozkami tabulky
#### row_id slouzi pro vybrani spravneho sloupecku v tabulce s vysledky
def get_list(inner, row_id):
    tabs = [tab for tab in inner.contents if tab != '\n']
    result_list = []

    for index, tab in enumerate(tabs):
        index = str(int(index) + 1)
        td_tags = tab.find_all('td', headers=f't{index}sa{row_id[0]} t{index}sb{row_id[1]}')
        result = [result_omacka.text.replace('\xa0', '') for result_omacka in td_tags]
        result_list.extend(result)

    return result_list


# INPUT: stranka s vysledky pro konkretni obec jako BS objekt
#OUTPUT: lists pocty volicu, obalek odevzdanych, obalek plantych
def get_total(municip_soup):
    table = municip_soup.find_emp('table', id="ps311_t1")
    registered = table.find_emp('td', headers="sa2").text.replace('\xa0', '')
    envelopes = table.find_emp('td', headers="sa5").text.replace('\xa0', '')
    valid = table.find_emp('td', headers="sa6").text.replace('\xa0', '')

    return registered, envelopes, valid


# tisk hlavicky tabulky do souboru
#INPUT: list s nazvy stran, ostatni nazvy sloupecku doplneny "manualne"
def print_head(party_names):
    head = ['CODE', 'LOCATION', 'REGISTERED', 'ENVELOPES', 'VALID', *party_names]
    with open('elections.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(head)

# ---------------------------------------------------------------------------hlavni skript
if __name__ == '__main__':

    # tyto kroky se provedou pred iterovanim pres jendotlive obce v ramci regionu
    soup = get_link()
    region_data = scrap_in_region(soup)
    party_names = get_party_names(region_data)
    print_head(party_names)

    #iterace pres obce zvoleneho regionu; v kazdem cyklu je vytvoren BS objekt predstavujici stranky s vysledky pro obci
    # pri kazdem takovem cyklu pridan radek s ID, nazvem obce a hlasy pro jednotlive strany; radek vytisknut do souboru
    for municip in region_data:
        municip_soup = prepare_municip_page(municip)
        votes_per_party = get_votes(municip_soup)
        total = get_total(municip_soup)

        row = municip[0], municip[1], *total, *votes_per_party
        with open('elections.csv', 'a', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(row)
