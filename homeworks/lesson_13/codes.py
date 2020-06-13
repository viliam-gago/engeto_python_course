# l1 = [1,2,3,4,5,6]
# iterator = iter(l1)
#
# while True:
#     try:
#         print(next(iterator))
#
#     except StopIteration:
#         break

# l1 = []
# #
# # for i in range(30):
# #     l1.append(i)
# #
# # print(l1)
##### ========================================

# l1 = [i for i in range(30)]
# print(l1)
###########==================================
# names = ['bob', 'john', 'frank']
# upper_names = [ name.upper() for name in names]
# print(upper_names)

######=================================

# people = (('John',23),('Bob',43),('Fred',54))
#
# people_dict = {name: age for name, age in people}
# print(people_dict)

###================================

# even = [i for i in range(101) if i % 2 == 0]
# print(even)
#
# l1 = [i for i in even if i >= 50 if i % 4 == 0]
# print(l1)
#
# l2 = [i for i in even if i >= 50 and i % 4 == 0]
#
# print(l2)

#=======================================

# my_list = [(x,y) for x in 'abc' for y in 'def']
# print(my_list)

nums = [(x,y) for x in 'abc' for y in 'def']
print(nums)