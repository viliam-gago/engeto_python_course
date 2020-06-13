length = 5
symbols = ['#', ' ']

for r in range(length):
    row = []
    for p in range(length):
        row.append(symbols[(r+p) % 2])
    print(''.join(row))

