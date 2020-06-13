def find(seq, searched):
    for index, object in enumerate(seq):
        if object == searched:
            return index
    return -1

searched_item = find([1,5,4,3,7,6,5,4,4,6,77,7,4,4,6,44,], 6)
print(searched_item)
