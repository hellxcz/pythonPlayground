__author__ = 'zdenek'


class Node:
    def __init__(self):
        self.value = 0
        self.left = None
        self.right = None


class InOrderParser:
    def __init__(self, inOrderArray):
        self.inOrderArray = inOrderArray

    def parse(self):
        self.rootNode = Node()

        self._divide(self.rootNode, 0, len(self.inOrderArray) - 1)

        return self.rootNode

    def _divide(self, node, startIndex, endIndex):

        array = self.inOrderArray

        half = (endIndex - startIndex) >> 1

        halfIndex = startIndex + half
        node.value = array[halfIndex]

        print(
            'startIndex:', startIndex,
            ', endIndex:', endIndex,
            ', halfIndex:', halfIndex,
            ', halfIndex value:', node.value)

        if startIndex < halfIndex:  # there is still some item on the left side of current value
            node.left = Node()
            self._divide(node.left, startIndex, halfIndex - 1)  # skip current value

        if endIndex > halfIndex:  # there is still something on the right side of current value
            node.right = Node()
            self._divide(node.right, halfIndex + 1, endIndex)  # skip current value


class BinaryTreePrinter:
    def __init__(self, rootNode):
        self.rootNode = rootNode

    def printTree(self):
        treeHeight = self.findHeight(self.rootNode) - 1

        print('treeHeight:', treeHeight)

    def findHeight(self, node):

        leftHeight = 0
        rightHeight = 0

        if node.left is not None:
            leftHeight = self.findHeight(node.left)

        if node.right is not None:
            rightHeight = self.findHeight(node.right)

        if leftHeight > 0 and leftHeight > rightHeight:
            return 1 + leftHeight
        elif rightHeight > 0 and rightHeight > leftHeight:
            return 1 + rightHeight
        else:
            return 1


inOrder = [1, 2, 3, 4, 5, 6, 7, 8]

parser = InOrderParser(inOrder)
rootNode = parser.parse()

treePrinter = BinaryTreePrinter(rootNode)

treePrinter.printTree()



