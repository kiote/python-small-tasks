import sys
from binary_tree import *
tree = initTree()

current = tree.head
elem_to_find = 0
while(current):
    if (current.data == elem_to_find):
        print(current.data)
        sys.exit()
    elif (current.data < elem_to_find):
        current = current.right
    else:
        current = current.left
print("not found")

