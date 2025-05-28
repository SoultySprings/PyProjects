#This code has been taken from the book A CSG to DSA
#Calculates the product of the ith index of the array with upcoming elements till end
#For example, for [1,2,3,4], o/p is [(1*2)=2,(1*3)=3,(1*4)4,(2*3)=6,,(2*4)=8,,(3*4)=12]
#The time complexity for the algorithm is N!, but it is observed that N!=(N^2)/2 so order is O(N^2)

def twoProduct(array):
    products = []
    for ith in range(len(array)):
        for jth in range(ith+1, len(array)):
            products.append(array[ith]*array[jth])
    return products

if __name__ == '__main__':
    array = list(range(1,5))
    print(f'The array is : {array}.')
    resultArray = twoProduct(array)
    print(f'The result array is : {resultArray}.')
