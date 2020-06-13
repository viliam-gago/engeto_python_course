import random


class Deck:
    SUITS = ['♣', '♦', '♥', '♠']
    VALUES = ['ace', 'queen', 'king', 'jack'] + list(range(2, 11))

    def __init__(self):
        self.deck = self.create_deck()

    def create_deck(self):
        d = []

        for suit in self.SUITS:
            for value in self.VALUES:
                d.append(suit + str(value))

        return d

    def toss_card(self):
        card = self.deck.pop()

        return card


class Player:

    def __init__(self, name):
        self.name = name
        self.hand = None
        self.amount = initial_cash
        self.bet = 0
        self.score = 0
        self.issplit = False

    def __str__(self):
        return f'Player: {str(self.name)} | Bet: {str(self.bet)} | Cash left: {str(self.amount)} | Hand: {str(self.hand)} | Score: {str(self.score)} | '

    def put_bet(self):
        try:
            bet = int(input(f'---->{self.name}, you have {self.amount}$, how much do you want to bet?'))

            if bet > self.amount:
                print('You dont have enough money for that!')
                return None

            else:
                self.bet = bet
                self.amount -= bet

        except:
            return None

    def take_card(self, card):
        if not self.hand:
            self.hand = []

        self.hand.append(card)

    def calculate_score(self):
        self.score = 0
        total = 0

        for card in self.hand:
            value = card[1:]
            if value.isnumeric():
                total += int(value)
            elif value == 'ace':
                total += 11
            else:
                total += 10

        self.score += total

    def take_card_split(self, card, which):

        self.hand[which].append(card)

    def calculate_score_split(self):

        for i in range(2):
            total = 0

            for card in self.hand[i]:
                value = card[1:]
                if value.isnumeric():
                    total += int(value)
                elif value == 'ace':
                    total += 11
                else:
                    total += 10

            new_score = self.score
            new_score[i] = total

            self.score = new_score

    def split(self):
        self.hand = [[self.hand[0]], [self.hand[1]]]
        self.score = [[], []]


class Dealer:
    def __init__(self):
        self.name = 'DEALER'
        self.hand = None
        self.score = 0

    def __str__(self):
        return f'Dealer: | Hand: {str(self.hand)} | Score: {self.score} |'

    def take_card(self, card):
        if not self.hand:
            self.hand = []

        self.hand.append(card)

    def calculate_score(self):
        self.score = 0
        total = 0
        for card in self.hand:
            value = card[1:]
            if value.isnumeric():
                total += int(value)
            elif value == 'ace':
                total += 11
            else:
                total += 10

        self.score += total


# ----------------------------------------------------------------------

def set_game():
    players = []

    while True:

        more_players = input('---->Do you want to add player ? (y/n): ')

        if 'y' == more_players:
            name = input('Please choose name :')
            players.append(Player(name))

        elif 'n' == more_players:
            break

    return players


def put_a_bet():
    for player in players:

        while not player.bet:

            player.put_bet()


def serve_players(players):
    for player in players:

        for i in range(2):
            player.take_card(deck.toss_card())

        player.calculate_score()

    dealer.calculate_score()
    print('\nCards were given to players. Let the game begin!\n ')
    display_players(players)


def display_players(players):
    for player in players:
        print(player)

    print(dealer)

def display_player_status(player):
    print(f'{player.name} status: {player.hand} | Score: {player.score} |')

def one_hand(player):
    move = ''
    print('\n\n')

    choice = input(f'---->{player.name} do you want to DOUBLE DOWN ?')

    if player.amount < player.bet:
        print('You dont have enough money for that.')
        choice = 'n'

    if choice == 'y':

        player.amount -= player.bet
        player.bet = 2 * player.bet
        player.take_card(deck.toss_card())
        player.calculate_score()
        display_player_status(player)

        if player.score > 21:
            print('BUST!')
            player.score = 'BUST'


    elif choice == 'n':

        while move != 'n':

            display_player_status(player)
            move = input(f'---->{player.name}, do you want another card ? (y/n)')

            if move == 'y':
                player.take_card(deck.toss_card())
                player.calculate_score()

            if player.score > 21:

                for card in player.hand:
                    if card[1:] == 'ace':
                        player.score -= 10

            if player.score > 21:
                display_player_status(player)
                print('BUST!')
                player.score = 'BUST'
                break


