import json

PERSONAL_STR = '''First Name, Middle Name Initial, Last Name, Street Address,
City,State,Country of Residence, ZipCode, Personal Email, Telephone Number, Username,
Password,Date of Birth, Age, Citizenship, National ID'''

EMPLOYEE_STR = '''Employment Status (active/leave/inactive),
Manager,Department, Job Title, Band, Contract Beginning, Contract Type, Contract End (3.3.3333 for indefinite),
Is Manager, FTE (value between 0.0 and 1.0), Full-Time Salary'''

REQUIRED_STR = '''First Name, Last Name, Contract Beginning, Contract End, FTE, Contract Type, Manager, Department,
Job Title, Band, Full-Time Salary'''


def load_database(path):
    try:
        with open(path) as file:
            # data = file.read()
            # database = eval(data)
            database = json.load(file)
    except:
        print('File does not exist')

    else:
        return database


PERSONAL_CATEGORIES = [cat.lstrip(' \n') for cat in PERSONAL_STR.split(',')]
EMPLOYEE_CATEGORIES = [cat.lstrip(' \n') for cat in EMPLOYEE_STR.split(',')]
REQUIRED_CATEGORIES = [cat.lstrip(' \n') for cat in REQUIRED_STR.split(',')]

# filename = 'employee.txt'
filename = 'employee.json'

database = load_database(filename)


def update_database(path):

    with open(path, 'w') as file:
        # file.write(str(database))
        json.dump(database, file)