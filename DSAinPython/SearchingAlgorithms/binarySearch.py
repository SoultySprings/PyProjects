# This is a code for the Binary Search algorithm in Python
import random as rd

def binarySearch(array, searchElement):
    low, high = 0, len(array)-1
    i=1
    print(f"Array is : {array} and required element is : {searchElement}.")
    while low <= high:
        midIndex = (low + high) // 2
        midElement = array[midIndex]
        if midElement == searchElement:
            return f"Element at index {midIndex} and the number of steps were = {i}."
        elif searchElement > midElement:
            low = midIndex + 1
            i +=1
        elif searchElement < midElement:
            high = midIndex - 1
            i += 1
    return "Element not found!"

def randomArray() :
    array, i = [], 0
    while i<9:
        array.append(rd.randint(1, 3))
        i+=1
    requestedItem = rd.choice(array)
    array.sort()
    return array, requestedItem

if __name__ == '__main__':
    array, requestedItem = randomArray()
    print(binarySearch(array, requestedItem))


