def my_min(seq):
    minimal = seq.pop()
    for item in seq:
        if item < minimal:
            minimal = item
    print('The lowest value is:', minimal)

def my_max(seq):
    maximal = seq.pop()
    for item in seq:
        if item > maximal:
            maximal = item
    print('The highest value is:', maximal)

my_min([43,45,87,21,23])
my_max([43,45,87,21,23])



