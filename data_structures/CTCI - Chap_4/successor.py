import unittest


class Node:
    """
    Node class with a pointer to its parent
    """

    def __init__(self, data):
        self.left = self.right = self.parent = None
        self.data = data

    def __str__(self):
        return f'{self.data}'


def successor(root, data):
    """
    Return the in-order successor of the node containing the data
    :param data: value contained in the node
    :return: the inorder successor of the node, None otherwise
    """
    if not root:
        return

    # Find the node containing the data
    node = search(root, data)
    # Return if the element is not present in the tree
    if not node:
        return

    # First, if the node contains a right child, the in-order successor
    # is the left most child in the right subtree of the child.
    if node.right:
        # Find the smallest node in the left subtree of the child
        r_child = node.right
        while r_child.left:
            r_child = r_child.left
        return r_child.data
    else:
        parent = node.parent
        child = node
        while parent and parent.right is child:
            child = parent
            parent = child.parent

        return parent.data if parent else parent


def search(root, data):
    """
    From the root of the tree, search and return the reference to the node containing the data
    :param root: root of the tree to begin searching from
    :param data: data to be searched in the tree
    :return: Reference to the node containing data
    """
    if not root:
        return None
    # Check if the root node is the node containing the data
    if root.data == data:
        return root
    if data < root.data:  # Go left
        return search(root.left, data)
    else:
        return search(root.right, data)


class TestSuccessor(unittest.TestCase):
    def setUp(self):
        """
        Setup the tree for executing test cases
                    20
            8               22
        4       12
            10      14
        """
        self.root = Node(20)
        self.root.left = Node(8)
        self.root.left.parent = self.root
        self.root.left.left = Node(4)
        self.root.left.left.parent = self.root.left
        self.root.left.right = Node(12)
        self.root.left.right.parent = self.root.left
        self.root.left.right.left = Node(10)
        self.root.left.right.left.parent = self.root.left.right
        self.root.left.right.right = Node(14)
        self.root.left.right.right.parent = self.root.left.right
        self.root.right = Node(22)
        self.root.right.parent = self.root

    def test_successor(self):
        self.assertEqual(successor(self.root, 8), 10)
        self.assertEqual(successor(self.root, 10), 12)
        self.assertEqual(successor(self.root, 14), 20)
        self.assertIsNone(successor(self.root, 22))
