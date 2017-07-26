class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack(object):
    def __init__(self):
        self.head = None
        self.tail = None
    def push(self, elem):
        if (not self.head):
            self.head = elem
        else:
            if (not self.tail):
                self.head.next = elem
                self.tail = elem
            self.tail.next = elem
            self.tail = elem
    def pop(self):
        current = self.head
        if (not current.next):
            self.head = None
            return current
        if (not current):
            return None
        while (current.next != self.tail):
            current = current.next
        self.tail = current
        return self.tail
    def print(self):
        current = self.head
        while(current):
            print(current.data)
            current = current.next

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

stack = Stack()
stack.push(node1)
stack.push(node2)
stack.push(node3)

stack.print()

stack.pop()
stack.pop()

stack.print()
