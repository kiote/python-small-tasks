class List(object):
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail
    def flatten(self):
        current = self.head
        while(current != self.tail):
            if (current.child):
                self.tail.next = current.child
                current.child.prev = self.tail
                self.tail = current.child
                while(self.tail.next):
                    self.tail = self.tail.next
            current = current.next
    def print(self):
        self.flatten()
        current = self.head
        while(current):
            print(current.data)
            current = current.next

class Node(object):
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
        self.child = None

node1 = Node(5)
node2 = Node(33)
node3 = Node(17)
node4 = Node(2)
node5 = Node(1)
node6 = Node(6)
node7 = Node(25)
node8 = Node(6)
node9 = Node(2)
node10 = Node(7)
node11 = Node(8)
node12 = Node(9)
node13 = Node(12)
node14 = Node(5)
node15 = Node(7)
node16 = Node(21)
node17 = Node(3)

node1.next = node2
node2.prev = node1
node1.child = node6
node6.next = node7
node7.prev = node6
node7.child = node11
node7.next = node8

node2.next = node3
node3.prev = node2
node3.next = node4
node4.prev = node3
node4.next = node5
node5.prev = node4
node4.child = node9
node9.next = node10
node10.prev = node9

node7.child = node11
node8.child = node12
node12.child = node15

node9.child = node13
node13.next = node14
node14.prev = node13

node13.child = node16
node16.next = node17
node17.prev = node16


lst = List(node1, node5)
lst.print()
