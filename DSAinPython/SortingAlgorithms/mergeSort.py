#The following code contains an implementation of the merge sort in Python
#The sorting algorithm is known to have a time complexity of O(nlogn) overall
#This is considered to have a better time complexity than that of Insertion, Bubble and Quick sort due to having O(nlogn) complexity overall
#Note that this sorting algorithm only works for numbers

import random as rd

def mergeSort(array, length):
    stepsTaken = 0 #Can be ignored
    if length > 1:
        mid = length // 2
        arrayFirst = array[:mid]
        lengthFirst = len(arrayFirst)
        arraySecond = array[mid:]
        lengthSecond = len(arraySecond)

        mergeSort(arrayFirst, lengthFirst)
        mergeSort(arraySecond, lengthSecond)
        ithElement = jthElement = kthElement = 0
        while ithElement < lengthFirst and jthElement < lengthSecond:
            if arrayFirst[ithElement] <= arraySecond[jthElement]:
                array[kthElement] = arrayFirst[ithElement]
                ithElement += 1
                stepsTaken += 1 #Can be ignored
            else:
                array[kthElement] = arraySecond[jthElement]
                jthElement += 1
                stepsTaken += 1 #Can be ignored
            kthElement += 1
        while ithElement < lengthFirst:
            array[kthElement] = arrayFirst[ithElement]
            ithElement += 1
            kthElement += 1
            stepsTaken += 1 #Can be ignored
        while jthElement < lengthSecond:
            array[kthElement] = arraySecond[jthElement]
            jthElement += 1
            kthElement += 1
            stepsTaken += 1 #Can be ignored
    return array, stepsTaken #steps can be ignored

if __name__ == '__main__':
    array = list(range(1,10))
    rd.shuffle(array)
    print('Unsorted array : ', array)

    sortedArray, stepsTaken = mergeSort(array, len(array))

    print(f'Sorted for them : {sortedArray} and steps taken are: {stepsTaken}')

