import unittest

from LinkedList import LinkedList


def is_palindrome(l_list):
    """
    Check if the provided Linked List is a palindrome list or not
    :param l_list: Linked List
    :return: True if the linked list is a palindrome, False otherwise
    """
    if not l_list or l_list.empty():
        return False

    new_list = l_list.clone_reverse(l_list)

    list1 = l_list.head()
    list2 = new_list.head()
    for i in range(len(new_list) // 2):
        if not list1 == list2:
            return False
        list1 = list1.next()
        list2 = list2.next()

    return True


def is_palindrome_stack(l_list: LinkedList):
    """
    Implement the algorithm to check if the linked list is a palindrome using a stack
    Use the Fast Pointer, Slow pointer technique to insert the first half of the list in the stack,
    pop an item off the stack and traverse through the remaining list to see if they match.
    1 -> 2 -> 3 -> 4 -> 3 -> 2 -> 1 - True
    1 -> 2 -> 3 -> 4 -> 4 -> 3 -> 2 -> 1 - True
    :param l_list: Linked list
    :return: True if the list is a palindrome, False otherwise
    """
    if not l_list or l_list.empty():
        return False
    # Traverse through the first half of the list and add to the stack
    stack = []
    slow = l_list.head()
    fast = l_list.head()

    while fast and fast.next():
        stack.append(slow.value())
        slow = slow.next()
        fast = fast.next().next()

    if fast:  # If there are odd number of elements in the list, the fast pointer is not null
        slow = slow.next()
    # Start popping from the stack and compare against the remaining elements in the list using the slow pointer
    while slow:
        item = stack.pop()
        if not item == slow.value():
            return False
        slow = slow.next()

    return True


def is_palindrome_recurse(head, length):
    """
    Check if the list is a palindrome using a recursive technique where each ith node is compared with the n-ith node in the list
    1- > 2 -> 3 -> 4 -> 3 -> 2 -> 1
    :param head: Linked List to be compared
    :param length: length of the list
    :return: A tuple of whether the linked list is a palindrome and the node with which the head needs to be compared to
    """
    if length == 0:  # Reached the middle of the list
        return head, True
    elif length == 1:
        return head.next(), True  # Odd number of elements so return the next element.

    node, res = is_palindrome_recurse(head.next(), length - 2)

    if not res:
        return node, False

    return node.next(), node.value() == head.value()


class TestPalindromeList(unittest.TestCase):
    """
    Test cases for a Palindrome Linked List
    """

    _list_true = LinkedList()
    _list_true.add_last(1)
    _list_true.add_last(2)
    _list_true.add_last(3)
    _list_true.add_last(4)
    _list_true.add_last(3)
    _list_true.add_last(2)
    _list_true.add_last(1)

    _list_false = LinkedList()
    _list_false.add_last(1)
    _list_false.add_last(2)
    _list_false.add_last(3)
    _list_false.add_last(4)
    _list_false.add_last(5)

    def test_palindrome(self):
        _, res = is_palindrome_recurse(self._list_true.head(), len(self._list_true))
        self.assertTrue(res)

    def test_not_palindrome(self):
        _, res = is_palindrome_recurse(self._list_false.head(), len(self._list_false))
        self.assertFalse(res)


if __name__ == '__main__':
    unittest.main()
