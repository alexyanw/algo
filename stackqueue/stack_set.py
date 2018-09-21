from unittest import TestCase
from stack import Stack

class StackSet:
    ''' StackSet behave like Stack in case of push/pop
    It maintains an internal set of stacks with limit number of elements
    '''
    def __init__(self, limit):
        self.set = []
        self.limit = limit

    def push(self, v):
        if len(self.set) == 0 or len(self.set[-1]) == self.limit:
            s = Stack()
            self.set.append(s)
        else:
            s = self.set[-1]
        s.push(v)

    def popAt(self, i):
        if len(self.set) <= i:
            raise IndexError
        s = self.set[i]
        v = s.pop()
        if len(s) == 0:
            del self.set[i]

        return v

    def pop(self):
        return self.popAt(-1)

    def __str__(self):
        return ' '.join([str(s) for s in self.set])

class TestStackSet(TestCase):
    def setUp(self):
        self.stack = StackSet(2)

    def test_push_pop(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.assertEqual('1 2 3', str(self.stack))
        self.assertEqual(3, self.stack.pop())
        self.assertEqual(2, self.stack.pop())
        self.assertEqual(1, self.stack.pop())
        self.assertRaises(IndexError, self.stack.pop)

    def test_pop_at(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.stack.push(4)
        self.stack.push(5)
        self.assertEqual(4, self.stack.popAt(1))
        self.assertEqual(3, self.stack.popAt(1))
        self.assertEqual(5, self.stack.popAt(1))
        self.assertRaises(IndexError, self.stack.popAt, 1)

if __name__ == '__main__':
    unittest.main()

