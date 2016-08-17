class LinkedList(object):
    def __init__(self, value):
        self.value = value
        self.next = None

    def add(self, value):
        lst = LinkedList(value)
        self.next = lst
        return lst

    def __str__(self):
        print str(self.value)

    def next(self):
        return self.next


lst = LinkedList(1)
lst.add(2).add(3).add(4)

print lst
lst.next 
print lst
