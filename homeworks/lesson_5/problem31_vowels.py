string = 'A speech sound that is produced by comparatively open configuration of the vocal tract.'
string = string.split(' ')
counts = {'con': 0, 'vow': 0}


for word in string:
    for letter in word.strip(',.-').lower():
        if letter in 'aeiouy':
            counts['vow'] += 1
        else:
            counts['con'] += 1
            
print(counts)
