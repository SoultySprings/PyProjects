import basicNode
class LinkedList:
    def __init__(self, firstNode = None):
        self.firstNode = firstNode

    def read(self, index):
        currentNode = self.firstNode
        currentIndex = 0

        while currentIndex < index:
            currentNode = currentNode.nextNode
            currentIndex += 1

            if not currentNode:
                return None

        return currentNode.data

    def search(self, value):
        currentNode = self.firstNode
        currentIndex = 0

        while True:
            if currentNode == value:
                return currentIndex
            currentNode = currentNode.nextNode

            if not currentNode:
                break

            currentIndex += 1
        return None


