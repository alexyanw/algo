from unittest import TestCase

from .tree import *
import sys

def is_balanced(r):
    def max_depth(r):
        if r == None: return 0
        return max(max_depth(r.left), max_depth(r.right)) + 1

    def min_depth(r):
        if r == None: return 0
        return min(min_depth(r.left), min_depth(r.right)) + 1

    if max_depth(r) - min_depth(r) <= 1:
        return True
    else:
        return False

def is_balanced_post(r):
    ''' post_order traverse the tree, get depth of left and right
    and compare at current node'''
    if r == None: return True
    depth = 0
    stack = []
    p = r
    while p:
        stack.append((p, depth))
        depth += 1
        p = p.left

    min_depth, max_depth = sys.maxsize, 0
    poped = None
    while stack:
        t,d = stack[-1]  # peek
        if t.right == poped or t.right == None:
            poped,d = stack.pop()
            if poped.left == None and poped.right == None: # leaf
                min_depth = min(min_depth, d)
                max_depth = max(max_depth, d)
                if abs(min_depth-max_depth) > 1:
                    return False
        else:
            p,d = t.right, d+1
            while p:
                stack.append((p, d))
                d += 1
                p = p.left
            poped = None

    return True


class TestTreeBalanced(TestCase):
    def test_balanced_1(self):
        n = [Node(i) for i in range(5)]
        n[0].left, n[0].right = n[1], n[2]
        n[1].left, n[1].right = n[3], n[4]
        self.assertEqual(True, is_balanced(n[0]))
        self.assertEqual(True, is_balanced_post(n[0]))

    def test_balanced_2(self):
        n = [Node(i) for i in range(5)]
        n[0].left, n[0].right = n[1], n[2]
        n[2].left, n[2].right = n[3], n[4]
        self.assertEqual(True, is_balanced(n[0]))
        self.assertEqual(True, is_balanced_post(n[0]))

    def test_balanced_3(self):
        n = [Node(i) for i in range(5)]
        n[0].left, n[0].right = n[1], n[2]
        n[1].left, n[2].right = n[3], n[4]
        self.assertEqual(True, is_balanced(n[0]))
        self.assertEqual(True, is_balanced_post(n[0]))

    def test_balanced_4(self):
        n = [Node(i) for i in range(5)]
        n[0].left, n[0].right = n[1], n[2]
        n[1].right, n[2].left = n[3], n[4]
        self.assertEqual(True, is_balanced(n[0]))
        self.assertEqual(True, is_balanced_post(n[0]))

    def test_balanced_5(self):
        n = [Node(i) for i in range(5)]
        n[0].left, n[0].right = n[1], n[2]
        n[1].right, n[2].left = n[3], n[4]
        self.assertEqual(True, is_balanced(n[0]))
        self.assertEqual(True, is_balanced_post(n[0]))

    def test_imbalance_1(self):
        n = [Node(i) for i in range(5)]
        n[0].left, n[0].right = n[1], n[2]
        n[1].left = n[3]
        n[3].left = n[4]
        self.assertEqual(False, is_balanced(n[0]))
        self.assertEqual(False, is_balanced_post(n[0]))

    def test_imbalance_2(self):
        n = [Node(i) for i in range(5)]
        n[0].left, n[0].right = n[1], n[2]
        n[1].left = n[3]
        n[3].right = n[4]
        self.assertEqual(False, is_balanced(n[0]))
        self.assertEqual(False, is_balanced_post(n[0]))

    def test_imbalance_3(self):
        n = [Node(i) for i in range(5)]
        n[0].left, n[0].right = n[1], n[2]
        n[2].left = n[3]
        n[3].left = n[4]
        self.assertEqual(False, is_balanced(n[0]))
        self.assertEqual(False, is_balanced_post(n[0]))

    def test_imbalance_4(self):
        n = [Node(i) for i in range(5)]
        n[0].left, n[0].right = n[1], n[2]
        n[2].left = n[3]
        n[3].right = n[4]
        self.assertEqual(False, is_balanced(n[0]))
        self.assertEqual(False, is_balanced_post(n[0]))

    def test_imbalance_5(self):
        n = [Node(i) for i in range(5)]
        n[0].left, n[0].right = n[1], n[2]
        n[2].right = n[3]
        n[3].left = n[4]
        self.assertEqual(False, is_balanced(n[0]))
        self.assertEqual(False, is_balanced_post(n[0]))

if __name__ == '__main__':
    unittest.main()

