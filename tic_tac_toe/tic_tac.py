def introduction():
    intro_text = '''Welcome to Tic Tac Toe
GAME RULES:
Each player can place one mark (or stone) per turn on the 3x3 grid
The WINNER is who succeeds in placing three of their marks in a
* horizontal,
* vertical or
* diagonal row
Let's start the game'''

    print(intro_text)
    print('======================================')


def print_table(table):
    row_one = ' | '.join(table[0:3])
    row_two = ' | '.join(table[3:6])
    row_three = ' | '.join(table[6:9])
    separator = '---------'
    dist = 12 * ' '
    print(dist, separator,
          '\n' + dist, row_one,
          '\n' + dist, separator,
          '\n' + dist, row_two,
          '\n' + dist, separator,
          '\n' + dist, row_three,
          '\n' + dist, separator)


def switch_player(pl):
    if pl == 'o':
        pl = 'x'
    else:
        pl = 'o'
    return pl


def fill_position(choice, pl, table):
    table[choice] = pl



def choose_field(table, pl):
    hint = 'Player {} || Choose position (1-9): '.format(pl)
    already_filled = 'Dont try this... this field is already taken.'

    # loop until input is correct
    while True:
        print('======================================')
        choice = input(hint)
        print('======================================')

        if choice not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            print('NO !! I SAID NUMBER IN RANGE 1-9 !')
            continue

        choice = int(choice) - 1

        if table[choice] == ' ':
            break
        else:
            print(already_filled)

    return choice


# -------------------------------------------------------------
def row_win(table):
    if table[0] == table[1] == table[2] != ' ':
        return table[0]
    elif table[3] == table[4] == table[5] != ' ':
        return table[3]
    elif table[6] == table[7] == table[8] != ' ':
        return table[6]
    else:
        return None


def column_win(table):
    if table[0] == table[3] == table[6] != ' ':
        return table[0]
    elif table[1] == table[4] == table[7] != ' ':
        return table[1]
    elif table[2] == table[5] == table[8] != ' ':
        return table[2]
    else:
        return None


def diagonal_win(table):
    if table[0] == table[4] == table[8] != ' ' or table[2] == table[4] == table[6] != ' ':
        return table[4]
    else:
        return None


# ---------------------------------------------------------------------------------
#checking if player has 3 symbols next to each other, required to win
def decide_winner(table):
    winner = 0

    row_wins = row_win(table)
    column_wins = column_win(table)
    diagonal_wins = diagonal_win(table)

    if row_wins:
        winner = row_wins
    elif column_wins:
        winner = column_wins
    elif diagonal_wins:
        winner = diagonal_wins

    return winner

# breaking the loop variable ''end'' -> if blank field not in table or somebody have won
def end_loop(table):
    end = False
    winner = decide_winner(table)

    if winner:
        end = True
    elif ' ' not in table:
        end = True

    return winner, end


# ---------------main function-----------------------------
def main():
    introduction()
    table = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ]
    player = 'o'

    while True:

        print_table(table)

        winner, end = end_loop(table)

        if end:
            break

        choice = choose_field(table, player)

        fill_position(choice, player, table)

        player = switch_player(player)

    if winner:
        print('\nPlayer "{}" have won !'.format(winner))
    else:
        print('\nIts a draw.')


main()
