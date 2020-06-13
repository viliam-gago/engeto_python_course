import os

def content(path):
    if os.path.isabs(path):
        print('It is absolute path.')
    else:
        print('It is relative path.')

    dicts_to_search = [path]

    while dicts_to_search:
        path = dicts_to_search.pop(0)

        for item in os.listdir(path):
            inside = os.path.join(path, item)
            if os.path.isdir(inside):
                dicts_to_search.append(inside)

                print(item, os.listdir(inside))

content(os.getcwd())