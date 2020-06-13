data = [['ID','Name', 'Price', 'Amount', 'Supplier'],
        ['321','Ibalgin', 40.50, 2841, 'Zentiva'],
        ['534','Paralen', 19.90, 3229, 'Zentiva'],
        ['327','Smecta', 68.00, 2709, 'Sipsen'],
        ['242','Uniclophen', 76.00, 476, 'UNIMED'],
        ['444','hovno', 46.00, 46, 'sracka']]



total_price = 0
total_amount = 0
zentiva = 0

dictionary = {}

for list in range(1,len(data)):
    dictionary[list] = {}
    for index,parameter in enumerate(data[list]):
        dictionary[list][data[0][index]] = parameter

        if index == 2:
            total_price += data[list][2]
        elif index == 3:
            total_amount += data[list][3]
        elif parameter == 'Zentiva':
            zentiva += data[list][3]







print(dictionary)



print(total_price)
print(total_amount)
print(zentiva)

