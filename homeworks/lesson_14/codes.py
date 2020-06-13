##rekurzivni fce
# def sum_rec(num):
#     if num==0:
#         return 0
#     return num + sum_rec(num-1)
#
# print(sum_rec(5))


# def factory():
#     def add_num(n):
#         return n + 5
#     return add_num
#
#
# a = factory()
# print(factory())
# print(a(2))

def secti():

    a = 2
    b = 4
    def suma(n):
        return n + a + b

    return suma

f = secti()
f_closure = f.__closure__[1].cell_contents
print(f_closure)