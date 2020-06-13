import os, time, sys

def clean_files(path, days_since_opened):

    #gives paths to files
    paths_to_files = list(map(lambda x: path + x, os.listdir(path)))
    days = days_since_opened*60*60*24

    #getting only files opened more than X days ago
    old_paths = list(filter(lambda x: (time.time() - os.path.getatime(x)) > days, paths_to_files))

    #creating Old_Stuff folder
    create_folder(path)

    #setting up new paths for files into Old_Stuff folder
    new_paths = list(map(lambda x: os.path.split(x)[0] + '\\Old_Stuff\\' + os.path.split(x)[1], old_paths))

    #move files into Old_Stuff
    move_files(old_paths, new_paths)


def create_folder(path):
    try:
        os.mkdir(path + '\\Old_Stuff')
    except:
        print('Folder already exists.')
        quit()

def move_files(old_paths, new_paths):
    for old, new in zip(old_paths, new_paths):
        os.rename(old, new)


if __name__ == '__main__':
# argumenty zadat s dvojitymi lomitky(escaping), zadat tu path bez uvozovek, pred nazvem scriptu napsat py !!!!
    path = sys.argv[1]
    days = int(sys.argv[2])

    try:
        path = sys.argv[1]
        days = int(sys.argv[2])
    except IndexError:
        print('\nUSAGE: python cleanup2.py <dir_to_clean_path> <older_than>\n')
    except ValueError:
        print('\n<older_than> has to be numeric\n')
        print('\nUSAGE: python cleanup2.py <dir_to_clean_path> <older_than>\n')
    else:
        clean_files(path, days)



