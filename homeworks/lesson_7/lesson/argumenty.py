# def our_better_print(*args, **kwargs):
#     print(type(args))
#     print(type(kwargs))
#     for arg in args:
#         print(arg)
#     for kwarg in kwargs.values():
#         print(kwarg)
#
# our_better_print('string1', ' string2', 1, 2, key='shit', key2='doubleshit')

name = 'Bob'

def func():
    surname = 'Smith'
    name = name + " " + surname
    print(locals())
    return name

func()