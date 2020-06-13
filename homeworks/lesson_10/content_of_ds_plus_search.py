import os
import shutil



def content(path, searched):
    if os.path.isabs(path):
        print('It is absolute path.')
    else:
        print('It is relative path.')
    print()

    folders_to_search = [path]
    files_found = []

    while folders_to_search:
        path = folders_to_search.pop(0)

        for item in os.listdir(path):
            item_path = os.path.join(path, item)

            if os.path.isdir(item_path):
                folders_to_search.append(item_path)

            if searched in item_path:
                files_found.append(item_path)
                if os.path.isfile(item_path):
                    continue

            # print(item_path)
    backup(files_found)
    return files_found


def backup(files_found):
    backup_path = os.getcwd() + '\\' + 'BACKUP'
    if os.path.exists(backup_path):
        shutil.rmtree(backup_path)
        os.mkdir(backup_path)
    else:
        os.mkdir(backup_path)

    for item in files_found:
        if os.path.isfile(item):
            shutil.copy(item, backup_path)
            continue
        elif os.path.isdir(item):
            shutil.copytree(item, backup_path)
            continue


print(content(os.getcwd(),'read'))

