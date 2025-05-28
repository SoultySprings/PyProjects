#This code has been taken from the book A Common Sense Guide to DSA (in short A CSG to DSA)
#In short calculates the mean of even, odd and then overall numbers present in the array
#The time complexity for the algorithm is 3N+3 but can be taken as O(N)

def averageEvenOddOverall(array):
    sumEven, sumOdd, sumOverall = 0,0,0
    countofEvenNums, countofOddNums, countofOverallNums = 0,0,0
    for number in array:
        if number % 2 == 0 :
            countofEvenNums += 1
            sumEven += number
        elif number % 2 == 1:
            countofOddNums += 1
            sumOdd += number
        sumOverall += number
    return sumEven//countofEvenNums, sumOdd//countofOddNums, sumOverall//len(array)

if __name__ == '__main__' :
    array = list(range(1,100))
    print(f'The given array is : {array}')
    aEven, aOdd, aOver = averageEvenOddOverall(array)
    print(f'Average of even : {aEven}, of odd : {aOdd}, and overall : {aOver}.')