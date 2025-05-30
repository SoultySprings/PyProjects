#The following code has been taken from A CSG to DSA
#Creates anagrams of a particular string using recursion as backtracking

def anagramsOf(string):
    if len(string) == 1:
        return [string[0]]
    collection = []
    substringAnagrams = anagramsOf(string[1:])
    for substringAnagram in substringAnagrams:
        for index in range(len(substringAnagram) + 1):
            newString = (substringAnagram[1:index] + string[0] + substringAnagram[index:])
            collection.append(newString)

    return collection

if __name__ == '__main__':
    string = 'bc'
    print(f'The string is {string}')
    anagrams = anagramsOf(string)
    print(f'The anagrams of the string are {anagrams}')