def two_hand(player):
    player.split()

    for i in range(2):
        player.take_card_split(deck.toss_card(), i)
        player.calculate_score_split()

    for i in range(2):
        move = ''

        while move != 'n':
            print('\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
            print(f'Now you are playing with hand {i + 1}: ')
            display_player_status(player)

            move = input(f'---->{player.name}, do you want another card ? (y/n)')

            if move == 'y':
                player.take_card_split(deck.toss_card(), i)
                player.calculate_score_split()

            if player.score > 21:

                for card in player.hand:
                    if card[1:] == 'ace':
                        player.score -= 10

            if player.score[i] > 21:

                display_player_status(player)
                print('BUST!')
                new_score = player.score
                new_score[i] = 'BUST'
                player.score = new_score
                player.hand[i] = []

                break



    if player.score[0] == player.score[1] == 'BUST':
        player.score = 'BUST'

    else:
        player.score = max([value if str(value).isnumeric() else 0 for value in player.score])


def play(players, dealer):

    for player in players:

        if player.score == 21:
            print(f'{player.name} BLACK JACK!')
            continue

        if player.hand[0] == player.hand[1]:
            want_split = input(f'{player.name} - same values. Do yo want to SPLIT ? (y/n)')

            if want_split == 'y':
                player.amount -= player.bet
                player.bet = 2 * player.bet
                player.issplit = True

        if player.issplit == True:
            two_hand(player)

        else:
            one_hand(player)

    print('\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    
    print('Now lets see what does dealer have.')

    display_players(players)

    print('\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

    input('Press enter to continue:')
    dealer_turn(dealer)
    print(dealer)
    input('Press enter to continue:')

    # display_players(players)
    print('\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')


def dealer_turn(dealer):
    while dealer.score < 17:
        dealer.take_card(deck.toss_card())
        dealer.calculate_score()

        if dealer.score > 21:
            dealer.score = 0
            print('DEALER BUST !')
            break


def judge(players, dealer):
    for player in players:

        if player.score == 'BUST':
            continue

        elif player.score > dealer.score:
            player.amount += 2 * player.bet
            print(f'{player.name} has won !')



        elif player.score == dealer.score != 0:
            print(f'{player.name} - It is a push !')
            player.amount += player.bet


        else:

            print(f'{player.name} lost !')

        input('Press enter to continue:')


def play_again(players):
    next_round = []

    while players:

        if players[0].amount < min_bet:
            print('You dont have enough cash to play, goodbye.')
            players.pop(0)
            continue

        choice = input(f'---->{players[0].name}, do you want another game ? (y/n)')
        if choice == 'y':
            players[0].hand = None
            players[0].bet = 0
            players[0].score = 0
            players[0].issplit = False
            next_round.append(players[0])
            players.pop(0)

        elif choice == 'n':
            print(f'Goodbye {players[0].name}')
            players.pop(0)

        dealer.hand = None
        dealer.score = 0

    return next_round


if __name__ == '__main__':

    deck = Deck()
    random.shuffle(deck.deck)

    initial_cash = 100
    min_bet = 10

    dealer = Dealer()

    players = set_game()

    while players:

        print('\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

        put_a_bet()

        print('\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

        dealer.take_card(deck.toss_card())
        serve_players(players)

        print('\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

        play(players, dealer)
        judge(players, dealer)

        print('\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= \nSituation of the table after this round:')

        for player in players:
            print(f'Player: {player.name} | Cash left: {player.amount} |')

        print('\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        input('Press enter to continue: ')

        players = play_again(players)

        deck = Deck()
        random.shuffle(deck.deck)
