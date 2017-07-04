class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class List(object):
    def __init__(self, head):
        self.head = head

def printList(list):
    ref = list.head
    while(ref):
        print(ref.data)
        ref = ref.next

head = Node(1)
myList = List(head)

node2 = Node(2)
head.next = node2
node3 = Node(3)
node2.next = node3

printList(myList)
