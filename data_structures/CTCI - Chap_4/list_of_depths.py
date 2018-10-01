import unittest

from binary_tree import Node


def list_of_depths(root):
    """
    Given a binary tree, design an algorithm which creates a linked list of all the nodes
    at each depth (e.g., if you have a tree with depth D, you'll have D linked lists).
    :param root: root of the tree
    :return: a reference to the list of lists
    """
    if not root:
        return None

    lists = list()
    _list_depths_helper(root, lists)
    return lists


def _list_depths_helper(root, lists, index=0):
    if not root:
        return
    if len(lists) == index:
        lists.append([root.data])
    else:
        lists[index].append(root.data)

    if root.left:
        _list_depths_helper(root.left, lists, index + 1)
    if root.right:
        _list_depths_helper(root.right, lists, index + 1)


class TestListOfDepths(unittest.TestCase):
    def setUp(self):
        """
        Create the tree to be traversed
                       8
                 4          10
             2       5            6
        """
        self.root = Node(8)
        self.root.left = Node(4)
        self.root.right = Node(10)
        self.root.left.left = Node(2)
        self.root.left.right = Node(5)
        self.root.right.right = Node(6)

    def test_lists_length(self):
        lists = list_of_depths(self.root)
        self.assertEqual(len(lists[0]), 1)
        self.assertEqual(len(lists[1]), 2)
        self.assertEqual(len(lists[2]), 3)
