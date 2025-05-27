#This code has been taken from Ch3Ex of the Book - A Common-Sense Guide to Data Structures and Algorithms in Python
#But it has the addition of elements used for the product as well as what their index is w.r.t. the array.
import random as rd

def greatestProduct(array):
    if len(array) < 2:
        return 'None'
    greatestProductSoFar = array[0] * array[1]
    for ithIndex, ithValue in enumerate(array):
        for jthIndex, jthValue in enumerate(array):
            if (ithIndex != jthIndex and ithValue*jthValue>greatestProductSoFar):
                greatestProductSoFar = ithValue*jthValue
                high1 = ithValue
                high2 = jthValue
                high1Index = ithIndex
                high2Index = jthIndex
    return greatestProductSoFar, high1, high2, high1Index, high2Index

if __name__ == '__main__':
    array = [1,2,3,4,5,6,7,8,9]
    rd.shuffle(array)
    result, highestNumber1, highestNumber2, hIndex1, hIndex2= greatestProduct(array)
    print(f'The greatest product for the array {array} is : {result} as its the product of {highestNumber1} and {highestNumber2} at index {hIndex1} and {hIndex2} resp.')
