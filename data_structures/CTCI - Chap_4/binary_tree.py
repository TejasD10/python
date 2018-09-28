"""
Implementation of a binary tree
"""
class Node:
    def __init__(self, value):
        self.left = self.right = None
        self.data = value

    def __str__(self):
        return str(self.data)


class Tree:

    def __init__(self):
        self.root = None

    def add_root(self, value):
        if not self.is_empty():
            raise Exception('Tree is not empty!')
        self.root = Node(value)

    def add_right(self, search, value):
        """
        Add as a right child of the node containing the value
        :param value: existing value of a node in the tree
        :return: Value that was added to the tree
        """
        if self.is_empty():
            raise Exception('Tree is empty!')
        node = self.search(search)
        if not node:
            raise Exception('Value not found!')
        if node.right:
            raise Exception('A value already present at the location')
        node.right = Node(value)
        return value

    def add_left(self, search, value):
        """
        Add as a left child of the node containing the value
        :param value: existing value of a node in the tree
        :return: Value that was added to the tree
        """
        # Search for the value in the tree
        if self.is_empty():
            raise Exception('Tree is empty!')
        node = self.search(search)
        if not node:
            raise Exception('Value not found!')
        if node.left:
            raise Exception('A value already present at the location')
        node.left = Node(value)
        return value

    def search(self, value):
        """
        Return a reference to the node containing the value in the tree
        :param value: to be found in the tree
        :return: Reference to the node containing the value
        """
        if self.is_empty():
            return None
        return self._search(self.root, value)

    def _search(self, root, value):
        if root is None:
            return None

        if root.data == value:
            return root

        left = self._search(root.left, value) if root.left else None
        if left:
            return left
        right = self._search(root.right, value) if root.right else None
        if right:
            return right

    def is_empty(self):
        return self.root is None

    def __iter__(self):
        if not self.root:
            return None
        for item in self.preorder(self.root):
            yield str(item)

    def preorder(self, root):
        yield root
        if root.left:
            for item in self.preorder(root.left):
                yield item
        if root.right:
            for item in self.preorder(root.right):
                yield item

    def __str__(self):
        return ' -> '.join(item for item in self)