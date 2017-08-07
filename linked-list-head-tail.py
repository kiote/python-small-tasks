class List(object):
    def __init__(self, head):
        self.head = head
        self.tail = None
    def add(self, elem):
        current = self.head
        while (current.next):
            current = current.next
        current.next = elem
        self.tail = elem
    def addAfter(self, elem, elem2):
        current = self.head
        inserted = False
        while (current and current != elem):
            current = current.next
        if (current == elem):
            elem2.next = current.next
            current.next = elem2
            inserted = True
        return inserted
    def print(self):
        current = self.head
        while (current.next):
            print(current.data)
            current = current.next
        print(current.data)

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

l = List(node1)
l.add(node2)
l.add(node3)

l.print()
print(l.addAfter(node2, node4))
l.print()
