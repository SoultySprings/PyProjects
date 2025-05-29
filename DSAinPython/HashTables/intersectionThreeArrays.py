#This code has been taken from the book A CSG to DSA
#Code checks if the second array is a subset of another using iteration comparisons
#For example, for [1,2,3] and [2,3,5,6], o/p is False, as [1,2,3] ISN'T a subset of [2,3,5,6]
#The time complexity for the algorithm is O(N)

def intersectionArrays(arrayOne, arrayTwo,arrayThree):
    hashTable = {}
    for value in arrayOne:
        hashTable[value] = True
    for value in arrayTwo:
        if hashTable.get(value) == True:
            pass
        else:
            arrayOne.append(value)
    for value in arrayThree:
        if hashTable.get(value) == True:
            pass
        else:
            arrayOne.append(value)
    return arrayOne

if __name__ == '__main__':
    array1 = [1,2,3,4,5]
    array2 = [0,2,4,6,8]
    array3 = [2,4]
    print(f"Arrays are : {array1},{array2} and {array3}.")
    array = intersectionArrays(array1, array2, array3)
    print(f'Resultant array is : {array}')