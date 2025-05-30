#The following code has been taken from A CSG to DSA
#It prints subdirectories for as many present for a subdirectory using recurion

import os

def printSubdirectories(directoryName):
    for filename in os.listdir(directoryName):
        path = os.path.join(directoryName, filename)
        if os.path.isdir(path):
            print(path)
            printSubdirectories(path)


if __name__ == '__main__':
    directory = "Recursion"
    print(f'The path for the directory {directory} is {printSubdirectories(directory)}.')
