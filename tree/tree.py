from unittest import TestCase

class Node:
    def __init__(self, v):
        self.value = v
        self.left = None
        self.right = None

class TraverseRecursion:
    __slots__ = []

    @classmethod
    def pre_order(cls, n):
        if n == None:
            return
        yield n.value
        yield from cls.pre_order(n.left)
        yield from cls.pre_order(n.right)

    @classmethod
    def in_order(cls, n):
        if n == None:
            return
        yield from cls.in_order(n.left)
        yield n.value
        yield from cls.in_order(n.right)

    @classmethod
    def post_order(cls, n):
        if n == None:
            return
        yield from cls.post_order(n.left)
        yield from cls.post_order(n.right)
        yield n.value

class TraverseStack:
    __slots__ = []

    @classmethod
    def pre_order(cls, r):
        if r == None:
            return
        stack = [r]

        while len(stack) > 0:
            p = stack.pop()
            yield p.value
            if p.left:
                stack.append(p.left)
            if p.right:
                stack.append(p.right)

    @classmethod
    def in_order(cls, r):
        if r == None:
            return

        p = r
        stack = []
        while p:
            stack.append(p)
            p = p.left

        while len(stack) > 0:
            p = stack.pop()
            yield p.value
            p = p.right
            while p:
                stack.append(p)
                p = p.left

    @classmethod
    def post_order(cls, r):
        if r == None:
            return

        p = r
        stack = []
        while p:
            stack.append(p)
            p = p.left

        poped = None
        while len(stack) > 0:
            p = stack[-1] # peek
            if p.right == poped:
                poped = stack.pop()
                yield poped.value
            else:
                poped = None
                p = p.right
                while p:
                    stack.append(p)
                    p = p.left

def insert_node(r, n):
    if r == None:
        r = n

    if n.value <= r.value:
        if r.left == None:
            r.left = n
        else:
            insert_node(r.left, n)
    else:
        if r.right == None:
            r.right = n
        else:
            insert_node(r.right, n)
    return r

def delete_node(r, v):
    # search parent of v
    p, n = None, None
    if r.value == v:
        n = r
    else:
        stack = [r]
        while stack:
            t = stack.pop()
            if t.left:
                if t.left.value == v:
                    p = t
                    n = t.left
                    break
                else:
                    stack.append(t.left)
            if t.right:
                if t.right.value == v:
                    p = t
                    n = t.right
                    break
                else:
                    stack.append(t.right)

    if not n: return r

    # reconstruct subtree of root n
    promoted = None
    if not n.right:
        promoted = n.left
    elif not n.left:
        promoted = n.right
    else: # n.left and n.right:
        c = n.right
        while c.left:
            c = c.left
        promoted = Node(c.value)
        promoted.left = n.left
        promoted.right = delete_node(n.right, c.value)

    if not p:
        del n
        return promoted

    if p.left == n:
        p.left = promoted
    else:
        p.right = promoted

    del n
    return r

class TestTree(TestCase):
    def setUp(self):
        self.root = Node(5)
        for e in [2,4,9,11,1,3,6,8,7,10]:
            insert_node(self.root, Node(e))

    def test_recur_inorder(self):
        cls = TraverseRecursion
        gold = [e for e in range(1, 12)]
        list = [e for e in cls.in_order(self.root)]
        self.assertEqual(gold, list)

    def test_recur_prepost_order(self):
        cls = TraverseRecursion
        gold = [e for e in range(1, 12)]
        pre = [e for e in sorted(cls.pre_order(self.root))]
        self.assertEqual(gold, pre)
        post = [e for e in sorted(cls.post_order(self.root))]
        self.assertEqual(gold, post)

    def test_stack_inorder(self):
        cls = TraverseStack
        gold = [e for e in range(1, 12)]
        list = [e for e in cls.in_order(self.root)]
        self.assertEqual(gold, list)

    def test_stack_prepost_order(self):
        cls = TraverseStack
        gold = [e for e in range(1, 12)]
        pre = [e for e in sorted(cls.pre_order(self.root))]
        self.assertEqual(gold, pre)
        post = [e for e in sorted(cls.post_order(self.root))]
        self.assertEqual(gold, post)

    def test_deletion(self):
        cls = TraverseStack
        gold = [e for e in range(1, 12)]
        for e in range(1, 12):
            gold.remove(e)
            self.root = delete_node(self.root, e)
            list = [e for e in cls.in_order(self.root)]
            self.assertEqual(gold, list)


if __name__ == '__main__':
    unittest.main()

