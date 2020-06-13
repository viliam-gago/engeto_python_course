def my_reduce(func, iterable, initializer=None):
        iterator = iter(iterable)
        if initializer is None:
            value = next(iterator)
        else:
            value = initializer

        for element in iterator:
            value = func(value, element)

        return value

print(my_reduce(lambda x,y: x*y, range(1,10)))



