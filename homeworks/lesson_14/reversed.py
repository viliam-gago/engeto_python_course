l = [9,8,7,6,5,4,3,2,1]

def reversed(l):
    if len(l) == 1:
        return l
    return [l[-1] ]+ reversed(l[:-1])




print(reversed(l))