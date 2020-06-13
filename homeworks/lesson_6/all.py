def my_all(seq):
    for obj in seq:
        if not obj:
            return False
    return True

print(my_all([1,2,3,0,4,5]))