table = [['Amount1','Amount2', 'Amount3'],
         [  321,       43,       432],
         [ 3213,       42,       482],
         [  543,        38,      232]]


sumy = [sum([table[p][r] for p in range(1,4)]) for r in range(0,3)]
print(sumy)

sumy1 = [sum(row) for row in table[1:]]
print(sumy1)

sumy2 = list(map(sum,table[1:]))
print(sumy2)