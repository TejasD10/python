import unittest


class Node:
    """
    Node class with a pointer to its parent node
    """

    def __init__(self, data):
        self.left = self.right = self.parent = None
        self.data = data

    def __str__(self):
        return str(self.data)


def remove_items(diff, node_list):
    if diff == 0:
        return
    for i in range(diff):
        node_list.pop(0)


def first_common_ancestor(root, v1, v2):
    """
    Return the first common ancestor of the nodes containing v1 and v2 in its data.
    :param v1: element 1 present in the tree
    :param v2: element 2 present in the tree
    :return: Value of the first common ancestor
    """
    if not root:
        return

    # Find the nodes in the tree
    node_v1 = search_list(root, v1)
    node_v2 = search_list(root, v2)

    # Remove the extra nodes from the path
    diff = abs(len(node_v1) - len(node_v2))
    remove_items(diff, node_v1 if len(node_v1) > len(node_v2) else node_v2)
    # One of the nodes not found
    if not node_v1 or not node_v2:
        return

    # Keep popping elements from the returned lists until you get the same element or
    # you run out of elements in one list
    while node_v1 and node_v2:
        if node_v1[0] == node_v2[0]:
            return node_v1[0]
        node_v1.pop(0)
        node_v2.pop(0)


def find_common_ancestor(root, v1, v2):
    """
    Find the common anecestor in a tree where the nodes does not have links to its parents
    :param root: root of the tree
    :param v1:
    :param v2:
    :return: Common ancestor of v1 and v2 if it exists, None otherwise
    """
    if not search(root, v1) or not search(root, v2):
        return
    return find_common_ancestor_rec(root, v1, v2)


def find_common_ancestor_rec(root, v1, v2):
    if not root:
        return

    if search(root.left, v1) and search(root.left, v2):
        return find_common_ancestor_rec(root.left, v1, v2)
    elif search(root.right, v1) and search(root.right, v2):
        return find_common_ancestor_rec(root.right, v1, v2)
    else:
        return root.data


def first_common_ancestor_opt(root, v1, v2):
    """
    :param root:
    :param v1:
    :param v2:
    :return:
    """
    # make sure both the nodes are in tree
    node_v1 = search(root, v1)
    node_v2 = search(root, v2)

    # If either node is not present, return None
    if not node_v1 or not node_v2:
        return

    # check if one node covers the other, if so return one
    if search(node_v1, v2):
        return v1
    if search(node_v2, v1):
        return v2

    # Traverse up the route from v1 and check if the sibling of the parent
    # has the node v2, in which case the parent will be the needed ancestor

    p = node_v1.parent
    child = node_v1

    while p:
        sib = sibling(p, child)
        if search(sib, v2):
            return p.data  # p is the ancestor
        child = p
        p = p.parent


def sibling(parent, child):
    """
    FInd the sibling of the parent which is not the child
    :param parent:
    :param child:
    :return:
    """
    if not parent or not child:
        return

    return parent.left if parent.left != child else parent.right


def search(root, v1):
    # search one of the nodes in the tree
    if not root:
        return

    if root.data == v1:
        return root

    return search(root.left, v1) or search(root.right, v1)


def search_list(root, v1):
    """
    Search for values v1 and v2 in the tree
    :param root: root of the tree to be searched
    :param v1: search the value v1
    :param v2: search the value v1
    :return: Reference to the nodes containing values v1 and v2
    """
    if not root:
        return

    if root.data == v1:
        return [root.data]
    left = search_list(root.left, v1)
    if left:
        left.append(root.data)
        return left
    right = search_list(root.right, v1)
    if right:
        right.append(root.data)
        return right


class TestFirstCommonAncestor(unittest.TestCase):
    def setUp(self):
        self.root = Node(1)
        self.root.left = Node(2)
        self.root.left.parent = self.root
        self.root.left.left = Node(4)
        self.root.left.left.parent = self.root.left
        self.root.left.right = Node(5)
        self.root.left.right.parent = self.root.left

        self.root.right = Node(3)
        self.root.right.parent = self.root
        self.root.right.left = Node(6)
        self.root.right.left.parent = self.root.right
        self.root.right.right = Node(7)
        self.root.right.right.parent = self.root.right

    def test_first_common_ancestor(self):
        self.assertEqual(2, first_common_ancestor(self.root, 4, 5))
        self.assertEqual(1, first_common_ancestor(self.root, 4, 6))
        self.assertEqual(1, first_common_ancestor(self.root, 4, 3))
        self.assertEqual(2, first_common_ancestor(self.root, 4, 2))

    def test_first_common_ancestor_opt(self):
        self.assertEqual(2, first_common_ancestor_opt(self.root, 4, 5))
        self.assertEqual(1, first_common_ancestor_opt(self.root, 4, 6))
        self.assertEqual(1, first_common_ancestor_opt(self.root, 4, 3))
        self.assertEqual(2, first_common_ancestor_opt(self.root, 4, 2))

    def test_find_common_ancestor_rec(self):
        self.assertEqual(2, find_common_ancestor(self.root, 4, 5))
        self.assertEqual(1, find_common_ancestor(self.root, 4, 6))
        self.assertEqual(1, find_common_ancestor(self.root, 4, 3))
        self.assertEqual(2, find_common_ancestor(self.root, 4, 2))
        self.assertIsNone(find_common_ancestor(self.root, 4, 8))
