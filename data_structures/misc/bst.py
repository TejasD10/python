class Node(object):
    """
    Container for the data to be stored in the binary search tree
    """
    def __init__(self, data):
        self.left = self.right = None
        self.data = data


class BinarySearchTree(object):
    """
    Binary Search tree will provide the functions to manipulate the tree
    """
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert(self.root, data)

    def _insert(self, root, data):
        if root is None:
            return Node(data)
        if data < root.data:
            root.left = self._insert(root.left, data)
        elif data > root.data:
            root.right = self._insert(root.right, data)
        return root

    def preorder(self, root):
        """
        Prints a space-seperated pre-order traversal of the tree
        :param root: Root of this tree
        :return: None
        """
        if root is None:
            return
        print(root.data, end=' ')
        self.preorder(root.left)
        self.preorder(root.right)

    def height(self, root):
        """
        Calculates the max height of the binary search tree
        :param root: of the tree
        :return: Max height of the tree -> int
        """
        if root is None:
            return 0
        leftheight = self.height(root.left)
        rightheight = self.height(root.right)
        return 1 + max(leftheight, rightheight)

    def getHeight(self, root):
        """
        Returns the max number of edges in the tree
        :param root: of the binary tree
        :return: Max edges in the tree -> int
        """
        if root is None:
            return 0
        height = max(self.getHeight(root.left), self.getHeight(root.right))
        if self.isInternal(root):
            return height
        else:
            return 1 + height

    def isInternal(self, root):
        if root.left is None and root.right is None:
            return True
        else:
            return False

    def levelorder(self, root):
        if not root:
            print('Empty tree')
        queue = list()
        queue.append(root)
        while queue:
            elem = queue.pop(0)
            print(elem.data, end=' ')
            if elem.left:
                queue.append(elem.left)
            if elem.right:
                queue.append(elem.right)



def main():
    """
    Driver of the program
    :return: None
    """
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(20)
    bst.insert(5)
    bst.insert(7)
    bst.insert(12)
    # bst.preorder(bst.root)
    # bst.getHeight(bst.root)
    bst.levelorder(bst.root)


if __name__ == '__main__':
    main()