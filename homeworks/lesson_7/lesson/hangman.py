import random


# asking user for a guess
def get_choice(guesses):
    text = 'Guess a letter ({} guesses left):'.format(guesses)
    guess = input(text)
    return guess


# checking if guessed letter in chosen word
def check_choice(char, string):
    char_count = 0
    if char in string:
        char_count = string.count(char)

        if char_count > 1:
            print('Yes, there are {} letters {}.'.format(char_count, char))
        else:
            print('Yes, there is 1 letter {}.'.format(choice))
        return choice

    else:
        print('No, wrong choice.')

        return None


# replacing _ with character in hidden word
def replace(letter, hidden, string):
    for index, char in enumerate(string):
        if letter == char:
            hidden[index] = letter
    return secret


# --------------------------------------------------------------------------------------------
# initialization of guessed word
words = ['cat', 'aligator', 'abracadabra']
word = random.choice(words)
tries = round(1.5 * len(word))

# welcoming phrase, giving a task
print('I am thinking of a word. What word is it?:')
secret = ['_ '] * len(word)
print(''.join(secret))

# game main loop
while True:
    # getting letter from user
    choice = get_choice(tries)

    # checking if letter in word chosen by PC
    tip = check_choice(choice, word)

    # action based on previous check
    if not tip:
        tries -= 1
        print(''.join(secret))
    else:
        secret = replace(tip, secret, word)
        print(''.join(secret))

    # game finisher (breaking the main loop)
    if '_ ' not in secret:
        print('You won !')
        break
    elif tries < 1:
        print('You lose!')
        break
