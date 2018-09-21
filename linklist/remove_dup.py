import unittest
from unittest import TestCase
from linked_list import LinkedList

def remove_dup(ll):
    ''' with a set recording existing nodes '''
    if not ll or not ll.next:
        return
    exists = set()
    exists.add(ll.value)
    p = ll
    while p.next:
        v = p.next.value
        if v in exists:
            dup, p.next = p.next, p.next.next
            del dup
        else:
            p = p.next
            exists.add(v)

def remove_dup_inplace(ll):
    ''' no extra buffer '''
    if not ll or not ll.next:
        return

    p = ll
    while p.next:
        q = ll
        while q != p.next:
            if q.value == p.next.value:
                dup, p.next = p.next, p.next.next
                del dup
                break
            q = q.next
        if q == p.next:
            p = p.next


class TestRemoveDup(TestCase):
    def setUp(self):
        self.ll = LinkedList(1)
        self.ll.append(2)
        self.ll.append(3)
        self.ll.append(3)
        self.ll.append(4)
        self.ll.append(3)
        self.gold = ['1','2','3', '4']

    def test_rm_with_map(self):
        remove_dup(self.ll)
        self.assertEqual(' '.join(self.gold), str(self.ll))

    #@unittest.skip('skip inplace')
    def test_rm_inplace(self):
        remove_dup_inplace(self.ll)
        self.assertEqual(' '.join(self.gold), str(self.ll))

if __name__ == '__main__':
    unittest.main()

