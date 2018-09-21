from unittest import TestCase
from stack import Stack

class Hanoi:
    ''' StackSet behave like Stack in case of push/pop
    It maintains an internal set of stacks with limit number of elements
    '''
    def __init__(self, n):
        self.total = n
        self.stacks = [Stack(), Stack(), Stack()]
        for d in range(n, 0, -1):
            self.stacks[0].push(d)

    def reset(self):
        self.__init__(self.total)

    def move(self, n, src, dst):
        if n == 1:
            d = self.stacks[src].pop()
            self.stacks[dst].push(d)
            yield 'disk{}: stack{} -> stack{}'.format(d, src, dst)
        else:
            spare = 0
            for i in range(3):
                if i != src and i != dst:
                    spare = i
                    break
            yield from self.move(n-1, src, spare)
            yield from self.move(1, src, dst)
            yield from self.move(n-1, spare, dst)

    def play(self):
        #self.move(self.total, 0, 2)
        self.reset()
        return [s for s in self.move(self.total, 0, 2)]

    def __str__(self):
        steps = self.play()
        return "\n".join(steps)

class TestStackSet(TestCase):
    def setUp(self):
        self.game = Hanoi(3)

    def test_play(self):
        gold = '''\
disk1: stack0 -> stack2
disk2: stack0 -> stack1
disk1: stack2 -> stack1
disk3: stack0 -> stack2
disk1: stack1 -> stack0
disk2: stack1 -> stack2
disk1: stack0 -> stack2'''
        self.assertEqual(gold, str(self.game))

if __name__ == '__main__':
    unittest.main()

