import sys
from binary_tree import *
tree = initTree()

def find(root, value):
    if (root == None):
        print("Not found")
        return
    if (root.data == value):
        print("Found")
        return value
    if (root.data > value):
        find(root.left, value)
    else:
        find(root.right, value)

find(tree.head, 0)
