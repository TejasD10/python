import unittest


def magic_index(input):
    if not input or len(input) == 0:
        return
    return magic_index_helper(input, 0, len(input) - 1)


def magic_index_helper(input, low, high):
    if high < low:
        return -1
    mid = (low + high) // 2

    if input[mid] == mid:
        return mid
    if input[mid] < mid:
        # Branch right
        return magic_index_helper(input, mid + 1, high)
    else:
        return magic_index_helper(input, low, mid - 1)


class TestMagicIndex(unittest.TestCase):
    def setUp(self):
        self.input = [-40, -20, -1, 1, 2, 3, 5, 7, 9, 12, 13]

    def test_magic_index(self):
        self.assertEqual(magic_index(self.input), 7)
