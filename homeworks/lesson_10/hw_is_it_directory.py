import os

def which(path):
    if os.path.isdir(path):
        return 'dir'
    elif os.path.isfile(path):
        return 'file'
    else:
        return 'PathNotValid'
