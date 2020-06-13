### MAIN FILE

from actions import *
import os
import sys
import back_up as b


def homepage():

    choices = {'1': 'Create New Employee (1)', '2': 'Find Employee (2)', '3': 'Remove Employee (3)', 'q': 'q'}
    print_menu(choices)

    try:
        choice = str(input('PLEASE SELECT YOUR ACTION (or "q" to quit): '))
    except KeyboardInterrupt:
        return False

    if choice not in choices.keys():
        print('I AM SORRY, BUT THERE IS NO SUCH OPTION')
        homepage()

    elif choice == 'q':
        quit()

    return choice


def print_menu(choices):

    separator = '=' * 69
    template = '\n' + separator + '\n| {} | {} | {} |\n'.format(*choices.values()) + separator
    print(template)
# ============================================================


def main(database):

    args = sys.argv
    b.backup(args)

    while True:

        os.system('cls')
        choice = homepage()

        if choice == False:
            continue

        if choice == '1':
            os.system('cls')
            person, ID = create_emp(database)

            if person == False:
                continue

            os.system('cls')
            table_func(ID)
            input('\nEntry has been completed for {}. Press ENTER to continue:'.format(ID))

        elif choice == '2':
            os.system('cls')

            try:
                ID = input('Enter ID of searcher employee: ')
                find_emp(ID)

            except KeyboardInterrupt:
                continue

        elif choice == '3':
            os.system('cls')

            try:
                ID = input("Enter employee's ID to be removed: ")
                remove_emp(ID)

            except KeyboardInterrupt:
                continue

        update_database(filename)


main(database)