class List(object):
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail
    def unflatten(self, elem=None):
        if (not elem):
            elem = self.head
        if (elem != self.tail and elem.next):
            if (elem.child):
                self.poke_child(elem.child)
                self.unflatten(elem.child)
            else:
                self.unflatten(elem.next)
    def poke_child(self, child):
        child.prev.next = None
        child.prev = None

class Node(object):
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
        self.child = None

