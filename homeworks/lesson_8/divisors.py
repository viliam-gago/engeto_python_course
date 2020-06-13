def divisors_pairs_dict(start, stop):
    pairs = dict()

    for divisor in range(2, 10):
        numbers = range(start, stop + 1)

        for number in numbers:
            if number % divisor == 0:
                pairs[divisor] = pairs.setdefault(divisor, [])
                pairs[divisor].append(str(number))

        pairs[divisor] = ', '.join(pairs[divisor])

    return pairs


def table_width(pairs):
    max_width = 0

    for width in pairs.values():
        if len(width) > max_width:
            max_width = len(width)

    return max_width


def printer(max_width, pairs):
    # table header
    header = ["Divisor", "Numbers"]
    len_divisor = len(header[0])
    header_row = f'|| {header[0]:^{len_divisor}} | {header[1]:^{max_width}} ||'
    print(header_row)

    # separator
    len_separator = max_width + len_divisor + 5 + 2 + 2
    separator = '{0:=^{1}}'.format('', len_separator)
    print(separator)

    # rows in table
    for key, value in pairs.items():
        table_row = f'|| {key:^{len_divisor}} | {value:^{max_width}} ||'
        print(table_row)


# -------------------------------------------------------------------------
# main function
def divisors(start, stop):
    pairs = divisors_pairs_dict(start, stop)

    max_width = table_width(pairs)

    printer(max_width, pairs)


divisors(1, 41)
