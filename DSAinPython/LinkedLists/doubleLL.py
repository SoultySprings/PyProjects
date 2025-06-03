import basicNode as node

class doublyLinkedList:
    def __init__(self, firstNode = None, lastNode = None):
        self.firstNode = firstNode
        self.lastNode = lastNode

    def append(self, value):
        newNode = node.Node()
        if not self.firstNode:
            self.firstNode = newNode
            self.lastNode = newNode
        else:
            newNode.previous_node = self.lastNode
            self.lastNode.next_node = newNode
            self.lastNode = newNode