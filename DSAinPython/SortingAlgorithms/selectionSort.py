#The following code contains an implementation of the selection sort in Python
#The sorting algorithm is known to have a time complexity of O(n^2) for worst and O(n) for best and has
#space complexity of O(1)
#Though both of bubble sort and selection sort have the same time complexity however selection is twice faster than bubble sort.
#Note that this sorting algorithm only works for numbers

import random as rd

def selectionSort(array):
    steps = 0
    for ith_Index in range(len(array)-1):
        lowestNumIndex = ith_Index

        for jth_Index in range(ith_Index+1, len(array)):
            if array[jth_Index] < array[lowestNumIndex]:
                steps = steps + 1
                lowestNumIndex = jth_Index

        if lowestNumIndex != ith_Index:
            array[ith_Index], array[lowestNumIndex] = array[lowestNumIndex], array[ith_Index]
    return array, steps

if __name__ == "__main__":
    array = list(range(1,10))
    rd.shuffle(array)
    print(f'Unsorted array : {array}.')

    sortedArray, stepsTaken = selectionSort(array)

    print(f'Sorted array : {sortedArray} and the steps is: {stepsTaken}.')
