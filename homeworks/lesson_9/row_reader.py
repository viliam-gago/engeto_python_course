def row_reader(path):
    try:
        with open(path) as file:
            lst = file.read()
            lst = lst.split('\n')
            print(lst)

    except FileNotFoundError:
            lst = []
            print(lst)
            print('File {} not found!'.format(path.split('/')[-1]))



row_reader('cesta/podcesta/textik.txt')



