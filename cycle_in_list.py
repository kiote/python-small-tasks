class List(object):
    def __init__(self, head):
        self.head = head
    def cycle(self):
        current = self.head
        while(current.next):
            current = current.next
            checker = self.head
            while(checker != current):
                if (checker == current.next):
                    return True
                checker = checker.next
        return False

class Node(object):
    def __init__(self, data):
        self.next = None
        self.data = data

node1 = Node(3)
node2 = Node(2)
node3 = Node(4)
node4 = Node(6)
node5 = Node(2)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

lst = List(node1)
print(lst.cycle())

node5.next = node3
lst = List(node1)
print(lst.cycle())
