import unittest

from exceptions import EmptyStackException


class Stack:
    """
    Implement a stack for use in the SetOfStacks class
    """

    def __init__(self):
        self.stack = []
        self.size = 0

    def push(self, item):
        """
        Push an item on the stack
        :param item: to be pushed on the stack
        :return: item
        """
        self.stack.append(item)
        self.size += 1

        return item

    def pop(self):
        """
        Pop an item of the stack
        :return: item popped off the stack
        :raises: Exception if the stack is empty
        """
        if self.is_empty():
            raise EmptyStackException("Stack is empty!")

        return self.stack.pop()

    def is_empty(self):
        """
        check if the stack is empty
        :return: True if the stack is empty, False otherwise
        """
        return self.size == 0

    def __str__(self):
        return ' -> '.join([str(item) for item in self.stack])

    def __len__(self):
        """
        Return the length of the stack
        :return: Length of the stack
        """
        return len(self.stack)


class SetOfStacks:
    """
    This class will leverage stacks and implement a set of stacks
    """

    def __init__(self, capacity):
        """
        Constructor for the SetOfStacks
        :param capacity: Individual stack's capacity
        """
        self.capacity = capacity
        self.stacks = []

    def push(self, item):
        """
        Push an item on the last stack in the stacks
        :param item: to be pushed
        :return: item pushed
        """
        # Check if this is the first item inserted in the stack

        stack = self.get_last_stack()
        assert stack is not None
        stack.push(item)

    def pop(self):
        """
        Pops an item from the last stack
        :return: Popped item
        :raises: EmptyStackException if the stack is empty
        """
        # No need to get the last stack if the len of stacks is 0
        if len(self.stacks) == 0:
            raise EmptyStackException('Nothing to pop!')

        stack = self.get_last_stack()
        assert stack is not None
        item = stack.pop()
        if len(stack) == 0:
            self.stacks.pop()

        return item

    def get_last_stack(self):
        """
        Return the last stack on the set of stacks to be used in the operation
        :return:
        """
        if len(self.stacks) == 0:
            # Create a new stack and add to the list of stacks
            st = Stack()
            self.stacks.append(st)
            return self.stacks[-1]

        last_stack = self.stacks[-1]
        if len(last_stack) == self.capacity:
            st = Stack()
            self.stacks.append(st)
            return self.stacks[-1]
        return last_stack

    def __len__(self):
        return len(self.stacks)


class TestSetOfStacks(unittest.TestCase):
    def setUp(self):
        self.stack_set = SetOfStacks(3)

    def push_elem(self):
        self.stack_set.push(10)
        self.stack_set.push(20)
        self.stack_set.push(30)
        self.stack_set.push(40)
        self.stack_set.push(50)

    def test_push(self):
        self.push_elem()
        self.assertEqual(len(self.stack_set), 2)

    def test_pop(self):
        self.push_elem()
        self.stack_set.pop()
        self.stack_set.pop()
        self.assertEqual(len(self.stack_set), 1)
