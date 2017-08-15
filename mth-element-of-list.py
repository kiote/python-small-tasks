class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class List(object):
    def __init__(self, node):
        self.head = node
        self.current = self.head
    def add(self, elem):
        self.current.next = elem
        self.current = elem
    def print(self):
        current = self.head
        while(current):
            print(current.data)
            current = current.next
    def mth(self, m):
        current_suspected = self.head
        current = self.head
        count = 0
        while(current):
            current = current.next
            if (count > m):
                current_suspected = current_suspected.next
            count += 1
        print(current_suspected.data)


lst = List(Node(1))
lst.add(Node(2))
lst.add(Node(3))
lst.add(Node(4))

lst.print()

lst.mth(4)
