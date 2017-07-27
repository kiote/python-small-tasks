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
        if (not current):
            return None
        if (current.next is None):
            self.head = None
            self.tail = None
            return current
        while ((current.next != self.tail) and (current.next)):
            current = current.next
        old_tail = self.tail
        self.tail = current
        current.next = None
        return old_tail
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

#stack.print()

e = stack.pop()
print(e.data)
e = stack.pop()
print(e.data)
e = stack.pop()
print(e.data)
