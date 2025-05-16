#code to deduce a secret 3-digit number when given max 20 guesses
import random

num_digits = 3
max_guess = 20

def main():
    print('''The following game allows the user to deduce a three digit random integer.
    the rules simply says that:
    1. if a digit is in the right place - Fermi
    2. if digit in the wrong place but exists in number - Gamma
    3. if digit not in number - Bagels
    ''')
    guessing_number = getsecrectnumber()

    while True:
        print(f'You have {max_guess} guesses in total.)')
        print('''The number has been guessed''')
        guess = 1
        while guess <= max_guess :


def getsecrectnumber():
    numbers = list(range(0, 9))
    random.shuffle(numbers)
    num_tobeguessed = ''
    for i in range(num_digits):
        num_tobeguessed += str(numbers[i])
    return num_tobeguessed

def clues():

