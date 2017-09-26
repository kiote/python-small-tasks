from binary_tree import *

tree = initTree()

def depth(node):
    if (node == None):
        return 0
    return 1 + max(depth(node.right), depth(node.left))

print(depth(tree.head))
