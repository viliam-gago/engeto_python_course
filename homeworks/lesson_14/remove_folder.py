import os

p = 'C:\\Users\\viliam\\git_repa\\engeto_python_academy\\Level0'

def rm_r(path):

    for file_name in os.listdir(path):
        new_path = os.path.join(path, file_name)

        if os.path.isdir(new_path):
            rm_r(new_path)
            print('Removed dir:', new_path)
        else:
            print('Removed file:', new_path)
            os.remove(new_path)

    os.rmdir(os.path.split(new_path)[0])

rm_r(p)
