import operator as op

def my_map(func, *iterables):
    iterators = [iter(iterable) for iterable in iterables]
    result = []

    while True:
        try:
            args = []
            for iterator in iterators:
                args.append(next(iterator))
            result.append(func(*args))
        except StopIteration:
            break
    return result


# doubles = list(map(lambda n: n%2 == 0, [3,2,6,8,4,6,2,9]))
# print(doubles)
print(my_map(op.add, [1,2,3]))
# print(my_map(op.add, [1,2,3], [1,5,9,8]))