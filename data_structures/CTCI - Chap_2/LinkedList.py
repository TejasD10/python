from random import randint
import unittest


class LinkedList:
    """
    Implementation of a singly linked list
    """
    class _Node:

        def __init__(self, element, next=None):
            self._element = element
            self._next = next

        def __str__(self):
            return str(self._element)

        def next(self):
            return self._next

        def value(self):
            return self._element

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __iter__(self):
        current = self._head
        while current:
            yield current
            current = current._next

    def __str__(self):
        """
        :return: List representation of a Linked list
        """
        # We can use the below syntax as we have defined __iter__ in which is a generator
        #
        values = [str(node) for node in self]
        return ' -> '.join(values)

    def __len__(self):
        """
        Return the size of the linked list
        :return:
        """
        return self._size

    def add_last(self, value):
        """
        Add a node to the end of the linked list
        :param value:
        :return: Added element
        """
        newest = self._Node(value)
        if not self._head:
            self._head = self._tail = newest
            self._size += 1
            return value

        self._tail._next = newest
        self._tail = newest
        self._size += 1
        return value

    def add_first(self, value):
        """
        Add to the head of the list
        :return: added value
        """
        self._head = self._Node(value, self._head)
        self._size += 1

    def add_to_list(self, values):
        for v in values:
            self.add_last(v)

    def generate_list(self, n, min_value=1, max_value=100):
        """
        Generate a linked list of n items in the range of min_value and max_value
        :param n: Number of items to be added in the list
        :param min_value: The values in the list should be greater than min_value
        :param max_value: The values in the list should be greater than max_value
        :return: this list
        """
        self._head = self._tail = None  # Reset the linked list
        for i in range(n):
            self.add_last(randint(min_value, max_value))

        return self

    def head(self):
        return self._head

    def tail(self):
        return self._tail


class TestLinkedList(unittest.TestCase):
    """
    Test Cases for Linked List Class
    """
    def test_add_last(self):
        l_list = LinkedList()
        l_list.add_last(10)
        l_list.add_last(20)
        l_list.add_last(30)
        print(str(l_list))
        self.assertEqual(len(l_list), 3)

    def test_add_first(self):
        l_list = LinkedList()
        l_list.add_first(30)
        l_list.add_first(20)
        l_list.add_first(10)
        print(str(l_list))
        self.assertEqual(len(l_list), 3)


if __name__ == '__main__':
    unittest.main()