#This code has been taken from the book A CSG to DSA
#Takes two sorted arrays and merges them to create a new array
#For example, for [1,2,3] and [2,3,5,6], o/p is [1,2,2,3,3,5,6]
#The time complexity for the algorithm is O(N*M)

def merge(arrayOne, arrayTwo):
    newArray = []
    arrayPointerOne = 0
    arrayPointerTwo = 0

    while arrayPointerOne<len(arrayOne) or arrayPointerTwo<len(arrayTwo):
        if arrayPointerOne >= len(arrayOne):
            newArray.append(arrayTwo[arrayPointerTwo])
            arrayPointerTwo += 1

        elif arrayPointerTwo >= len(arrayTwo):
            newArray.append(arrayOne[arrayPointerOne])
            arrayPointerOne += 1

        elif arrayOne[arrayPointerOne] < arrayTwo[arrayPointerTwo]:
            newArray.append(arrayOne[arrayPointerOne])
            arrayPointerOne += 1

        else:
            newArray.append(arrayTwo[arrayPointerTwo])
            arrayPointerTwo += 1


    return newArray

if __name__ == '__main__':
    arrayOne = [1,2,3]
    arrayTwo = [2,3,5,6]
    print(f'The two arrays are as follows : {arrayOne}, and {arrayTwo}')
    newArray = merge(arrayOne, arrayTwo)
    print(f'The new merged array is : {newArray}')


