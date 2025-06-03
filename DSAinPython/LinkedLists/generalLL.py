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

    def insert(self, index, value):
        newNode = basicNode.Node(value)

        if index == 0:
            newNode.nextNode = self.firstNode
            self.firstNode = newNode
            return

        currentNode = self.firstNode
        currentIndex = 0

        while currentIndex < (index - 1):
            currentNode = currentNode.nextNode
            currentIndex += 1

        newNode.nextNode = currentNode.nextNode
        currentNode.nextNode = newNode

    def delete(self, index):
        if index == 0 :
            self.firstNode = self.firstNode.nextNode
            return
        currentNode  = self.firstNode
        currentIndex = 0
        while currentIndex < (index - 1):
            currentNode  = currentNode.nextNode
            currentIndex +=1

        nodeAfterDeletedNode = currentNode.nextNode.nextNode
        currentNode.nextNode = nodeAfterDeletedNode
        
