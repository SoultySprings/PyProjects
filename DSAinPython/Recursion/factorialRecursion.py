#The following code has been taken from A CSG to DSA
#It calculates the factorial of a number using recurion

product = 0
def factorial(number):
    if number <= 1:
        return 1
    return number * factorial(number-1)

if __name__ == '__main__':
    num = 10
    print(f'The number is {num} and the factorial is {factorial(num)}')