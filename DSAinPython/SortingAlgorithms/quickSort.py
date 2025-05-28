#The following code contains an implementation of the quick sort in Python
#The sorting algorithm is known to have a time complexity of O(nlogn) for worst and O(1) for best
#This is considered to have a better time complexity than that of Insertion, Bubble and Quick sort due to having O(nlogn) complexity
#Note that this sorting algorithm only works for numbers

import random as rd

def partition(array, low, high):
    ith_Element = low - 1
    pivot = array[high]
    for jth_Element in range(low, high):
        if array[jth_Element] <= pivot:
            ith_Element += 1
            array[ith_Element], array[jth_Element] = array[jth_Element], array[ith_Element]
    array[ith_Element+1], array[high] = array[high], array[ith_Element+1]
    return ith_Element+1

def quickSort(array, low, high):
    if low<high:
        part = partition(array, low, high)
        quickSort(array, low, part-1)
        quickSort(array, part+1, high)

if __name__ == '__main__':
    array = [1,2,3,4,6,7,8,9]
    rd.shuffle(array)
    print('Unsorted array:', array)
    quickSort(array, 0, len(array)-1)
    print('Sorted array:', array)