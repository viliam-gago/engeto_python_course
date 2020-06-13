# def sym(symbol: str, count: int):
#     return str(symbol)*int(count)
#
# print(sym('[]',20))

################################################################
# def letter_count(names):
#     total = 0
#
#     for name in names:
#         total += len(name)
#
#     print(total)
#
#
# names_list = ['Jacob', 'Jana', 'Petr', 'Klara']
# letter_count(names_list)
################################################################
# def divide(a, b):
#     print(a/b)
#
# divide(5,2)

################################################################
def convert_height(l):
    l = 0.25 * l
    return l

def convert_weight(m):
    m = 0.45 * m
    return m

def bmi(height,weight):
    print(convert_weight(weight) / convert_height(height) ** 2)

bmi(6.3,120)