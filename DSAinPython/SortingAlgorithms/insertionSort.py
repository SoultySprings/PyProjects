#The following code contains an implementation of the insertion sort in Python
#The sorting algorithm is known to have a time complexity of O(n^2) for worst and O(n) for best and has

#Though both of bubble sort and selection sort have the same time complexity however insertion is twice faster than seletion and four times than bubble sort.
#Note that this sorting algorithm only works for numbers

import random as rd
def insertionSort(array):
    stepsTaken = 0
    for index in range(1,len(array)):
        temporaryValue = array[index]
        position = index - 1

        while position >= 0:
            if array[position] > temporaryValue:
                array[position+1] = array[position]
                position -= 1
                stepsTaken += 1
            else:
                break
        array[position + 1] = temporaryValue
    return array, stepsTaken

if __name__ == "__main__":
    array  = [1,2,3,4,5,6,7,8,9]
    rd.shuffle(array)
    print(f'The unsorted array is : {array}.')
    arr, steps = insertionSort(array)
    print(f'The sorted array is : {arr}, and the number of steps taken are : {steps}.')
