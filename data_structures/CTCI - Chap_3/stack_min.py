"""
How would you design a stack which, in addition to push and pop, has a function min
which returns the minimum element? Push, pop and min should all operate in 0(1) time
"""
import unittest


class StackMin:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        self.size = 0

    def push(self, item):
        """
        Push an item to the stack
        :param item: to be added to the stack
        :return: item pushed on the stack
        """
        # First, push the item on stack
        self.stack.append(item)
        self.size += 1

        # Check if the min stack is empty, if so push the item on the stack
        if self.is_min_stack_empty():
            self.min_stack.append(item)
            return item

        # If the min stack is not empty, check if the TOS of the min_stack is greater than the item
        # if so, add the item on the min stack, which will be the new minimum

        if self.min_stack[-1] > item:
            self.min_stack.append(item)

        return item

    def pop(self):
        """
        Remove and return the top element in the list
        :return: Item popped off the list
        :raises: Exception if the stack is empty
        """
        if self.is_empty():
            raise Exception('Stack is empty!')

        # Pop the item off the stack and reduce the size by 1
        item = self.stack.pop()

        # check if the item is the min item, if so pop the element from the min stack too
        if not self.is_min_stack_empty():
            if self.min_stack[-1] == item:
                self.min_stack.pop()

        return item

    def min(self):
        """
        Return the minimum element of the stack in O(1) time
        :return: Min element from the stack
        """
        if self.is_min_stack_empty():
            raise Exception('Stack is empty!')

        return self.min_stack[-1]

    def is_min_stack_empty(self):
        return len(self.min_stack) == 0

    def is_empty(self):
        """
        Checks if the stack is empty
        :return: True is the stack is empty, False otherwise
        """
        return self.size == 0


class TestStackMin(unittest.TestCase):

    def setUp(self):
        self.stack = StackMin()

    def test_min_stack(self):
        self.stack.push(10)
        self.stack.push(12)
        self.stack.push(2)
        self.assertEqual(2, self.stack.min())

    def test_empty_stack(self):
        with self.assertRaises(Exception) as ex:
            self.stack.min()
