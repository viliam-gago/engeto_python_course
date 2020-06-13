def luhn(number):

    number = list(reversed(str(number)))
    s1 = 0
    s2 = []

    for index, digit in enumerate(number):
        if index % 2 != 0:
            s2.append(str(2*int(digit)))
        else:
            s1 += int(digit)

    s2 = sum_digits(s2)
    s2 = sum(s2)

    s = s1 + s2

    return s % 10 == 0


def sum_digits(lst):
    for i, string in enumerate(lst):
        if len(string) > 1:
            lst[i] = int(string[0]) + int(string[1])
        else:
            lst[i] = int(string)

    return lst

number = 49927398716
print(luhn(number))

