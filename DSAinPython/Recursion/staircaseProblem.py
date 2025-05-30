#The following code has been taken from A CSG to DSA
#Illustrates the famous staircase problem where every possibility of going down a stairs have been mentioned using recursion as backtracking

def Paths(number):
    collection = []
    def numberOfPaths(number):
        if number == '1':
            collection.append('1')
            return 1
        if number == 2:
            collection.append('2')
            return 2
        if number == 3:
            collection.append('3')
            return 3
        return numberOfPaths(number-1) + numberOfPaths(number-2) + numberOfPaths(number-3)
    return collection, numberOfPaths(number)

if __name__ == '__main__':
    stairLevel = 6
    collection, numpaths = Paths(stairLevel)
    print(f'Number of possible paths for {stairLevel} levels, are {numpaths}')
    print(collection)