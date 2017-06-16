class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(1)
node2 = Node(2)
head.next = node2
node3 = Node(3)
node2.next = node3

ref = head
while(ref):
    print(ref.data)
    ref = ref.next
