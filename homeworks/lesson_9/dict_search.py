def dict_search(key, value, dict):


    try:
        return dict[key] == value
    except KeyError:
        print('Key not found')
        return False
    except TypeError:
        print('Neni to slovnik')
        return False


x = 1
d = {'jmeno':'Pepa', 'prijmeni': 'Novak', 'rok_narozeni': 1990, 'mesto': 'Praha', 'domaci_mazlicek': 'Chameleon'}

print(dict_search('xxx', 'stefan', x))

