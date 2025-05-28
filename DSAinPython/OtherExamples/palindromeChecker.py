#This code has been taken from the book A CSG to DSA
#Logic is if the word reads the same when written in reverse order
#The time complexity for the algorithm is 2N, but is taken as O(N)

def isPalindrome(string):
    leftIndex = 0
    rightIndex = len(string) - 1

    while leftIndex < len(string)//2:
        if(string[leftIndex] != string[rightIndex]):
            return False

        leftIndex+=1
        rightIndex-=1

    return True

if __name__ == '__main__':
    string = 'Race'
    print(f'The string is : {string}')
    boolean = isPalindrome(str.lower(string))
    if boolean == True:
        print('The string is a palindrome!')
    else:
        print('The string isn\'t a palindrome.')