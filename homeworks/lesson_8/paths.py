paths = {'/bin/mkdir': None,
         '/lib/init/vars/vars.sh': None,
         '/lib/init/vars.sh': None,
         '/home/documents/reports/report1.xls': None,
         '/home/music/album3/song2.mp3': None,
         '/home/music/album1/song2.mp3': None,
         '/lib/systemd/system/sudo.service': None
         }

# turning path into list()
def split_path(path):
    path = path.split('/')[1:]
    return path

#checking whether given path valid/invalid
def file_exist(path, cd_in, final):
    found = False
    while path:

        cd_name = path.pop(0)
        for folder in cd_in: # iterating over each folders name, looking for match with searched name; !!!! folder is dict() or str() !!!!

            if cd_name in folder and type(folder) == dict: # checking if name of the folder is in current dict() and whether folder is dict()
                cd_in = folder[cd_name] # jumping "into folder"
                break

            if folder == final and cd_name == final: # checking if analyzed file and end-file matches
                found = True
                return found

        # if script done with iterating over folder and nothing found => function terminated
        else:
            return found


# --------------------------------------------------
def main():
    with open('adresar.txt', 'r') as file:
        text = file.read()
        filesystem = eval(text)

    cd_name = '/' # folder name
    cd_in = filesystem[cd_name]  # what's inside folder (list())

    # iterating over each path in given paths dictionary
    for path in paths:

        path_key = path
        path = split_path(path) # converts path into list of folders/files [FUNCTION]
        final = path[-1] # initializing searched file (end of the path)
        answer = file_exist(path, cd_in, final) # checking if the path is correct [FUNCTION]
        paths[path_key] = answer # entering if path correct/false

    return paths


print(main())
