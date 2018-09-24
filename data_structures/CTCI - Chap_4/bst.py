import unittest


class Node:
    """
    Represents the node of the tree
    """

    def __init__(self, data):
        self.left = self.right = None
        self.data = data

    def __str__(self):
        return str(self.data)


class BinarySearchTree:
    """
    Binary Search tree implementation
    """

    def __init__(self):
        self.root = None
        self.size = 0

    def pre_order(self, root, pre):
        """
        Returns a pre-order traversal of the tree
        :param root: root of the tree
        :param pre: list ot which the elements will be added too
        :return: list of the elements in pre-order traversal
        """
        if not root:
            return list()
        pre.append(root.data)
        if root.left:
            self.pre_order(root.left, pre)
        if root.right:
            self.pre_order(root.right, pre)
        return pre

    def post_order(self, root, post):
        """
       Returns a post-order traversal of the tree
       :param root: root of the tree
       :param post: list ot which the elements will be added too
       :return: list of the elements in post-order traversal
       """
        if not root:
            return list()
        if root.left:
            self.post_order(root.left, post)
        if root.right:
            self.post_order(root.right, post)
        post.append(root.data)
        return post

    def __str__(self):
        """
        Represents the pre-order string representation of the BST
        :return:
        """
        return ' -> '.join(str(item) for item in self.preorder(self.root, list()))

    def insert(self, value):
        """
        Delete to a private insert function which inserts a node recursively
        :param value:
        :return: inserted value
        """
        self.root = self._insert(self.root, value)

    def _insert(self, root, value):
        """
        Insert a value into the tree
        :param root: Root of the BST
        :param value: to be inserted into the tree
        :return: root of the tree
        """
        if not root:
            self.size += 1
            return Node(value)

        if value < root.data:
            root.left = self._insert(root.left, value)
        if value > root.data:
            root.right = self._insert(root.right, value)
        return root

    def __len__(self):
        """
        Returns the length of the tree in constant time
        :return:
        """
        return self.size

    def height(self):
        """
        O(N) - Needs to visit all the nodes to calculate the height
        Returns the heiht of the tree
        :return: height of the tree
        """
        return self._height(self.root)

    def _height(self, root):
        if root is None or (root.left is None and root.right is None):
            return 0
        return 1 + max(self._height(root.left), self._height(root.right))


class TestBinarySearchTree(unittest.TestCase):

    def setUp(self):
        self.bst = BinarySearchTree()

    def test_insert(self):
        self.bst.insert(15)
        self.bst.insert(13)
        self.bst.insert(17)
        self.bst.insert(10)
        self.bst.insert(16)
        self.bst.insert(18)
        self.assertEqual(6, len(self.bst))

    def test_pre_order(self):
        self.bst.insert(15)
        self.bst.insert(13)
        self.bst.insert(17)
        self.bst.insert(10)
        self.bst.insert(16)
        self.bst.insert(18)
        pre = self.bst.pre_order(self.bst.root, list())
        self.assertEqual([15, 13, 10, 17, 16, 18], pre)

    def test_post_order(self):
        self.bst.insert(15)
        self.bst.insert(13)
        self.bst.insert(17)
        self.bst.insert(10)
        self.bst.insert(16)
        self.bst.insert(18)
        post = self.bst.post_order(self.bst.root, list())
        self.assertEqual([10, 13, 16, 18, 17, 15], post)

    def test_height(self):
        self.bst.insert(15)
        self.bst.insert(13)
        self.bst.insert(17)
        self.bst.insert(10)
        self.bst.insert(16)
        self.bst.insert(11)
        self.assertEqual(3, self.bst.height())
