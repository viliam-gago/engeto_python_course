import math
d_r = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
d_a = {value: key for key, value in d_r.items()}


def to_arab(roman):
    arab = 0
    for index in range(0, len(roman) - 1):
        if d_r[roman[index + 1]] > d_r[roman[index]]:
            arab -= d_r[roman[index]]
        else:
            arab += d_r[roman[index]]

    arab += d_r[roman[-1]]

    print(arab)



def to_roman(arab):
    div = 1

    while arab >= div:
        div *= 10

    div = int(div / 10)
    res = " "

    while arab:
        koef = int(arab/div)

        if koef <= 3:
            res += (d_a[div]*koef)
        elif koef == 4:
            res += (d_a[div] + d_a[div * 5])
        elif 5 <= koef <= 8:
            res += (d_a[div * 5] + (d_a[div] * (koef - 5)))
        elif koef == 9:
            res += (d_a[div] + d_a[div * 10])

        arab = arab % div
        div /= 10


    print(res)
    return res

# to_arab('XIV')

to_roman(3974)
