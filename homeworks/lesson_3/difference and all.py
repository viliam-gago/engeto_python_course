string01 = 'Bratislava'
string02 = 'Budapest'

difference = set(string01) ^ set(string02)
sjednoceni = set(string01) | set(string02)

print(difference)
print(sjednoceni)