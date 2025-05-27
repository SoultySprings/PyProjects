#The following code contains an implementation of the selection sort in Python
#The sorting algorithm is known to have a time complexity of O(n^2) for worst and O(n) for best and has
#space complexity of O(1)

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
    array = [2,1,3,4,5,6,7,8,9]
    rd.shuffle(array)
    print(f'The unsorted array is: {array}.')
    sortedArray, Steps = selectionSort(array)

    print(f'and the sorted is: {sortedArray} and the steps is: {Steps}.')
