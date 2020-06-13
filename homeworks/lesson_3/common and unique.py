string01 = 'Bratislava'
string02 = 'Budapest'

common = set(string01) & set(string02)
unique = set(string01) - set(string02)

print('Common characters: ', common)
print('Unique characters: ', unique)