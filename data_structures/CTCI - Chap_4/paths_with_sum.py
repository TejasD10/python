"""
You are given a binary tree in which each node contains an integer value (which
might be positive or negative). Design an algorithm to count the number of paths that sum to a
given value. The path does not need to start or end at the root or a leaf, but it must go downwards
(traveling only from parent nodes to child nodes).
           1
        /     \
      3        -1
    /   \     /   \
   2     1   4     5
        /   / \     \
       1   1   2     6
"""
import unittest
from binary_tree import Node


def sum_of_paths_rec(root, target_sum):
    if not root:
        return 0

    counts_from_root = _sum_helper(root, target_sum, 0)

    left_count = sum_of_paths_rec(root.left, target_sum)
    right_count = sum_of_paths_rec(root.right, target_sum)

    return counts_from_root + left_count + right_count


def _sum_helper(root, target_sum, curr_sum):
    """
            1
        /     \
      3        -1
    /   \     /   \
   2     1   4     5
        /   / \     \
       1   1   2     6
    """
    if not root:
        return 0

    # Check if we found the target sum
    curr_sum += root.data
    count_of_paths = 0
    if curr_sum == target_sum:
        count_of_paths += 1

    count_of_paths += _sum_helper(root.left, target_sum, curr_sum) \
                      + _sum_helper(root.right, target_sum, curr_sum)
    return count_of_paths


def sums_of_path_memo(root, target_sum):
    if not root:
        return
    return _sum_helper_memo(root, target_sum, 0, {})


def _sum_helper_memo(root, target_sum, current_sum, path_count):
    """
           1
        /     \
      3        -1
    /   \     /   \
   2     1   4     5
        /   / \     \
       1   1   2     6

    """
    if not root:
        return 0

    current_sum += root.data
    sum = current_sum - target_sum
    total_paths = path_count.get(sum, 0)

    if current_sum == target_sum:
        total_paths += 1

    increment_path_count(path_count, current_sum, 1)
    total_paths += _sum_helper_memo(root.left, target_sum, current_sum, path_count)
    total_paths += _sum_helper_memo(root.right, target_sum, current_sum, path_count)
    increment_path_count(path_count, current_sum, -1)

    return total_paths


def increment_path_count(path_count, current_sum, delta):
    new_count = path_count.get(current_sum, 0) + delta
    if new_count == 0:
        path_count.pop(current_sum)
    else:
        path_count[current_sum] = new_count


class TestSumsofPath(unittest.TestCase):
    def setUp(self):
        self.root = Node(1)
        self.root.left = Node(3)
        self.root.left.left = Node(2)
        self.root.left.right = Node(1)
        self.root.left.right.left = Node(1)

        self.root.right = Node(-1)
        self.root.right.left = Node(4)
        self.root.right.left.left = Node(1)
        self.root.right.left.right = Node(2)
        self.root.right.right = Node(5)
        self.root.right.right.right = Node(6)

    def test_sums_of_path(self):
        result = sum_of_paths_rec(self.root, 5)
        self.assertEqual(8, result)

    def test_sums_of_path_memo(self):
        result = sums_of_path_memo(self.root, 5)
        self.assertEqual(8, result)
