#This code has been taken from the book A CSG to DSA
#Code checks if the second array is a subset of another using iteration comparisons
#For example, for [1,2,3] and [2,3,5,6], o/p is False, as [1,2,3] ISN'T a subset of [2,3,5,6]
#The time complexity for the algorithm is O(N*M)

import time

def checkArrays(arrayOne, arrayTwo):
    if len(arrayOne) > len(arrayTwo):
        largerArray = arrayOne
        smallerArray = arrayTwo
    else:
        largerArray = arrayTwo
        smallerArray = arrayOne

    for ithIndex in smallerArray:
        foundMatch = False
        for jthIndex in largerArray:
            if ithIndex == jthIndex :
                foundMatch = True
                break

        if not foundMatch:
            return False
    return True

if __name__ == '__main__':
    startTime = time.time()
    array1 = list(range(1,1000))
    array2 = list(range(2,600))
    print(f'The arrays are as follows : {array1} and {array2}.')
    boolean = checkArrays(array1,array2)
    print(f'Expected result is as follows : {boolean}.')
    print(f'Time taken is {time.time()-startTime}')