import unittest
from unittest import TestCase
from stack import Stack

class StackQueueMy:
    ''' Implement queue with 2 stacks '''
    def __init__(self):
        self.stacks = [Stack(), Stack()]
        self.at = 0

    def enqueue(self, v):
        if self.at == 1:
            try:
                while True:
                    self.stacks[0].push(self.stacks[1].pop())
            except IndexError:
                pass
            self.at = 0
        self.stacks[0].push(v)

    def dequeue(self):
        if self.at == 0:
            try:
                while True:
                    self.stacks[1].push(self.stacks[0].pop())
            except IndexError:
                pass
            self.at = 1
        return self.stacks[1].pop()

    def __str__(self):
        if self.at == 1:
            return str(self.stacks[1])[::-1]
        else:
            return str(self.stacks[0])

class StackQueue:
    ''' Implement queue with 2 stacks '''
    def __init__(self):
        self.stack0 = Stack()
        self.stack1 = Stack()

    def enqueue(self, v):
        self.stack0.push(v)

    def dequeue(self):
        if not self.stack1.is_empty():
            return self.stack1.pop()
        while not self.stack0.is_empty():
            self.stack1.push(self.stack0.pop())
        return self.stack1.pop()

    def peek(self):
        if not self.stack1.is_empty():
            return self.stack1.peek()

        while not self.stack0.is_empty():
            self.stack1.push(self.stack0.pop())

        return self.stack1.peek()

    def __str__(self):
        return str(self.stack1)[::-1] + str(self.stack0)

class TestStackSet(TestCase):
    def setUp(self):
        self.queue = StackQueue()

    def test_enqueue(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.assertEqual('1 2', str(self.queue))

    #@unittest.skip('temp')
    def test_dequeue(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)
        self.assertEqual(1, self.queue.dequeue())
        self.assertEqual('2 3', str(self.queue))
        self.assertEqual(2, self.queue.dequeue())
        self.assertEqual(3, self.queue.dequeue())
        self.assertRaises(IndexError, self.queue.dequeue)

    def test_peek(self):
        self.queue.enqueue(1)
        self.assertEqual(1, self.queue.peek())
        self.queue.enqueue(2)
        self.assertEqual(1, self.queue.peek())
        self.assertEqual(1, self.queue.peek())
        self.assertEqual(1, self.queue.dequeue())
        self.assertEqual(2, self.queue.peek())
        self.assertEqual(2, self.queue.peek())
        self.assertEqual(2, self.queue.dequeue())
        self.assertEqual(None, self.queue.peek())


if __name__ == '__main__':
    unittest.main()


