my_new_dict = {'m': 12345, 'n': 32145, 'o': 54321, 'p': 23232, 'q': 43210, 'r': 1357}

maximal_value_of_key = max(my_new_dict)



if max(my_new_dict.values()) > my_new_dict[maximal_value_of_key]:
    my_new_dict.pop(maximal_value_of_key)

print(my_new_dict)
