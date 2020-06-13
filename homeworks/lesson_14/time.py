from time import time


def fac_for(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res


def fac_rec(n):
    if n == 1:
        return 1
    return n * fac_rec(n - 1)


for_start = time()
fac_for(900)
for_stop = time()
for_time = for_stop - for_start

rec_start = time()
fac_rec(900)
rec_stop = time()
rec_time = rec_stop - rec_start

print('For loop time: {}'.format(for_time))
print('Recursion time: {}'.format(rec_time))