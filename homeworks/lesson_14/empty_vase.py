def empty_v(n):
    if n == 0:
        print('vaza je prazdna')
        return 0
    print('ve vaze je {} kvitek, odeberu 1'.format(n))
    return empty_v(n-1)

empty_v(5)

