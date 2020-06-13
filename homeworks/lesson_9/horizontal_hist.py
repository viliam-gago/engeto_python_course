def h_hist(seq: list):
    try:
        for index, number in enumerate(seq):
            print('|' + number * '*')
    except TypeError:
        print('!Nekompatibilni prvek v listu!')


h_hist([1,2,3,8,3,12,5,4,3,2,1])
