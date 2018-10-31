import unittest


class Node:
    """
    Object that represents each node in the linked list
    """

    def __init__(self, value):
        self.data = value
        self.next = None

    def __str__(self):
        return str(self.data)


def delete_kth_node(head, k):
    if not head:
        return
    if k == 1:
        return None
    if k == 0:
        return head
    # 1 > 2 > 3 > 4 > 5 > 6 > 7 > 8
    temp = head
    prev = head
    counter = k
    while temp:
        prev = temp
        temp = temp.next
        counter -= 1
        if counter == 1 and temp:
            prev.next = temp.next
            temp = prev.next
            counter = k


class TestDeleteKthNode(unittest.TestCase):
    def setUp(self):
        # Create the linked list
        self.head = self.tail = None
        values = [1, 2, 3, 4, 5, 6, 7]
        self.insert(values)

    def insert(self, values):
        for item in values:
            if not self.head:
                self.head = Node(item)
                self.tail = self.head
            else:
                self.tail.next = Node(item)
                self.tail = self.tail.next

    def test_delete_kth_node(self):
        delete_kth_node(self.head, 3)
        list_nodes = self.convert_to_list(self.head)
        self.assertEqual([1, 2, 4, 5, 7], list_nodes)

    def convert_to_list(self, head):
        if not head:
            return []
        temp = head.next
        result = [head.data]
        while temp:
            result.append(temp.data)
            temp = temp.next
        return result
