#The following code has been taken from A CSG to DSA
#It reverses any given string using recurion

def reversalStr(string):
    if not string:
        return ''
    return reversalStr(string[1:]) + string[0]

def palindrome(str, reversedStr):
    if str == reversedStr:
        return 'Palindrome!'
    else:
        return 'not Palindrome!'

if __name__ == '__main__' :
    string = 'racecar'
    newString = reversalStr(string)
    print(f'Original string is : {string}, and reversed string is : {newString}')
    print(f'and they are {palindrome(string, newString)}')