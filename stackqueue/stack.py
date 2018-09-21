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


class Stack:
    ''' Implement stack with linked list'''
    def __init__(self):
        self.top = None
        self.count = 0

    def push(self, v):
        if self.top == None:
            self.top = Node(v)
        else:
            n = Node(v)
            n.next = self.top
            self.top = n
        self.count += 1

    def pop(self):
        if self.top == None:
            raise IndexError
        n = self.top
        self.top = n.next
        self.count -= 1
        return n.value

    def peek(self):
        if self.top == None:
            return None
        return self.top.value

    def is_empty(self):
        return self.top == None

    def __len__(self):
        return self.count

    def __str__(self):
        if self.top:
            return str(self.top)[::-1]
        else:
            return ''

class TestStack(TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_peek(self):
        self.stack.push(1)
        self.assertEqual(1, self.stack.peek())
        self.stack.pop()
        self.assertEqual(None, self.stack.peek())

    def test_empty(self):
        self.assertEqual(True, self.stack.is_empty())
        self.stack.push(1)
        self.assertEqual(False, self.stack.is_empty())
        self.stack.pop()
        self.assertEqual(True, self.stack.is_empty())

    def test_push(self):
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual('1 2', str(self.stack))

    def test_pop(self):
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(2, self.stack.pop())
        self.assertEqual(1, self.stack.pop())
        self.assertRaises(IndexError, self.stack.pop)

if __name__ == '__main__':
    unittest.main()

