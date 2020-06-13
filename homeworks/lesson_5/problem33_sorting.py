names = ['Michal', 'Pepa', 'Honza',
        'Pavel', 'Lukas', 'Matej',
        'Iva', 'Klara', 'Jana',
        'Honza', 'Vasek','Milan', 'Michal'
        ]

sorted_list = []
sorted_list.append(names.pop())
print(sorted_list)

for name in names:
    for index, sorted_name in enumerate(sorted_list):
        if name < sorted_name:
            sorted_list.insert(index, name)
            break
    else:
        sorted_list.append(name)

print(sorted_list)
