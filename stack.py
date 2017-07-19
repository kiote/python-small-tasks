class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack(object):
    def __init__(self, head):
        self.head = head
        self.tail = head
    def push(self, elem):
        self.tail.next = elem
        self.tail = elem
    def print(self):
        current = self.head
        while(current):
            print(current.data)
            current = current.next

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

stack = Stack(node1)
stack.push(node2)
stack.push(node3)

stack.print()
