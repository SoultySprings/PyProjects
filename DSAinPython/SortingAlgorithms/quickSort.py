#The following code contains an implementation of the quick sort in Python
#The sorting algorithm is known to have a time complexity of O(n^2) for worst and O(nlogn) for best
#This is considered to have a better time complexity than that of Insertion, Bubble and Selection sort due to having O(nlogn) complexity at best but becomes same when considered worst cast scenario
#Note that this sorting algorithm only works for numbers

import random as rd

def partition(array, low, high, steps):
    ith_Element = low - 1
    pivot = array[high]
    for jth_Element in range(low, high):
        if array[jth_Element] <= pivot:
            ith_Element += 1
            array[ith_Element], array[jth_Element] = array[jth_Element], array[ith_Element]
            steps += 1 #Can be ignored
    array[ith_Element+1], array[high] = array[high], array[ith_Element+1]
    steps += 1 #Can be ignored
    return ith_Element+1, steps

def quickSort(array, low, high, steps):
    if low<high:
        part, steps = partition(array, low, high, steps) #steps variable can be ignored
        quickSort(array, low, part-1, steps) #steps variable can be ignored
        quickSort(array, part+1, high, steps) #steps variable can be ignored
    return array, steps

if __name__ == '__main__':
    array = list(range(1,10))
    rd.shuffle(array)
    print('Unsorted array:', array)

    sortedArray, stepsTaken = quickSort(array, 0, len(array)-1, 0)

    print(f'Sorted array: {sortedArray} and steps taken are: {stepsTaken}.')