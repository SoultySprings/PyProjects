#This code has been taken from the book A CSG to DSA
#It iterates over an array and concates 'n' strings where n is the number of characters overall
#For example array i/p = ['a', 'b' 'c'] and n=2, then ['ab','ac','ba','bc','ca','cb']
#The time complexity for the algorithm below is O(N^2)

def wordBuilder(array):
    collections = []

    for ith_index, ith in enumerate(array):
        for jth_index, jth in enumerate(array):
            if ith_index != jth_index:
                collections.append(ith+jth)

    return collections

def intBuilder(array):
    collections = []

    for ith_index, ith in enumerate(array):
        for jth_index, jth in enumerate (array):
            if ith_index != jth_index:

                collections.append(int(str(ith)+str(jth)))

    return collections

if __name__ == '__main__' :
    intArray = list(range(1,4))
    strArray = ['a', 'b', 'c']

    print(f'String Array is : {strArray}')
    strCollection = wordBuilder(strArray)
    print(f'Array is : {strCollection}\n')
    print(f'Integer Array is : {intArray}')
    intCollection = intBuilder(intArray)
    print(f'Array is : {intCollection}')
