paths = {'/bin/mkdir' : None,
         'lib/init/vars/vars.sh' : None,
         '/lib/init/vars.sh' : None,
         '/home/documents/reports/report1.xls' : None,
         '/home/music/album3/song2.mp3' : None,
         '/home/music/album1/song2.mp3' : None,
         '/lib/systemd/system/sudo.service' : None
         }


def path_exists(tree: dict, path: list):

    for key in tree:
        if key == path[0]:
            path.pop(0)

            for item in tree[key]:

                try:
                    if path[0] in item.keys():
                        return path_exists(item, path)
                except:
                    return True

        return False


def main():
    with open('FILESYSTEM.txt') as tree:
        tree = tree.read()
        tree = eval(tree)

    for p in paths:

        if p[0] != '/':
            print('[{}] is not absolute path!'.format(p))
            paths[p] = False
            continue

        path = p.split('/')[1:]
        path.insert(0, '/')
        paths[p] = path_exists(tree, path)

    print(paths)

main()