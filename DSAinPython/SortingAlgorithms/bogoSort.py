#The following code contains an implementation of the bogo sort in Python and is considered a joke algorithm
#It works by shuffling the array until it resembles a sorted array
#The sorting algorithm is known to have a time complexity of O(infinity) for worst and O(1) for best and has
#space complexity of O(1)

#Note that this sorting algorithm only works for numbers

import random as rd

def bogoSort(array):
    correctOrder = list(range(1,5))
    stepsTaken = 0
    sorted = False
    while not sorted:
        rd.shuffle(array)
        stepsTaken += 1
        if array == correctOrder:
            sorted = True
    return array, stepsTaken


if __name__ == '__main__':
    array = list(range(1,5))
    rd.shuffle(array)
    print(f'Unsorted array : {array}')

    sortedArray, stepsTaken = bogoSort(array)

    print(f'Sorted array : {sortedArray} and number of steps taken are : {stepsTaken}')
