import os


def tree(path, level=0):
    for i in os.listdir(path):
        print(' ' * level * 4 + '|' + '_' * 3 + i)

        p = os.path.join(path, i)

        if os.path.isdir(p):
            tree(p, level + 1)

tree('C:\\Users\\viliam\\CODING\\flask_udemy')