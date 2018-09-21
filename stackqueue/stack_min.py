from unittest import TestCase

class StackMin:
    def __init__(self):
        self.list = []

    def push(self, v):
        m = v
        if len(self.list) > 0:
            m = min(self.list[-1][1], v)
        self.list.append((v, m))

    def pop(self):
        if len(self.list) <= 0:
            raise IndexError
        e = self.list.pop()
        return e[0]

    def min(self):
        if len(self.list) <= 0:
            raise IndexError
        return self.list[-1][1]

class TestStackMin(TestCase):
    def setUp(self):
        self.stack = StackMin()

    def test_pop_error(self):
        self.assertRaises(IndexError, self.stack.pop)

    def test_push_pop(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)

        v = self.stack.pop()
        self.assertEqual(3, v)
        v = self.stack.pop()
        self.assertEqual(2, v)
        v = self.stack.pop()
        self.assertEqual(1, v)

    def test_min(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)

        self.stack.pop()
        self.assertEqual(1, self.stack.min())
        self.stack.pop()
        self.assertEqual(1, self.stack.min())
        self.stack.pop()
        self.assertRaises(IndexError, self.stack.min)

if __name__ == '__main__':
    unittest.main()
