from unittest import TestCase
from linked_list import Node

class TestMyLinkedList(TestCase):
    def test_kth_to_last_elem(self):
        try:
            from build import MyLinkedList
        except ImportError:
            self.assertFalse("no function found")


        linked_list = MyLinkedList(None)
        self.assertEqual(linked_list.kth_to_last_elem(0), None)

        self.assertEqual(linked_list.kth_to_last_elem(100), None)

        head = Node(2)
        linked_list = MyLinkedList(head)
        self.assertEqual(linked_list.kth_to_last_elem(0), 2)

        linked_list.insert_to_front(1)
        linked_list.insert_to_front(3)
        linked_list.insert_to_front(5)
        linked_list.insert_to_front(7)

        self.assertEqual(linked_list.kth_to_last_elem(2), 3)
