"""
In a given BST, find the number of nodes that lie between a certain range.
"""
import unittest

from node import Node


def nodes_in_range_inorder(root, lo, hi):
    """
    :param root: of the BST
    :param low: lower bound of the range
    :param hi: upper bound of the range
    :return: count of nodes
    :performance: O(N)
    """
    if not root:
        return 0
    count = 0
    if root.left:
        count += nodes_in_range_inorder(root.left, lo, hi)
    if root.right:
        count += nodes_in_range_inorder(root.right, lo, hi)
    if lo <= root.data <= hi:
        count += 1

    return count


def print_inorder(root, lo, hi, count=0):
    """
    Keep performing an inorder traversal and find the nodes that lie in between
    The Inorder traversal will normally take O(N) time but we can improve by not
    going down the tree when we find that the elements are already out of range.
    Worst - O(N)
    Average - O(max(depth(elem < lo), depth(elem > max))
    """
    if not root:
        return count
    # As this is an inorder traversal, we can stop when we see an element lesser than the lo
    if root.data < lo:
        return count
    count = print_inorder(root.left, lo, hi, count) if root.left else count
    if lo <= root.data <= hi:
        count += 1
    # As this is an inorder traversal, we can stop when we see an element greater than the hi
    if root.data > hi:
        return count
    count = print_inorder(root.right, lo, hi, count) if root.right else count
    return count


class TestNodesInRange(unittest.TestCase):
    def setUp(self):
        self.root = Node(10)
        self.root.left = Node(5)
        self.root.left.left = Node(1)
        self.root.right = Node(50)
        self.root.right.left = Node(40)
        self.root.right.right = Node(100)

    def test_nodes_in_range_inorder(self):
        # self.assertEqual(3, nodes_in_range_inorder(self.root, 5, 45))
        self.assertEqual(print_inorder(self.root, 5, 45), 3)
