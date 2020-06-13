import os

path = 'C:\\Users\\viliam\\git_repa\\engeto_python_academy\\Level0'
nrecursions = 0


def tree(path):
    global nrecursions

    for file_name in os.listdir(path):
        n_path = os.path.join(path, file_name)

        level = nrecursions + 1
        span = ' ' * level + '|___'

        if os.path.isdir(n_path):
            print(span, file_name)
            nrecursions += 4
            tree(n_path)
        else:
            print(span, file_name)

    nrecursions -= 4


tree(path)
