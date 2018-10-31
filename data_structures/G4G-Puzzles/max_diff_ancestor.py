"""
Given a binary tree, find the maximum difference between a node and its ancestor
"""
import unittest
from node import Node

ans = -1


def max_diff_ancestor(root):
    if not root:
        return 0
    if not root.left and not root.right:
        return root.data  # Leaf node's value is minimum as it does not have any descendants
    val = min(max_diff_ancestor(root.left), max_diff_ancestor(root.right))
    global ans
    ans = max(ans, root.data - val)
    return min(root.data, val)


class TestMaxDiff(unittest.TestCase):
    def setUp(self):
        self.root = Node(8)
        self.root.left = Node(3)
        self.root.left.left = Node(1)
        self.root.left.right = Node(6)

        self.root.right = Node(10)

    def test_max_diff(self):
        max_diff_ancestor(self.root)
        self.assertEqual(ans, 7)
