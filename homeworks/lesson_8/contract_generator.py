from ast import literal_eval


def get_db_data(emp, emps_data):
    full_name = emps_data[emp]['full_name']
    ID = emps_data[emp]['ID']
    birthdate = emps_data[emp]['birthdate']
    salary = emps_data[emp]['salary']
    job_title = emps_data[emp]['job_title']
    position_from = emps_data[emp]['position_from']
    contract_end = emps_data[emp]['contract_end']

    return full_name, ID, birthdate, salary, job_title, position_from, contract_end


def report(id):
    print(f'Creating contract for {id} ....')


def salary_change(emps_data):
    # iterating over each person in database
    for emp in emps_data:
        # opening salary_change file as a string
        with open('templates/salary_change.txt') as s_change:
            sal = s_change.read()

        # getting data from database of employees (it is dictionary)
        full_name, ID, birthdate, salary, job_title, position_from, contract_end = get_db_data(emp, emps_data)

        # printing assigned data to salary_change string
        sal = sal.format(full_name=full_name, ID=ID, birthdate=birthdate, salary=salary)

        # printing upgraded string to .txt file, unique for each person in database
        with open(f'contracts/salary_change_{ID}.txt', 'w+') as contract:
            contract.write(sal)

        report(ID)


def job_change(emps_data):
    for emp in emps_data:
        with open('templates/job_change.txt') as j_change:
            job = j_change.read()

        full_name, ID, birthdate, salary, job_title, position_from, contract_end = get_db_data(emp, emps_data)
        job = job.format(full_name=full_name, ID=ID, birthdate=birthdate, job_title=job_title,
                         position_from=position_from)

        with open(f'contracts/job_change_{ID}.txt', 'w+') as contract:
            contract.write(job)

        report(ID)


def contact_prolong(emps_data):
    for emp in emps_data:
        with open('templates/contract_prolongation.txt') as c_prol:
            cont = c_prol.read()

        full_name, ID, birthdate, salary, job_title, position_from, contract_end = get_db_data(emp, emps_data)
        cont = cont.format(full_name=full_name, ID=ID, birthdate=birthdate, contract_end=contract_end, )

        with open(f'contracts/contract_prolongation_{ID}.txt', 'w+') as contract:
            contract.write(cont)

        report(ID)


def main():

    print('Please select the option number of action you want to perform:')
    print('''
0. salary change
1. job change
2. contract prolongation''')

    num = int(input('\nNumber: '))

    # opening database as a dictionary
    with open('employees.txt') as emps:
        emps_data = literal_eval(emps.read())

    if num == 0:
        salary_change(emps_data)
    elif num == 1:
        job_change(emps_data)
    elif num == 2:
        contact_prolong(emps_data)

    print('Contracts have been generated')


main()
