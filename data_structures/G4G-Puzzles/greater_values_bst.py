import unittest


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

    def __str__(self):
        return str(self.data)


def greater_values(root, sum=0):
    """
    Perform a reverse in-order traversal calculating the sum and
    returning it to the previous for use
    :param root:
    :param sum:
    :return:
    """
    if not root:
        return sum
    sum = greater_values(root.right, sum)

    sum += root.data
    root.data = sum

    sum =  greater_values(root.left, sum)

    return sum


def preorder(root):
    if not root:
        return
    lst = [int(str(root))]
    if root.left:
        lst.extend(preorder(root.left))
    if root.right:
        lst.extend(preorder(root.right))
    return lst


class TestGreaterValues(unittest.TestCase):
    def setUp(self):
        # Set up a tree
        self.root = Node(50)
        self.root.left = Node(30)
        self.root.left.left = Node(20)
        self.root.left.right = Node(40)

        self.root.right = Node(70)
        self.root.right.left = Node(60)
        self.root.right.right = Node(80)

    def test_greater_values(self):
        greater_values(self.root)
        self.assertEqual(preorder(self.root), [260, 330, 350, 300, 150, 210, 80])
