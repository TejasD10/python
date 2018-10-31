import unittest


class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

    def __str__(self):
        return str(self.data)


def add_last(new_list, ret_list):
    if not ret_list:
        new_list.next = None
        return

    temp = new_list
    while temp.next:
        temp = temp.next
    temp.next = ret_list


def rearrange(head):
    if not head:
        return

    temp = head
    new_list = None
    while temp:
        ret_list = _rearrange_helper(temp)
        if not new_list:
            new_list = ret_list
        else:
            add_last(new_list, ret_list)
        temp = temp.next

    return new_list


def _rearrange_helper(head):
    """
    This list should go to the last node and return the
    first and the last nodes
    """
    if not head:
        return

    if not head.next:
        return Node(head.data)

    new_list = Node(head.data)
    temp = head
    del_node = head
    while temp.next:
        del_node = temp
        temp = temp.next

    new_list.next = Node(temp.data)
    del temp
    del_node.next = None
    return new_list


class TestRearrangeList(unittest.TestCase):
    def setUp(self):
        self.head = Node(1)
        self.head.next = Node(2)
        self.head.next.next = Node(3)
        self.head.next.next.next = Node(4)
        self.head.next.next.next.next = Node(5)

    def test_rearrange(self):
        llist = rearrange(self.head)
        temp = llist
        while temp:
            print(temp.data, end=" -> ") if temp.next else print(temp.data)
            temp = temp.next
