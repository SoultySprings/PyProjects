import random

def main():
    print("The game of Blackjack remade:")
    print('''The rules are simply that:
    1. You deal a number
    2. The dealer then deals a number
    3. Based on that and the number that you have, you have 2 choices
    4. You either Hit, to get a larger number but below 21, or
    5. You either Stay, to have the same number and let the Dealer Hit
    6. If the number goes above 21 for you, you lose
    7. If after staying, the dealer deals a higher number you lose,
    8. If after hitting or staying, ur number is higher than then the dealer but below 21, you win!
    
    Shall we start the game?''')
    game()

def game():
    dealer_number = random.randint(1, 21)
    user_number = random.randint(1, 21)
    print(f"The dealer has dealt : {dealer_number}, your number is : {user_number}.")
    response = input("Do you want to hit or stay? H for Hit or S for Stay.")
    if response == "H":
        user_number = user_number + random.randint(1, 11)
        if user_number > 21:
            print(f"The dealer has dealt : {dealer_number}, your number is : {user_number}.")
            print("You have dealt a higher number, hence lose")
        elif user_number > dealer_number and user_number <= 21:
            print(f"The dealer has dealt : {dealer_number}, your number is : {user_number}.")
            print("You have dealt a higher number than the dealer but below 21, hence you win")
    elif response == "S":
        while dealer_number<17:
            dealer_number = dealer_number + random.randint(1, 11)
        if dealer_number > 21:
            print(f"The dealer has dealt : {dealer_number}, your number is : {user_number}.")
            print("The dealer has dealt a higher number than 21, hence you win")
        elif dealer_number > user_number and dealer_number <= 21:
            print(f"The dealer has dealt : {dealer_number}, your number is : {user_number}.")
            print("The dealer has dealt a higher number than you, hence you lose")
        elif dealer_number < user_number:
            print(f"The dealer has dealt : {dealer_number}, your number is : {user_number}.")
            print("The dealer has dealt a higher number than you, hence you win")
    print("Thanks for playing!")

main()