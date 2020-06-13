import os


def filesearch(start_location, file_name):
    for dirpath, dirnames, filenames in os.walk(start_location):

        for directory in dirnames:
            if file_name in directory:
                print('DIR: ' + dirpath + '\\' + directory)

        for file in filenames:
            if file_name in file:
                print('FILE: ' + dirpath + '\\' + file)


if __name__ == '__main__':
    filesearch('C:\\Users\\viliam\\git_repa\\engeto_python_academy\\lesson_10\\DIR', 'test')
