import Node

class binarySearchTree:

    def insert(value, node):
        if value < node.value:
            if not node.leftChild:
                node.leftChild = Node.node(value)
            else:
                binarySearchTree.insert(value, node.leftChild)
        elif value > node.value:
            if not node.rightChild:
                node.rightChild = Node.node(value)
            else:
                binarySearchTree.insert(value, node.rightChild)

if __name__ == '__main__':
    binarySearchTree.insert(5)
