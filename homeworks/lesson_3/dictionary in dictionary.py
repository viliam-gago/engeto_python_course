database = {'id123': {},'id124': {},'id125': {}}

first_dict = {'name': 'Thomas', 'age': 45, 'Country': 'Czechia', 'City': 'Brno'}
second_dict = {'name': 'Daniel', 'age': 34, 'Country': 'Czechia', 'City': 'Prague'}
third_dict = {'name': 'Eva', 'age': 43, 'Country': 'Czechia', 'City': 'Olomouc'}

database['id123'] = first_dict
database['id124'] = second_dict
database['id125'] = third_dict

print(database)