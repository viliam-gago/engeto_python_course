text = '''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley.'''

searched = 'of'

for position, word in enumerate(text.split(' ')):
    word = word.strip(';,._/:')
    if word == searched:
        print('Position of the word:', position + 1 )
