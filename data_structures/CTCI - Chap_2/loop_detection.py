import unittest


class Node:
    """
    A Node class to create cycles manually and is used in writing the test cases
    """

    def __init__(self, element):
        self._element = element
        self._next = None

    def __str__(self):
        return str(self._element)

    def next(self):
        return self._next

    def value(self):
        return self._element


def find_cycle(l_list):
    """
    Detects if there is a cycle in the list, if so, returns the node at which the cycle starts.
    Uses the Floyd's algorithm a.k.a the fast and the slow pointer technique to identify the cycle
    :param l_list: Linked List
    :return: None or the node at which the cycle starts
    """
    if not l_list:
        return False

    fast = l_list
    slow = l_list

    while fast and fast.next():
        fast = fast.next().next()
        slow = slow.next()
        if fast is slow:
            break

    if fast is None or fast.next() is None:
        return None

    # Now, knowing that the distance to start of the loop from the head
    # and the collision are the same, we can set the slow to
    # head and move both lists until they collide which will be our start of the loop cycle
    slow = l_list

    while slow is not fast:
        slow = slow.next()
        fast = fast.next()

    return fast


class TestLoopDetection(unittest.TestCase):
    """
    Unit Test Cases for checking and finding the cycles in the list
    """
    # List with cycles
    head = Node(1)
    head._next = (Node(2))
    head.next()._next = (Node(3))
    head.next().next()._next = (Node(4))
    head.next().next().next()._next = head.next()

    head2 = Node(1)
    head2._next = (Node(2))
    head2.next()._next = (Node(3))
    head2.next().next()._next = (Node(4))

    def test_print(self):
        """
        Test to print the list
        :return: None
        """
        print(self.head.value(), end=" -> ")
        print(self.head.next().value(), end=" -> ")
        print(self.head.next().next().value(), end=" -> ")
        print(self.head.next().next().next().value(), end=" -> ")
        print(self.head.next().next().next().next().value(), end="")

    def test_find_cycle(self):
        """
        Test which identifies the presence of absence of a cycle in list
        :return:
        """
        self.assertIsNotNone(find_cycle(self.head))
        self.assertIsNone(find_cycle(self.head2))


if __name__ == '__main__':
    unittest.main()
