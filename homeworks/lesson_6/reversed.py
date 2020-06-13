def my_reversed(seq):
    reversed_seq = []
    for i in range(len(seq)-1,-1,-1):
        # print(i)
        reversed_seq.append(seq[i])

    return reversed_seq

print(my_reversed(range(10)))

