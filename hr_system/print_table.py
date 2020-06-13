from database_data import database


def table_func(id):

    data_format = get_table_data(id)

    max_width = width(data_format)

    table = make_table(data_format)

    print_table(table, max_width)


def get_table_data(id):

    employee = database.get(id)

    data = list(employee['1. Personal'].items()) + list(employee['2. Employee'].items())

    data_format = list(map(lambda x: '{}: {}'.format(*x), data))

    return data_format


def make_table(data_format):
    table = []

    while data_format:

        if len(data_format) > 1:
            table.append([data_format.pop(0), data_format.pop(0)])
        else:
            table.append([data_format.pop()])

    return table


def print_table(table, max_width):
    table_print = []

    for row in table:

        row = '|{:{w}} ||{:{w}} |'.format(*row, w=max_width) if len(row) == 2 else '|{:{w}} |'.format(*row, w=max_width)
        table_print.append(row)

    print('\n'.join(table_print))


def width(table):

    return len(max(table, key=len))
