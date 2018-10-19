"""
Tl and T2 are two very large binary trees, with Tl much bigger than T2. Create an
algorithm to determine ifT2 is a subtree of Tl.
A tree T2 is a subtree of Tl if there exists a node n in Tl such that the subtree of n is identical to T2.
That is, if you cut off the tree at node n, the two trees would be identical
"""
import unittest
from binary_tree import Node


def is_subtree_preorder(root_t1, root_t2):
    """
    Perform a pre-order traversal of the trees and check if T2's pre-order traversal
    is a substring of T1's pre-order traversal
    :param root_t1: T1's root
    :param root_t2: T2's root
    :return: True if T2 is a subtree of T1, False otherwise
    """
    if not root_t1 or not root_t2:
        return False
    t1 = []
    t2 = []
    preorder(root_t1, t1)
    preorder(root_t2, t2)
    t1_str = ''.join(str(item) for item in t1)
    t2_str = ''.join(str(item) for item in t2)

    return t1_str.find(t2_str) != -1


def preorder(root, p_list):
    if not root:
        p_list.append('X')
        return
    p_list.append(root.data)
    preorder(root.left, p_list)
    preorder(root.right, p_list)


def is_subtree(root_t1, root_t2):
    """
    Check if the t2 is a subtree of t1
    :param root_t1: root of t1
    :param root_t2: root of t2
    :return: True if t2 is a subtree of t1, False otherwise
    """
    # An empty tree is always a subtree
    if not root_t2:
        return True

    return subtree(root_t1, root_t2)


def subtree(t1, t2):
    if not t1 or not t2:
        return False

    # For every t2's root found in t1, call matchTree for that subtree
    for t2_root in find_root(t1, t2):
        if match_tree(t2_root, t2):
            return True

    return False


def find_root(t1, t2):
    if not t1:
        yield None
    if t1.data == t2.data:
        yield t1

    if t1.left:
        for item in find_root(t1.left, t2):
            yield item
    if t1.right:
        for item in find_root(t1.right, t2):
            yield item


def match_tree(t1, t2):
    if t1 and not t2 or t2 and not t1:
        return False
    if not t1 and not t2:
        return True
    if t1.data != t2.data:
        return False
    return match_tree(t1.left, t2.left) and match_tree(t1.right, t2.right)


class TestIsSubtree(unittest.TestCase):

    def setUp(self):
        """
    T2:
          10
        /    \
      4       6
       \
        30
    T1:
          26
        /   \
      10     3
    /    \     \
  4       6      4
   \
    30
        :return:
        """
        self.t1 = Node(26)
        self.t1.left = Node(10)
        self.t1.left.left = Node(4)
        self.t1.left.left.right = Node(30)
        self.t1.left.right = Node(6)
        self.t1.right = Node(3)
        self.t1.right.right = Node(4)

        # Construct T2
        self.t2 = Node(10)
        self.t2.left = Node(4)
        self.t2.left.right = Node(30)
        self.t2.right = Node(6)

    def test_is_subtree_preorder(self):
        self.assertTrue(is_subtree_preorder(self.t1, self.t2))
        self.assertFalse(is_subtree_preorder(self.t2, self.t1))

    def test_is_subtree(self):
        self.assertTrue(is_subtree(self.t1, self.t2))
        self.assertFalse(is_subtree(self.t2, self.t1))
        self.assertTrue(is_subtree(self.t1, None))
