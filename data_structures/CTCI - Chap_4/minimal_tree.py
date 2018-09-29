import unittest
from is_bst import BSTTree
from binary_tree import Node


def minimal_tree(inp_array):
    """
    Given a sorted array, convert it into a Minimal BST
    :param inp_array: Sorted input array
    :return: Reference to the root node of the tree, None if the array is empty
    """
    if len(inp_array) == 0:
        return None

    return minimal_tree_helper(inp_array, 0, len(inp_array) - 1)


def minimal_tree_helper(inp_array, start, end):
    """
    Recursively create a minimal tree, inserting the middle node as the root, left ones of the middle node
    to the left of the node and right one's to the right of the root node
    1 2 3 4 5 6 7
    :param inp_array: array
    :param start: start index of this array
    :param end: end index of this array
    :return: root of the tree
    """
    if start > end:
        return None

    mid = (start + end) // 2
    node = Node(inp_array[mid])
    node.left = minimal_tree_helper(inp_array, start, mid - 1)
    node.right = minimal_tree_helper(inp_array, mid + 1, end)

    return node


class TestMinimalTree(unittest.TestCase):
    def setUp(self):
        self.inp_array = [1, 2, 3, 4, 5, 6, 7]
        # Test if the created tree is a BST
        self.tree = BSTTree()

    def test_minimal_tree(self):
        root = minimal_tree(self.inp_array)
        self.assertTrue(self.tree.is_bst_inorder(root))

