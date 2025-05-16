#code to deduce a secret 3-digit number when given max 20 guesses
import random

num_digits = 3
max_guess = 20

def getsecrectnumer:
    numbers = list(range(0, 9))
    random.shuffle(numbers)
    num_tobeguessed = ''
    for i in range(num_digits):
        num_tobeguessed += str(numbers[i])
    return num_tobeguessed
