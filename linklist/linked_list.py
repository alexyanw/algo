from unittest import TestCase

class LinkedList:
    def __init__(self, v):
        self.value = v
        self.next = None

    def append(self, v):
        new_node = LinkedList(v)
        n = self
        while n.next:
            n = n.next
        n.next = new_node
        return new_node

    def __iter__(self):
        self.it = self
        return self

    def __next__(self):
        if self.it == None:
            raise StopIteration
        p = self.it
        self.it = p.next
        return p

    def traverse(self):
        p = self
        while p:
            yield p
            p = p.next

    def __str__(self):
        return ' '.join(str(n.value) for n in self)

class TestLinkedList(TestCase):
    def setUp(self):
        self.ll = LinkedList(1)
        self.ll.append(2)
        self.ll.append(3)
        self.gold = ['1','2','3']

    def test_iter(self):
        # it=iter(ll) => ll.__iter__(), next(it) => it.__next__()
        for i,e in enumerate(self.ll):
            self.assertEqual(' '.join(self.gold[i:]), str(e))

    def test_generator(self):
        for i,e in enumerate(self.ll.traverse()):
            self.assertEqual(self.gold[i], str(e.value))

    def test_str(self):
        self.assertEqual(' '.join(self.gold), str(self.ll))

if __name__ == '__main__':
    unittest.main()
