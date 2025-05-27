# This code is an extension to the binarySearch.py program which handles duplicates in an array

import binarySearch, random

obj = binarySearch

def testLocation(array, requestedItem, mid):
    if array[mid] == requestedItem:
        if mid-1>=0 and array[mid-1] == requestedItem:
            return 'Left'
        else:
            return 'Found'
    elif array[mid] >requestedItem:
        return 'Left'
    else:
        return 'Right'

def binarySearch(array, requestedItem):
    low, high = 0 , len(array)-1
    while low <= high:
        mid = (low+high)//2
        result = testLocation(array, requestedItem, mid)
        if result == 'Found':
            return f'The element was found at index {mid}.'
        elif result == 'Left':
            high = mid - 1
        elif result == 'Right':
            low = mid + 1
    return -1

if __name__ == '__main__':
    array, requestedItem = obj.randomArray()
    print(array, requestedItem)
    print(binarySearch(array, requestedItem))



