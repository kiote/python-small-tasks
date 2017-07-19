##
# list basic operations
#
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

def remove(list, elem):
    prev = None
    current = list.head
    saved_head = current

    if (current == elem):
        current = elem.next
        saved_head = current
    else:
        prev = current
        current = current.next

    while(current):
        if (current == elem):
            prev.next = elem.next
            current = elem.next
        else:
            prev = current
            current = current.next

    return List(saved_head)

head = Node(1)
myList = List(head)

node2 = Node(2)
head.next = node2
node3 = Node(3)
node2.next = node3

printList(myList)

myList = remove(myList, head)
printList(myList)
