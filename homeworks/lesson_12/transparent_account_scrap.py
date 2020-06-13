import bs4, requests, csv


# ---------------------------------------------------------------------------------
# site requestet, creating of BS object
def get_account_history(start='10.02.2020', stop='26.03.2020'):
    url = 'https://ib.fio.cz/ib/transparent?a=2800396030&f={}&t={}'.format(start, stop)
    req = requests.get(url)
    soup = bs4.BeautifulSoup(req.text, 'html.parser')

    return soup


# obtaining head of the table and rows from BS object(soup)
def set_table(soup):
    stuff_table = soup.find_all(class_='table')[1]
    head = [child.string for child in stuff_table.thead.tr.children if child != '\n']
    body = iterate_rows(stuff_table)

    return head, body


# NESTED FUNCTION; iterating over rows in table, creating body of the table
def iterate_rows(stuff_table):
    body = []
    for item in stuff_table.tbody.contents:
        if item != '\n':
            deal = [child.text.strip('CZK\n\t\t').replace('\xa0', '') for child in item.children if child != '\n']
            body.append(deal)

    return body


# write to csv file
def write_to_csv(head, body, start, stop):
    with open(f'account_movement_{start}_{stop}.csv', 'w+', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(head)
        writer.writerows(body)


# -------------------------------------------------------------------------------------
# main script
while True:
    start = input('Datum od kdy (dd.mm.yyyy): ')
    stop = input('Datum do kdy (dd.mm.yyyy): ')
    if start != '' or stop != '':
        break

soup = get_account_history(start, stop)
head, body = set_table(soup)
write_to_csv(head, body, start, stop)
