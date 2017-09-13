class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree(object):
    def __init__(self, head):
        self.head = head

def initTree():
    print("Inint tree:")
    node1 = Node(5)
    node2 = Node(3)
    node3 = Node(10)
    node4 = Node(1)
    node5 = Node(4)
    node6 = Node(7)
    node7 = Node(12)

    tree = Tree(node1)
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node3.right = node7
