#This code has been taken from the book A CSG to DSA
#Code checks if the second array is a subset of another using iteration comparisons
#For example, for [1,2,3] and [2,3,5,6], o/p is False, as [1,2,3] ISN'T a subset of [2,3,5,6]
#The time complexity for the algorithm is O(N*M)

import time

def isSubset(arrayOne, arrayTwo):
    hashTable = {}
    if len(arrayOne) > len(arrayTwo):
        largerArray = arrayOne
        smallerArray = arrayTwo
    else:
        largerArray = arrayTwo
        smallerArray = arrayOne

    for value in largerArray:
        hashTable[value] = True

    for value in smallerArray:
        if not hashTable.get(value):
            return False
    return True

if __name__ == '__main__':
    startTime = time.time()
    array1 = list(range(1,100000))
    array2 = list(range(2,600000))
    print(f'The arrays are as follows : {array1} and {array2}.')
    boolean = isSubset(array1,array2)
    print(f'Expected result is as follows : {boolean}.')
    print(f'Time taken is {time.time()-startTime}')