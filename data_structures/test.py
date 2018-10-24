class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

    def __str__(self):
        return str(self.data)


def insert(root, values):
    for value in values:
        root = _insert(root, value)
    return root


def _insert(root, value):
    if not root:
        return Node(value)
    if value < root.data:
        root.left = _insert(root.left, value)
    elif value >= root.data:
        root.right = _insert(root.right, value)

    return root


def bstDistance(values, n, node1, node2):
    if n == 0:
        return -1
    # Create the BST

    root = insert(None, values)

    # Find the distance.
    path1 = []
    find_node(root, path1, node1)

    path2 = []
    find_node(root, path2, node2)

    if not path1 or not path2:
        return -1

    i = 0
    while i < len(path1) and i < len(path2):
        if path1[i] != path2[i]:
            break
        i += 1

    return len(path1) + len(path2) - (2 * i)


def bst_distance(values, node1, node2):
    if len(values) == 0:
        return -1
    # Insert the values into the tree
    root = insert(None, values)

    return _bst_distance_helper(root, node1, node2)


def _bst_distance_helper(root, node1, node2):
    if not root:
        return 0
    dist = 0
    if root.data == node1 or root.data == node2:
        return dist + 1

    dist += _bst_distance_helper(root.left, node1, node2)
    dist += _bst_distance_helper(root.right, node1, node2)
    return dist


def find_node(root, path, value):
    if not root:
        return False

    path.append(root.data)

    if root.data == value:
        return True

    if (root.left and find_node(root.left, path, value)) or (root.right and find_node(root.right, path, value)):
        return True

    path.pop()
    return False


if __name__ == '__main__':
    # print(bstDistance([5, 6, 3, 1, 2, 4], 6, 2, 4))
    print(bst_distance([5, 6, 3, 1, 2, 4], 2, 4))
