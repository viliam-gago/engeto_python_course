import os


def greet():
    separator()
    print('Welcome to our car rental database.')
    separator()
    print('''What would you like to do ? Please choose from options below:
     a) Show all available cars
     b) Search cars
     c) Rent a car
     d) Return a car
     e) Exit the program''')
    separator()


def inp():
    choice = input('Answer : ')
    separator()
    return choice


def separator():
    print('=' * 40)


def breakpoint():
    input('Press enter to continue:')


# creating list = complete car database
def complete_database():
    car_nums = [int(name.strip('.txt')) for name in os.listdir('files') if name.strip('.txt').isnumeric()]
    cars = []

    for car_num in car_nums:
        with open(f'files\\{car_num}.txt') as f:
            lines = f.readlines()
            specs = {}

            for line in lines:
                spec = line.strip('\n').split('=')
                if spec[0] == 'technical':
                    continue

                specs[spec[0].lstrip('   ')] = spec[1]
            cars.append({car_num: specs})

    return cars


# print all cars + specs (available & unavailable)
def show_available(all_cars):
    """
    :param all_cars: all cars in database, each obtained from belonging .txt file
    :type all_cars: list
    """
    separator()
    with open('files\\not_rented.txt') as file:
        available = [int(ID.strip('\n')) for ID in file.readlines()]
        template = '     |{:^12}|{:^12}|'
        for number in available:
            print(template.format('ID', number))
            for key, value in all_cars[number - 1][number].items():
                print(template.format(key, value))
            separator()


# print cars + specs (cars matching conditions only)
def show_filtered(cars):
    """
    :param cars: cars matching selected filters
    :type cars: list
    """
    separator()
    for number in cars:
        for id_num, specs in number.items():
            template = '     |{:^12}|{:^12}|'
            print(template.format('ID', id_num))
            for spec, value in specs.items():
                print(template.format(spec, value))
            separator()


# ===== FILTERING SECTION
# creating conditions to select matching cars when searching according to chosen specs
def conditions():
    filters = {'brand': '', 'model year': '', 'power': '', 'consumption': '', 'transmission': '', 'fuel': '',
               'category': '', 'price': ''}
    filt = True

    while filt:
        print('''What is your desired specification ? Type one of the following letters a) - h)
    Filter by:
        a) Brand [{}]
        b) Year [{}]
        c) Engine power [{}]
        d) Fuel consumption [{}]
        e) Transmission [{}]
        f) Fuel type [{}]
        g) Category [{}]
        h) Price [{}]'''.format(*filters.values()))

        print('After you set all desired filters, please type SEARCH')
        choice = input('Set the filter:  \n')

        filt = filtering(choice, filters, filt)

    return filters


# creating list of cars matching selected filters
def filtered_cars(cars, filters):
    """
    :param cars: all cars in database, each obtained from belonging .txt file
    :type cars: list
    :param filters: conditions for searching cars in database
    :type filters: dict
    """
    filtered = []
    for i, car in enumerate(cars):
        match = []

        for key, value in filters.items():

            if key == 'consumption' and car[i + 1][key] < value:
                match.append(1)

            elif key == 'power' and car[i + 1][key] > value:
                match.append(1)

            elif key == 'price':
                if '>' in value and int(value.split(' ')[1]) < int(car[i + 1][key]):
                    match.append(1)
                elif '<' in value and int(value.split(' ')[1]) > int(car[i + 1][key]):
                    match.append(1)

            elif key == 'model year':
                if '>' in value and int(value.split(' ')[1]) < int(car[i + 1][key]):
                    match.append(1)
                elif '<' in value and int(value.split(' ')[1]) > int(car[i + 1][key]):
                    match.append(1)

            elif car[i + 1][key] == value:
                match.append(1)

        # print(match)
        if all(match) and len(match) == len(filters):
            filtered.append(car)

    return filtered


def filtering(choice, filters, filt):
    """
    :param choice: input from user; deciding what filter to set
    :type choice: str
    :param filters: conditions for searching cars, based on user's choices
    :type filters: dict
    :param filt: serves for breaking the loop, when False -> searching in the database starts
    :type filt: bool
    """
    if choice == 'a':
        f_by_brand(filters)
    elif choice == 'b':
        f_by_year(filters)
    elif choice == 'c':
        f_by_power(filters)
    elif choice == 'd':
        f_by_consumpt(filters)
    elif choice == 'e':
        f_by_transmission(filters)
    elif choice == 'f':
        f_by_fuel(filters)
    elif choice == 'g':
        f_by_category(filters)
    elif choice == 'h':
        f_by_price(filters)
    elif choice == 'SEARCH':
        filt = False

    return filt


def f_by_brand(filters):
    print('''Please choose from options below and type your answer in similar format:
        Find brand XXXX (type: XXXX)''')
    choice = input('Type the answer: ')
    filters['brand'] = '{}'.format(choice)
    separator()


