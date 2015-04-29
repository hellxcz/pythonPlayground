__author__ = 'zdenek'


class TreeNode:
    def __init__(self, left, right):
        self.left = left
        self.right = right


tree = TreeNode(None, None)
tree.value = 3


class Bunch(dict):
    def __init__(self, *args, **kwds):
        super(Bunch, self).__init__(*args, **kwds)
        self.__dict__ = self

# t = Tree(Tree("a", "b"), Tree("c", "d"))

T = Bunch
t = T(left=T(left=1, right=2), right=T(left=3))

print t.left



print t.left.right

