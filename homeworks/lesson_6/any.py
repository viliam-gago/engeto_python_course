def my_any(seq):
    for obj in seq:
        if obj:
            return True
    return False
print(my_any([0,0,0,0,3,0,0,0,0]))