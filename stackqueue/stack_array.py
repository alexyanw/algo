from unittest import TestCase

class StackArray:
    count = 3
    def __init__(self, list, index):
        if index >= StackArray.count:
            raise ValueError
        self.index = index
        self.list = list
        self.top = -1 - self.index

    def push(self, v):
        self.top += StackArray.count
        if self.top >= len(self.list):
            self.list.extend([0]*(StackArray.count - self.index -1) + [v] + [0]*self.index)
        else:
            self.list[self.top] = v

    def pop(self):
        if self.top < 0:
            raise IndexError
        v = self.list[self.top]
        self.top -= StackArray.count
        return v

class TestStackArray(TestCase):
    def setUp(self):
        list = []
        self.stack0 = StackArray(list, 0)
        self.stack1 = StackArray(list, 1)
        self.stack2 = StackArray(list, 2)

    def test_stack0(self):
        self.stack0.push(1)
        self.stack0.push(2)
        v = self.stack0.pop()
        self.assertEqual(2, v)
        v = self.stack0.pop()
        self.assertEqual(1, v)
        self.assertRaises(IndexError, self.stack0.pop)

    def test_stack2(self):
        self.stack2.push(1)
        self.stack2.push(2)
        v = self.stack2.pop()
        self.assertEqual(2, v)
        v = self.stack2.pop()
        self.assertEqual(1, v)
        self.assertRaises(IndexError, self.stack0.pop)
        self.assertRaises(IndexError, self.stack2.pop)


    def test_3stacks(self):
        self.stack0.push(1)
        self.stack0.push(2)
        self.stack0.push(3)
        self.stack1.push(4)
        self.stack1.push(5)
        self.stack1.push(6)
        self.stack2.push(7)
        self.stack2.push(8)
        self.stack2.push(9)

        v = self.stack2.pop()
        self.assertEqual(9, v)
        v = self.stack1.pop()
        self.assertEqual(6, v)
        v = self.stack0.pop()
        self.assertEqual(3, v)


if __name__ == '__main__':
    unittest.main()
