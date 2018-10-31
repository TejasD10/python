import unittest


def longest_substring(string):
    """
    dvdf
    :param string:
    :return:
    """
    if not string:
        return 0
    if len(string) == 1:
        return 1
    # Stores the last index at which the character was seen

    hist = {}
    max_len = 0
    start = 0
    for i, ch in enumerate(string):
        # Check when the character was last found, and mark it as a start of the new sub string.
        if ch in hist and hist[ch] >= start:
            start = hist[ch] + 1

            # Insert the character in the map
        hist[ch] = i

        max_len = max(max_len, i - start + 1)
    return max_len


class TestLongestString(unittest.TestCase):
    def test_longest_substring(self):
        self.assertEqual(longest_substring('aabaab!bb'), 3)
