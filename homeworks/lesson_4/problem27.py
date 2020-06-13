words = ['Python', 'is', 'a', 'widely', 'used',
         'high-level', 'programming', 'language',
         'for', 'general-purpose', 'programming,',
         'created', 'by', 'Guido', 'van', 'Rossum',
         'and', 'first', 'released', 'in', '1991.']

longest = ['', 0]

while words:
    word = words.pop()
    if len(word) > longest[1]:
        longest[0] = word
        longest[1] = len(word)


print(tuple(longest))
