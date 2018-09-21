import unittest
from unittest import TestCase
from linked_list import LinkedList

def add_link_number(l1, l2):
    ''' add 2 number in ll, small digit as head
    eg 123: 3->2->1
    '''
    if not l1:
        return l2
    if not l2:
        return l1

    p1,p2 = l1, l2
    v = l1.value + l2.value
    inc,mod = divmod(v, 10)
    r = LinkedList(mod)
    last = r
    while p1.next and p2.next:
        v = p1.next.value + p2.next.value + inc
        inc,mod = divmod(v, 10)
        last.append(LinkedList(mod))
        last = last.next
        p1, p2 = p1.next, p2.next

    p = p1.next or p2.next
    while p:
        if inc == 1 and p.value == 9:
            last.append(0)
        else:
            last.append(LinkedList(p.value + inc))
            inc = 0
        last = last.next
        p = p.next

    if inc == 1:
        last.append(LinkedList(inc))

    return r

class TestRemoveNode(TestCase):
    def test_add_empty(self):
        l1 = LinkedList(1)
        l2 = None
        result1 = add_link_number(l1, l2)
        result2 = add_link_number(l2, l1)
        gold = '1'
        self.assertEqual(gold, str(result1))
        self.assertEqual(gold, str(result2))

    def test_diff_length(self):
        l1 = LinkedList(1)
        l2 = LinkedList(1)
        l2.append(3)
        result1 = add_link_number(l1, l2)
        result2 = add_link_number(l2, l1)
        gold = '2 3'
        self.assertEqual(gold, str(result1))
        self.assertEqual(gold, str(result2))

    def test_carry(self):
        # 919 + 82
        l1 = LinkedList(9)
        l1.append(1)
        l1.append(9)
        l2 = LinkedList(2)
        l2.append(8)
        result1 = add_link_number(l1, l2)
        result2 = add_link_number(l2, l1)
        gold = '1 0 0 1'
        self.assertEqual(gold, str(result1))
        self.assertEqual(gold, str(result2))

if __name__ == '__main__':
    unittest.main()

