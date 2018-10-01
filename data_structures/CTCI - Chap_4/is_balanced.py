import unittest

from binary_tree import Node


def height(root):
    """
    Return the maximum height of the tree
    :param root:
    :return:
               8
         4          10
     2       5            6

    """
    if not root:
        return 0
    return 1 + max(height(root.left), height(root.right))


def is_balanced(root):
    """
    Implement a function to check if a binary tree is balanced. For the purposes of
    this question, a balanced tree is defined to be a tree such that the heights of the two subtrees of any
    node never differ by more than one.
    :param root: root of the tree
    :return: True if the tree is balanced, False otherwise
    """
    if not root:
        return True
    diff = height(root.left) - height(root.right)

    if abs(diff) > 1:
        return False
    else:
        return is_balanced(root.left) and is_balanced(root.right)


class TestBalancedTree(unittest.TestCase):
    def setUp(self):
        """
                        8
                 4          10
                                12
                                    14
                                        16
        """
        # Create a balanced tree for testing
        self.b_root = Node(8)
        self.b_root.left = Node(4)
        self.b_root.right = Node(10)
        self.b_root.left.left = Node(2)
        self.b_root.left.right = Node(5)
        self.b_root.right.right = Node(6)

        # Create an unbalanced tree
        self.ub_root = Node(8)
        self.ub_root.left = Node(4)
        self.ub_root.right = Node(10)
        self.ub_root.right.right = Node(12)
        self.ub_root.right.right.right = Node(14)
        self.ub_root.right.right.right.right = Node(16)

    def test_is_balanced(self):
        self.assertTrue(is_balanced(self.b_root))
        self.assertFalse(is_balanced(self.ub_root))
