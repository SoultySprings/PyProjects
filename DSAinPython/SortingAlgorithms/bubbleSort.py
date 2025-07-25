#The following code contains an implementation of the bubble sort in Python
#The sorting algorithm is known to have a time complexity of O(n^2) for worst and O(n) for best and has
#space complexity of O(1)

#Note that this sorting algorithm only works for numbers

import random as rd

def bubbleSort(array):
    unsortedIndex = len(array) - 1
    sorted = False
    stepCount = 0 #Can be ignored
    while not sorted:
        sorted = True
        for ithElement in range(unsortedIndex):
            if array[ithElement] > array[ithElement + 1]:
                array[ithElement], array[ithElement+1] = array[ithElement+1], array[ithElement]
                stepCount += 1*2
                print(array)
                sorted = False
        unsortedIndex -= 1
    return array, stepCount

if __name__ == '__main__':
    array = list(range(1,10))
    rd.shuffle(array)
    print(f'Unsorted array : {array}')

    sortedArray, stepsTaken = bubbleSort(array)

    print(f'Sorted array : {sortedArray} and number of steps taken are : {stepsTaken}')
