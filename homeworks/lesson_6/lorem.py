import random

words = {'articles':  ("the", "a", "an"), 'determiners': ("another", "this", "every", "many"), 'subjects': ("cat", "dog", "man", "woman"), 'verbs': ("sang", "ran", "jumped"), 'adverbs': ("loudly", "quietly", "well", "badly")}

# required orders of words in sentences
sentences = [('articles', 'subjects', 'verbs', 'adverbs'), ('determiners', 'subjects', 'verbs'), ('determiners', 'subjects', 'verbs', 'adverbs')]

def lorem_poetry(number):
    text = ''

    # choosing number of created rows
    for row in range(number):

        #choosing specific word order of newly created sentence (random choice)
        type = random.choice(sentences)

        #iterating over each word in word orders
        for word in type:
            text += random.choice(words[word]) + ' '
        text += '\n'

    return text

print(lorem_poetry(4))


