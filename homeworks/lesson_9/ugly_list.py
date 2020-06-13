def counting(lst):
    total = 0
    for item in lst:
        try:
            total += float(item)
        except:
            continue

    return total

print(counting([1, 'asda', {'zvire':'kocka'}, '3.0', 2.0, [], '\n', '4']))

