import unittest
from unittest import TestCase
from linked_list import LinkedList

def remove_node(n):
    ''' remove a node in middle, only access this node'''
    prev = None
    while n.next:
        n.value = n.next.value
        p = n
        n = n.next
    p.next = None
    del n

class TestRemoveNode(TestCase):
    def setUp(self):
        self.ll = LinkedList(1)
        self.ll.append(2)
        self.ll.append(3)
        self.ll.append(4)
        self.gold = ['1','2','4']

    def test_rm_node(self):
        remove_node(self.ll.next.next)
        self.assertEqual(' '.join(self.gold), str(self.ll))

if __name__ == '__main__':
    unittest.main()

