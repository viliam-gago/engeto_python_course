
def my_filter(func, iterable):
    # result = []
    # for i in iterable:
    #     if func(i):
    #         result.append(i)
    # return result

    return [i for i in iterable if func(i) is True]

print(my_filter(str.isupper, 'Hello'))





