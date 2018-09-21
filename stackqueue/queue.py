from unittest import TestCase

class Node:
    def __init__(self, v):
        self.value = v
        self.next = None
        self.end = self

    def append(self, v):
        self.end.next = Node(v)
        self.end = self.end.next
        return self.end

    def __iter__(self):
        self.it = self
        return self

    def __next__(self):
        if self.it == None:
            raise StopIteration
        p = self.it
        self.it = p.next
        return p

    def __str__(self):
        return ' '.join(str(n.value) for n in self)


class Queue:
    def __init__(self):
        self.first = None
        self.last = None

    def enqueue(self, v):
        n = Node(v)
        if self.first == None:
            self.first = n
            self.last = n
        else:
            self.last.next = n
            self.last = n

    def dequeue(self):
        if self.first == None:
            raise IndexError
        n = self.first
        self.first = n.next
        return n.value

    def __str__(self):
        return str(self.first)

class TestQueue(TestCase):
    def setUp(self):
        self.queue = Queue()

    def test_enqueue(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.assertEqual('1 2', str(self.queue))

    def test_dequeue(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.assertEqual(1, self.queue.dequeue())
        self.assertEqual(2, self.queue.dequeue())
        self.assertRaises(IndexError, self.queue.dequeue)

if __name__ == '__main__':
    unittest.main()

