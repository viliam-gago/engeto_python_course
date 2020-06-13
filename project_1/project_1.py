'''
author =
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley.''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]


# ---------------------initial phase---------------------------

# greeting and login
print('Welcome to the text analyzer app. Please log in: ')
name = input('USERNAME: ')
password = input('PASSWORD: ')


# "user registered ?" check
registered = {'bob': '123', 'ann': 'pass123', 'mike': 'password123', 'liz': 'pass123'}
if name in registered and password == registered[name]:
    print('Welcome back,', name)
elif name in registered and password != registered[name]:
    print('Wrong password!')
else:
    print('You are new user, welcome!')
print("--------------------------------------------")


# choosing text to be analyzed
print('There are three texts to be analyzed.')
text = TEXTS[int(input('Type 1, 2 or 3 to choose which one you wish to analyze: '))-1]



# ---------------text analysis----------------------


#creating list of words
text = text.replace('\n', '')
text = text.replace('.', '')
text = text.split(' ')
# print(text)


# words in total
total_count = len(text)


# initialization
word_counts = {'titlecase': 0, 'uppercase': 0, 'lowercase': 0, 'numeric': 0 }
lengths_counts = {}
numbersum = 0

while text:
    # subtracting words one by one from text variable (which is a list)
    word = text.pop()


    # word counts
    if word.istitle():
        word_counts['titlecase'] += 1
    elif word.isupper():
        word_counts['uppercase'] += 1
    elif word.islower():
        word_counts['lowercase'] += 1
    elif word.isnumeric():
        word_counts['numeric'] += 1


    # lengths counts - use of .setdefault() method for dict
    lengths_counts[len(word)] = lengths_counts.setdefault(len(word), 0) + 1

    # sum of all numbers in text
    if word.isnumeric():
        numbersum += float(word)



# --------------------output------------------------------------


# counts output
print("--------------------------------------------")
print('There is', total_count, 'words in total.')
for key in word_counts.keys():
    print('There are', word_counts[key], key, 'words.')

# lengths with bar charts output
print("--------------------------------------------")
for length in sorted(lengths_counts.keys()):
    print(length, lengths_counts[length] * '*', lengths_counts[length])

# sum of all numbers output
print("--------------------------------------------")
print('If we summed all the numbers in text, we would get:', numbersum)