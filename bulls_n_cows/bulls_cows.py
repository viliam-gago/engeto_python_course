import random
import time

#main function
def main():
    intro() # telling user what we are up to
    guesses = 0
    secret_number = random_num() #generating random number
    start = time.time()
    # print(secret_number)

    #main loop - till the right guess
    while True:
        player_guess = guess() #getting input from user
        bulls, cows = check_bulls_cows(player_guess, secret_number) #checking if guess right

        print('||| Bulls:', bulls, 'Cows:', cows,'|||')

        guesses += 1

        if bulls == 4: # breaking the main loop - you won
            break

    end = time.time()
    time_elapsed = round(end - start) # time to get it right
    print('-'*20)
    print('\nCongratulations, you guessed the right number in {} guesses !'.format(guesses))
    print('It took you cca',time_elapsed,'seconds.\n')

    write_stats(guesses, time_elapsed) # writing into txt file
    read_stats() #reading stats from txt



def intro(): # telling user what we are up to
    text = '''Hi there!
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.\n'''

    print(text)


def random_num(): #generating random number
    number = ''
    while len(number) < 4:
        digit = str(random.randint(1, 9))
        if digit in number:
            continue
        number += digit

    # print(number)
    return number


def guess(): # getting input
    number = input('Guess my number: ')
    return number


def check_bulls_cows(guess, secret): #checking guess
    bulls = 0
    cows = 0

    for index_s, digit_s in enumerate(secret):
        for index_d, digit_d in enumerate(guess):
            if digit_d == digit_s and index_d == index_s:
                bulls += 1
            elif digit_d == digit_s and index_d != index_s:
                cows += 1

    return bulls, cows


def write_stats(guesses, time_elapsed): # writing stats into .txt
    with open('stats.txt', 'a') as stats:
        stats.write(str(guesses))
        stats.write('|')
        stats.write(str(time_elapsed))
        stats.write('\n')


def read_stats():   # reading stats, formating them (display result for each game if wanted)
    count_guesses = 0
    count_time = 0

    with open('stats.txt') as stats:
        vysledky  = stats.readlines()
        for index,line in enumerate(vysledky):
            line = line.strip('\n')
            line = line.split('|')
            count_guesses += int(line[0])
            count_time += int(line[1])

            # print('Game n.{}: {} guess(es), guessed in {} seconds.'.format(index, line[0], line[1]))

    g, t = average(count_guesses, count_time, vysledky)
    print('Average number of guesses:',str(g), '| Average number of time needed:', str(t), 'seconds')


def average(count_guesses, count_time, vysledky): # average results to compare your skill
    average_guesses = round(count_guesses / len(vysledky), 2)
    average_time = round(count_time / len(vysledky), 2)

    return average_guesses, average_time


main()
