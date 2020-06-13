import random

customers = ['Bettison, Elnora',
             'Doro, Jeffrey',
             'Idalia, Craig',
             'Conyard, Phil',
             'Skupinski, Wilbert',
             'McShee, Glenn',
             'Pate, Ashley',
             'Woodison, Annie']

products = [('DROXIA', 33.86),('WRINKLESS PLUS',23.55),
            ('Claravis', 9.85), ('Nadolol', 12.35),
            ('Quinapril', 34.89), ('Doxycycline Hyclate', 23.43),
            ('Metolazone', 43.06), ('PAXIL', 14.78)]

def generate(number):

    table = []
    table.append(['Name', 'Item', 'Amount', 'Unit_Price', 'Total_Price'])

    for row in range(1, number + 1):
        table.append([])
        #name
        table[row].append(customers[random.randint(1,len(customers)-1)])
        #product
        table[row].append(products[random.randint(1,len(products)-1)][0])
        #amount
        table[row].append(random.randint(1, 100))
        #unit price
        table[row].append(products[random.randint(1,len(products)-1)][1])
        #total price
        table[row].append(table[row][2]*table[row][3])



    return table

print(generate(4))