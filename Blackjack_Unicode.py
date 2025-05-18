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
            if money=0 :
                print("You're broke!")
                sys.exit()
            bet = input("Enter your bet money : ")
            money = money - int(bet)
            print(f'Remaining money : {money}')
            deck = getDeck()
            dealerHand = [deck.pop(), deck.pop()]
            playerHand = [deck.pop(), deck.pop()]

            print(f'Bet : {bet}')
            while True:
                displayHands(dealerHand, playerHand)
                print()

                if getHandValue(playerHand) > 21:
                    break

                move  = getmove()p



