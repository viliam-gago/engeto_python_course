my_db = {   'Name': 'John Smith',
            'Age': 34,
            'Address': {'Street': 'Main',
                'Street #': 241,
                'City': 'Boston',
                'Country': 'Venezuela'},

            'Job': {'Job Title': 'System Admin',
                    'Level' : 3}
        }

print(list(my_db.keys()))
print(list(my_db.values()))
print(list(my_db.items()))