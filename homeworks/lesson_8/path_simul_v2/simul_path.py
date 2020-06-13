paths = {'/bin/mkdir' : None,
         'lib/init/vars/vars.sh' : None,
         '/lib/init/vars.sh' : None,
         '/home/documents/reports/report1.xls' : None,
         '/home/music/album3/song2.mp3' : None,
         '/home/music/album1/song2.mp3' : None,
         '/lib/systemd/system/sudo.service' : None
         }


def path_exists(tree: dict, path: list):

    # vezmu key (predstavuje nazev slozky) v dictu
    for key in tree:

        # kdyz se key == prvnimu prvku v path:
        if key == path[0]:
            # odstranim prvni prvek z path
            path.pop(0)

            # dostavam se do listu (obsah slozky), iteruji pres kazdy soubor/slozku (pokud je to slozka, je to zas dict)
            for item in tree[key]:

                # kdyz se novy prvni clen v path rovna key v itemu(dictu), volam rekurzivne funkci na tento dict a zacyklim se
                try:
                    if path[0] in item.keys():
                        return path_exists(item, path)

                # tohle nastane, kdyz item uz neni key v dictu, ale konecny soubor
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