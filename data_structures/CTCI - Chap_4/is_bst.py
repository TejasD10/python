"""
Check if the tree is a BST
"""
from binary_tree import Tree
import sys
import unittest


class BSTTree(Tree):
    """
    Inherits from the Binary Tree and adds an additional method to check if
    the tree is a Binary Search Tree
    """

    def is_bst(self, root, node_min=-sys.maxsize, node_max=sys.maxsize):

        """
        Check if the tree is balanced
        :param node_max: Max value that this node can have
        :param node_min: Min value that this node can have
        :param root: root of the tree
        :return: True if the tree is balanced, False otherwise
                        8
                4              10
            2       5             6
        """
        # Base Case
        if not root:
            return True
        if (root.left and root.data <= root.left.data) or root.data > node_max:
            return False
        if (root.right and root.data >= root.right.data) or root.data < node_min:
            return False
        return self.is_bst(root.left, node_min=node_min, node_max=root.data - 1) and (
            self.is_bst(root.right, node_min=root.data + 1, node_max=node_max))


class TestTree(unittest.TestCase):
    def setUp(self):
        self.tree = BSTTree()

    def test_bst(self):
        self.tree.add_root(8)
        self.tree.add_left(8, 4)
        self.tree.add_right(8, 10)
        self.tree.add_left(4, 2)
        self.tree.add_right(4, 5)
        # self.tree.add_left(10, 13)
        self.tree.add_right(10, 6)
        self.assertFalse(self.tree.is_bst(self.tree.root))
