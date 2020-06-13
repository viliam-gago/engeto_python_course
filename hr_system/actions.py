import random
from database_data import *
from print_table import *

def create_emp(database):
    person = {}

    while True:
        try:
            subsidiary = input('Employee subsidiary (CZ, SK): ')
        except KeyboardInterrupt:
            return False, False

        if subsidiary == 'CZ' or subsidiary == 'SK':
            break

    ID = generate_id(subsidiary)

    personal_stats = ask(PERSONAL_CATEGORIES, REQUIRED_CATEGORIES, '1. Personal')
    if not personal_stats:
        return False, False

    employee_stats = ask(EMPLOYEE_CATEGORIES, REQUIRED_CATEGORIES, '2. Employee')
    if not employee_stats:
        return False, False

    person['1. Personal'] = personal_stats
    person['2. Employee'] = employee_stats

    database[ID] = person

    return database[ID], ID


def generate_id(subsidiary):
    number = random.randint(100000, 999999)
    id = subsidiary + str(number)

    return id


def ask(CATEGORIES, REQUIRED, type):
    stats = {}

    for i, item in enumerate(CATEGORIES):

        while True:

            try:
                stat = input('{}/{}: '.format(type, item))
            except KeyboardInterrupt:
                return False

            if item in REQUIRED and stat == '':
                print('This is required !')
                continue

            elif item not in REQUIRED and not stat:
                break

            else:
                stats.update({item: int(stat) if stat.isnumeric() else stat})
                break

    return stats


def find_emp(id):
    try:
        table_func(id)
        input('\nEmployee {} displayed. Press ENTER to continue'.format(id))

    except TypeError:
        input('Employee has not been found. Press ENTER to continue')
#===============================================




def remove_emp(id):
    try:
        database.pop(id)
    except KeyError:
        input('Employee has not been found. Press ENTER to continue')
    else:
        input('{} was deleted. Press ENTER to continue'.format(str(id)))