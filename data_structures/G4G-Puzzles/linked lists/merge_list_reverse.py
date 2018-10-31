import unittest


class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

    def __str__(self):
        return str(self.data)


# class LinkedList:
#     def __init__(self):
#         self.head = self.tail = None


def merge_list_reverse(head1, head2):
    if not head1 and not head2:
        return
    temp1 = head1
    temp2 = head2
    new_list = None
    while temp1 or temp2:
        if not temp1 and temp2:
            node = Node(temp2.data)
            node.next = new_list
            temp2 = temp2.next
        elif not temp2 and temp1:
            node = Node(temp1.data)
            node.next = new_list
            temp1 = temp1.next
        elif temp1.data <= temp2.data:
            node = Node(temp1.data)
            node.next = new_list
            temp1 = temp1.next
        else:
            node = Node(temp2.data)
            node.next = new_list
            temp2 = temp2.next
        new_list = node
    return new_list


class TestMergeListsReverse(unittest.TestCase):
    def setUp(self):
        self.head1 = Node(5)
        self.head1.next = Node(10)
        self.head1.next.next = Node(15)
        self.head1.next.next.next = Node(40)

        self.head2 = Node(2)
        self.head2.next = Node(3)
        self.head2.next.next = Node(20)

    def test_merge_list_reverse(self):
        new_list = merge_list_reverse(self.head1, self.head2)
        self.assertEqual(self.create_list(new_list), [40, 20, 15, 10, 5, 3, 2])

    def create_list(self, root):
        if not root:
            return []
        result = []
        temp = root
        while temp:
            result.append(temp.data)
            temp = temp.next
        return result
