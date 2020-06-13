def v_hist(seq):

    max_row = max(seq) - 1

    while max_row >= 0:
        row = []
        for number in seq:
            if max_row in range(number):
                row.append('**')
            else:
                row.append('  ')
        row = ' '.join(row)
        print('|', row)

        max_row -= 1

    print('_'*25)


v_hist([4, 5, 7, 10, 6, 3, 2])
