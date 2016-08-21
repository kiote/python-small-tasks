class LinkedList(object):
    def __init__(self, value):
        self.value = value
        self.next = None

    def add(self, value):
        current_list = self
        new_list = LinkedList(value)
        while current_list.next is not None:
            current_list = current_list.next
        current_list.next = new_list


class TestLinkedList:
    def test_init_sets_value(self):
        assert LinkedList(3).value == 3

    def test_init_sets_next_to_none(self):
        assert LinkedList(3).next is None

    def test_add_adds_next_element(self):
        list = LinkedList(1)
        list.add(2)
        assert list.next is not None

    def test_add_creates_new_linked_object(self):
        list = LinkedList(1)
        list.add(2)
        assert type(list.next) == LinkedList

    def test_add_adds_several_elements(self):
        list = LinkedList(1)
        list.add(2)
        list.add(3)
        assert list.next.next.value == 3
