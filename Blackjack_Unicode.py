'''Blackjack using unicode, a different approach that includes money as well
Rules are the same:
1. Hit 21 or above the dealers bet or else you lose
2. Play till you have money or else you lose
'''

import random, sys

hearts = chr(9829)
diamonds = chr(9830)
spades = chr(9824)
clubs = chr(9827)

print(f'''
Hearts      :   {hearts}    
Diamonds    :   {diamonds}
Spades      :   {spades}       
Clubs       :   {clubs}''')


def main() :
    print('''
Rules:
    Try to get as close to 21 without going over.
    Kings, Queens, and Jacks are worth 10 points.
    Aces are worth 1 or 11 points.
    Cards 2 through 10 are worth their face value.
    (H)it to take another card.
    (S)tand to stop taking cards.
    On your first play, you can (D)ouble down to increase your bet
    but must hit exactly one more time before standing.
    In case of a tie, the bet is returned to the player.
    The dealer stops hitting at 17.
    ''')

    money = input('Choose the amount of money you want to start with (min 0; max 10000): ')
    if money <= 100000 and money > 0 :
        while True:
            if money == 0 :
                print("You're broke!")
                sys.exit()
            print(f'You have choosen to start with ${money}')
            bet = getBet(money)
            deck = getDeck()
            dealerHand = [deck.pop(), deck.pop()]
            playerHand = [deck.pop(), deck.pop()]

            print(f'Bet : {bet}')
            while True:
                displayHands(dealerHand, playerHand)
                print()

                if getHandValue(playerHand) > 21:
                    break

                move  = getMove(playerHand, money-bet)

                if move == 'D' :
                    additionalBet = getBet(min(bet, (money-bet)))
                    bet += additionalBet
                    print(f'Bet increased by : {bet}')
                    print(f'Bet : {bet}')

                if move in ('H', 'D') :
                    newCard = deck.pop()
                    rank, suit = newCard
                    print(f'You drew a {rank} of {suit}')
                    playerHand.append(newCard)

                    if getHandValue(playerHand) > 21:
                        continue

                if move in ('S', 'H') :
                    break
            if getHandValue(playerHand) <= 21 :
                while getHandValue(dealerHand) < 17 :
                    print('Dealer hits...')
                    dealerHand.append(deck.pop())
                    displayHands(dealerHand, playerHand, False)

                    if getHandValue(dealerHand) > 21:
                        break
                    input('Press enter to continue...')
                    print('\n\n')

            displayHands(dealerHand, playerHand, True)

            playerValue = getHandValue(playerHand)
            dealerValue = getHandValue(dealerHand)

            if dealerValue > 21 :
                print(f'Dealer busts! You won ${bet}')
                money += bet
            elif playerValue > 21 or playerValue < dealerValue :
                print('You lost!')
            elif playerValue > dealerValue :
                print(f'You won ${bet}!')
                money += bet
            elif playerValue == dealerValue :
                print("It's a tie, the bet money has been returned to you!")

            input('Press enter to continue...')
            print('\n\n')

    else :
        print('You have entered a invalid or higher value and cannot proceed!')
        input('Press enter to continue...')
        print('\n\n')
        sys.exit()


def getBet(maxbet):
    while True:
        bet = input('How much do you want to bet? : ').upper().strip()
        if bet == 'QUIT' :
            print('Thank you for playing!')
            sys.exit()
        if not bet.isdecimal() :
            continue

        bet = int(bet)
        if 1<= bet <= maxbet :
            return bet


def getDeck() :
    deck = []
    for suit in (hearts, diamonds, spades, clubs):
        for rank in range(2, 11) :
            deck.append((str(rank), suit))
        for rank in ('J', 'Q', 'K', 'A'):
            deck.append((rank, suit))
    random.shuffle(deck)
    return deck


def displayHands(dealerHand, playerHand, showDealerHand) :
    if showDealerHand:
        print('Dealer : ', getHandValue(dealerHand))
        displayCards(dealerHand)
    else :
        print('Dealer : ???')
        displayCards([backside] + dealerHand[1:])

    print('Player : ', getHandValue(playerHand))
    displayCards(playerHand)


def getHandValue(cards) :
    value = 0
    numberOfAces = 0

    for card in cards :
        rank = card[0]
        if rank  == 'A':
            numberOfAces += 1
        elif rank in ('J', 'Q', 'K'):
            value += 10
        else:
            value += int(rank)

    value += numberOfAces
    for i in range(numberOfAces) :
        if value + 10 <= 21 :
            value += 10

    return value


def displayCards(cards) :
    rows = ['', '', '', '', '']

    for i, card in enumerate(cards) :
        rows[0] += ' ____ '
        if card == backside:
            rows[1] += '|## |'
            rows[2] += '|###|'
            rows[3] += '| ##|'
        else:
            rank, suit = card
            rows[1] += '|{}  |'.format(rank.ljust(2))
            rows[2] += '| {} |'.format(suit)
            rows[3] += '|__{}|'.format(rank.rjust(2),'_')

    for row in rows:
        print(row)


def getMove(playerHand, money) :

