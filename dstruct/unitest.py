import unittest

from basic import stackmod
from basic.stackclass import Stack
from basic import tuplestack
from basic import tail_class


class TestStringMethods(unittest.TestCase):

    def test_stackmod_1(self):
        stackmod.push('spam')
        stackmod.push(123)
        self.assertEqual(stackmod.top(), 123)

    def test_stackclass_1(self):
        x = Stack()
        x.push('spam')
        x.push(123)
        self.assertEqual(x.pop(), 123)

    def test_tuplestack(self):
        x = tuplestack.Stack()
        x.push('spam')
        x.push(123)
        self.assertEqual(x.pop(), 123)

    def test_tailclass(self):
        x = tail_class.Stack()
        x.push('spam')
        x.push(123)
        self.assertEqual(x.pop(), 123)

if __name__ == '__main__':
    unittest.main()