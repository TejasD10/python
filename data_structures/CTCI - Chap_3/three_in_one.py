"""
Describe how you could use a single array to implement three stacks
"""
import unittest


class MultiStack:

    def __init__(self, capacity):
        self.num_stacks = 3
        self.stack_capacity = capacity
        self.values = [0] * (self.num_stacks * capacity)
        self.sizes = [0] * self.num_stacks

    def push(self, stack_number, item):
        """
        Push the element on the given stack
        :param stack_number: stack to which the item should be pushed
        :return: Item that is pushed on the stack, None otherwise
        :raises: Exception if the stack is full or invalid stack is referenced
        """
        if not self.valid_stack(stack_number):
            raise Exception('Stack number greater than the available stacks')

        if self.is_full(stack_number):
            raise Exception('Stack is full')

        self.values[self.index_of_top(stack_number) + 1] = item
        self.sizes[stack_number] += 1

        return item

    def pop(self, stack_number):
        """
        Pop an item off the provided stack
        :param stack_number: Stack in question
        :return: Popped item
        :raises: Exception if the stack is empty or invalid stack is referenced
        """

        if not self.valid_stack(stack_number):
            raise Exception('Stack number greater than the available stacks')

        if self.is_empty(stack_number):
            raise Exception('Stack is empty')

        item = self.values[self.index_of_top(stack_number)]
        self.sizes[stack_number] -= 1

        return item

    def peek(self, stack_number):
        """
        Peek the TOS item from the stack
        :param stack_number: Stack in question
        :return: Peeked item
        :raises: Exception if the invalid stack number is referenced
        """
        if not self.valid_stack(stack_number):
            raise Exception('Stack number greater than the available stacks')

        if self.is_empty(stack_number):
            raise Exception('Stack is empty')

        item = self.values[self.index_of_top(stack_number)]
        return item

    def index_of_top(self, stack_num):
        """
        Return the top of stack index for the stack number
        :param stack_num:
        :return: Index of the TOS
        """
        if not self.valid_stack(stack_num):
            raise Exception('Stack number greater than the available stacks')
        offset = stack_num * self.stack_capacity
        size = self.sizes[stack_num]
        return offset + size - 1

    def valid_stack(self, stack_num):
        """
        Return if the stack number is in the valid number of stacks
        :param stack_num: The stack number to be validated
        :return: True if the stack number is valid, False otherwise
        """
        if stack_num > self.num_stacks:
            return False
        return True

    def is_full(self, stack_number):
        """
        Check if stack_number is full
        :param stack_number: stack in question
        :return:
        """
        if not self.valid_stack(stack_number):
            raise Exception('Stack number greater than the available stacks')

        return self.sizes[stack_number] == self.stack_capacity

    def is_empty(self, stack_number):
        """
        Check if the stack_number is empty
        :param stack_number: stack in question
        :return:
        """
        if not self.valid_stack(stack_number):
            raise Exception('Stack number greater than the available stacks')

        return self.sizes[stack_number] == 0


class TestMultiStack(unittest.TestCase):

    def setUp(self):
        self.stacks = MultiStack(3)

    def test_insert_item_on_stack(self):
        self.assertIsNotNone(self.stacks.push(0, 10))
        self.assertIsNotNone(self.stacks.push(0, 20))
        self.assertIsNotNone(self.stacks.push(0, 30))

    def test_stack_is_full(self):
        self.assertIsNotNone(self.stacks.push(0, 10))
        self.assertIsNotNone(self.stacks.push(0, 20))
        self.assertIsNotNone(self.stacks.push(0, 30))
        self.assertTrue(self.stacks.is_full(0))

    def test_stack_is_empty(self):
        self.assertTrue(self.stacks.is_empty(0))

    def test_peek_on_stack(self):
        self.assertIsNotNone(self.stacks.push(0, 10))
        self.assertIsNotNone(self.stacks.push(0, 20))
        self.assertIsNotNone(self.stacks.push(0, 30))
        self.assertEqual(30, self.stacks.peek(0))
