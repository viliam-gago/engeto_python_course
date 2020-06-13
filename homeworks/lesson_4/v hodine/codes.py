seznam = []
add_more = True

while add_more:
    seznam.append(float(input('Zadej cenu: ')))
    cont = input('Press Enter to continue or Q to quit.')
    if cont == 'q':
        add_more = False

suma = 0
while seznam:
    suma += seznam.pop()

print('Suma je:', suma)



