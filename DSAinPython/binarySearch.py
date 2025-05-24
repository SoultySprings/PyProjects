# This is a code for the Binary Search algorithm in Python
import random as rd

def binarySearch(array, requiredItem):
    low, high = 0, len(array)-1
    print(f"Array is : {array} and required element is : {requiredItem}.")
    while low <= high:
        mid = (low + high) // 2
        midNumber = array[mid]
        if midNumber == requiredItem:
            return f"Element at index {mid}."
        elif midNumber > requiredItem:
            high = mid - 1
        elif midNumber < requiredItem:
            low = mid + 1
    return "Element not found!"

if __name__ == '__main__':
    array = []
    i = 0
    while i<20:
        array.append(rd.randint(1, 500))
        i += 1
    requestedItem = rd.choice(array)
    array.sort()
    print(array, requestedItem)
    print(binarySearch(array, requestedItem))


