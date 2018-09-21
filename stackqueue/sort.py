import unittest
from unittest import TestCase
from stack import Stack

def sort_stack(stack):
    r = Stack()

    while not stack.is_empty():
        e = stack.pop()
        while not r.is_empty() and r.peek() > e:
            stack.push(r.pop())
        r.push(e)

    return r


class TestSortStack(TestCase):
    def setUp(self):
        self.stack = Stack()
        self.stack.push(1)
        self.stack.push(3)
        self.stack.push(2)
        self.stack.push(4)
        self.stack.push(2)

    def test_sort(self):
        r = sort_stack(self.stack)
        self.assertEqual('1 2 2 3 4', str(r))

    def test_empty(self):
        s = Stack()
        r = sort_stack(s)
        self.assertEqual(True, r.is_empty())

if __name__ == '__main__':
    unittest.main()


