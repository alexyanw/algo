import unittest
from unittest import TestCase
from linked_list import LinkedList

def find_circle_start(ll):
    ''' find the circle entry node 
    eg: A->B->C->D->E->C ==> C
    '''
    if not ll or not ll.next: return None
    p1, p2 = ll.next, ll.next.next
    while p1 and p2 and p2.next and p1 != p2:
        p1 = p1.next
        p2 = p2.next.next
    if not p2.next:
        return None

    p = ll
    while p != p2:
        p = p.next
        p2 = p2.next

    return p

class TestCircular(TestCase):
    def test_circle_none(self):
        ll = LinkedList(1)
        ll.append(2)
        ll.append(3)
        n = find_circle_start(ll)
        self.assertEqual(None, n)

    def test_circle(self):
        ll = LinkedList(1)
        ll.append(2)
        entry = ll.append(3)
        ll.append(4)
        last = ll.append(5)
        last.next = entry
        n = find_circle_start(ll)
        self.assertEqual(entry.value, n.value)

if __name__ == '__main__':
    unittest.main()

