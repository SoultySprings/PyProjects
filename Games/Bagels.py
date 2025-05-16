#code to deduce a secret 3-digit number when given max 20 guesses
import numbers
import random

def main():
    num_digits = 3
    max_guess = 20
    print('''The following game allows the user to deduce a three digit random integer.
    the rules simply says that:
    1. if a digit is in the right place - Fermi
    2. if digit in the wrong place but exists in number - Gamma
    3. if digit not in number - Bagels
    ''')
    guessing_number = getsecrectnumber(num_digits)

    while True:
        print(f'You have {max_guess} guesses in total.)')
        print('''The number has been imagined.''')
        guesscount = 1
        while guesscount <= max_guess :
            user_num = str(input('Enter your guess: '))
            clues(user_num, guessing_number, num_digits)
        if user_num == guessing_number:
            break
        elif guesscount > max_guess:
            print('You have ran out of guesses!')
            break
        guesscount += 1

def getsecrectnumber(num_digits):
    numbers = list(range(0, 9))
    random.shuffle(numbers)
    num_tobeguessed = ''
    for i in range(num_digits):
        num_tobeguessed += str(numbers[i])
    return num_tobeguessed

def clues(user_num, guessing_number,num_digits):
    if user_num == guessing_number:
        print('You have guessed the correct number!')
    for i in range(0, num_digits):
        if user_num[i] == guessing_number[i]:
            print('Fermi')
        elif user_num[i] in guessing_number:
            print('Gamma')
        elif user_num[i] != guessing_number:
            print('Bagels')