def f_by_power(filters):
    print('''Please choose from options below and type your answer in similar format:
    Find engines with power higher than XXX (type: XXX)''')
    choice = int(input('Type the answer: '))
    filters['power'] = '{}'.format(choice)
    separator()


def f_by_year(filters):
    print('''Please choose from options below and type your answer in similar format:
    Find cars older than XXXX (type: < XXXX)
    Find cars newer than XXXX (type: > XXXX)''')
    choice = input('Type the answer: ')
    if '<' in choice:
        filters['model year'] = '{}'.format(choice)
    elif '>' in choice:
        filters['model year'] = '{}'.format(choice)
    separator()


def f_by_consumpt(filters):
    print('''Please choose from options below and type your answer in similar format:
        Find engines with consumption below (type: XXX)''')
    choice = int(input('Type the answer: '))
    filters['consumption'] = '{}'.format(choice)
    separator()


def f_by_transmission(filters):
    print('''Please choose from options below and type your answer in similar format:
            Manual / automatic transimission ? (type: manual / automatic)''')
    choice = input('Type the answer: ')
    filters['transmission'] = '{}'.format(choice)
    separator()


def f_by_fuel(filters):
    print('''Please choose from options below and type your answer in similar format:
                Gas / diesel engine ? (type: gas / diesel)''')
    choice = input('Type the answer: ')
    filters['fuel'] = '{}'.format(choice)
    separator()


def f_by_category(filters):
    print('''Please choose from options below and type your answer in similar format:
                Luxury / SUV / sedan / hatchback car ? (type: luxury / SUV / sedan / hatchback)''')
    choice = input('Type the answer: ')
    filters['category'] = '{}'.format(choice)
    separator()


def f_by_price(filters):
    print('''Please choose from options below and type your answer in similar format:
        Find cars cheaper than XXXX (type: < XXXX)
        Find cars with price higher than XXXX (type: > XXXX)''')
    choice = input('Type the answer: ')
    if '<' in choice:
        filters['price'] = '{}'.format(choice)
    elif '>' in choice:
        filters['price'] = '{}'.format(choice)
    separator()


def pick_nonempty(dct):
    """
    :param dct: conditions for filtering in database
    :type dct: dict
    :return: dictionary excluding pairs with empty values
    """
    return dict(filter(lambda x: x[1] != '', dct.items()))
# ===== FILTERING SECTION


# renting a car
def rent():
    with open('files\\not_rented.txt') as f:
        avail_cars = [int(line.strip('\n')) for line in f.readlines()]

    while True:
        print('Which car would you like to rent ? Available IDs: ', end='')
        for car in sorted(avail_cars):
            print(car, end=' ')
        choice = input('\n Type ID: ')
        try:
            choice = int(choice)
            if choice in avail_cars:
                with open('files\\not_rented.txt', 'w') as f:
                    for line in avail_cars:
                        if line != choice:
                            f.write(str(line) + '\n')

                with open('files\\rented.txt', 'a') as f:
                    f.write(str(choice) + '\n')

                print('Thank you, enjoy your car !')
                separator()
                break
            else:
                print('Car with this ID is not available !')
                separator()
        except ValueError:
            print('Please type something.')
            separator()


# if the car is rented, you can return it
def return_car():
    with open('files\\rented.txt') as f:
        rented_cars = [int(line.strip('\n')) for line in f.readlines()]

    while True:

        if len(rented_cars) == 0:
            print('All cars are on site.')
            break

        print('Which car would you like to return ? We are missing cars with IDs: ', end='')
        for car in sorted(rented_cars):            print(car, end=' ')
        choice = input('\n Type ID: ')
        try:
            choice = int(choice)
            if choice in rented_cars:
                with open('files\\rented.txt', 'w') as f:
                    for line in rented_cars:
                        if line != choice:
                            f.write(str(line) + '\n')

                with open('files\\not_rented.txt', 'a') as f:
                    f.write(str(choice) + '\n')

                print('Thank you for using our service !')
                separator()
                break


            else:
                print('We are not missing this car!')
                separator()

        except ValueError:
            print('Please type something.')
            separator()


# =====================================================
def main():
    while True:
        # creating database
        all_cars = complete_database()

        # first contact with customer
        greet()
        choice = inp()

        # displaying available cars
        if choice == 'a':
            show_available(all_cars)
            breakpoint()

        # filtering
        elif choice == 'b':
            choices = pick_nonempty(conditions())
            filt_cars = filtered_cars(all_cars, choices)
            show_filtered(filt_cars)
            breakpoint()

        # borrow car
        elif choice == 'c':
            rent()
            breakpoint()

        # return car
        elif choice == 'd':
            return_car()
            breakpoint()

        # quit
        elif choice == 'e':
            print('Bye bye !')
            quit()

        #''clearing'' pycharm run window
        print('\n' * 80)  # clearing run window in pycharm
# =====================================================


main()
