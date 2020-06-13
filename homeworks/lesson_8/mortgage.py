import math


def user_input():
    L = int(input('How much do you want to borrow ?: '))
    r = float(input('At what rate?: ')) / 100 / 12
    years = int(input('How many years?: '))
    n = years * 12

    return L, r, years, n


def calc_specs(L, r, n):
    monthly_payment = math.ceil(L * (r * (1 + r) ** n) / ((1 + r) ** n - 1))
    total_amount = monthly_payment * n
    total_interest = total_amount - L

    return monthly_payment, total_amount, total_interest


def headers(L, years, total_interest, monthly_payment):
    mortgage_info = [f' Loan: {L} ', f' Years: {years} ', f' Interest: {total_interest} ',
                     f' Monthly payment: {monthly_payment} ']
    mortgage_info_string = '|' + f'{mortgage_info[0]}' + '|' + f'{mortgage_info[1]}' + '|' + f'{mortgage_info[2]}' + '|' + f'{mortgage_info[3]}' + '|'
    print(mortgage_info_string)

    separate(mortgage_info_string)

    header = ['Payment', 'Interest', 'Principal', 'Left to Pay']
    header_string = '|{:^{width_0}}|{:^{width_1}}|{:^{width_2}}|{:^{width_3}}|' \
        .format(*header, width_0=len(mortgage_info[0]), width_1=len(mortgage_info[1]), width_2=len(mortgage_info[2]),
                width_3=len(mortgage_info[3]))
    print(header_string)

    separate(mortgage_info_string)

    return mortgage_info


def separate(mortgage_info_string):
    separator = '=' * len(mortgage_info_string)
    print(separator)


def month_pay(n, r, monthly_payment, mortgage_info, total_amount):
    for month in range(n):
        mesicni_urok = math.ceil(total_amount * r)
        principal = monthly_payment - mesicni_urok
        total_amount = total_amount - monthly_payment

        table_row = [month, mesicni_urok, principal, total_amount]
        table_row_string = '|{:^{width_0}}|{:^{width_1}}|{:^{width_2}}|{:^{width_3}}|' \
            .format(*table_row, width_0=len(mortgage_info[0]), width_1=len(mortgage_info[1]),
                    width_2=len(mortgage_info[2]), width_3=len(mortgage_info[3]))
        print(table_row_string)


# -----------------main function-------------------------------------
def mortgage_calc():

    L, r, years, n = user_input()

    monthly_payment, total_amount, total_interest = calc_specs(L, r, n)

    mortgage_info = headers(L, years, total_interest, monthly_payment)

    month_pay(n, r, monthly_payment, mortgage_info, total_amount)


mortgage_calc()
