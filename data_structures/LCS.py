import unittest


def longest_subsequence(s1, s2):
    """
    Determine the longest common subsequence in the strings s1 and s2
    :param s1: String
    :param s2: String
    :return: A Tuple of the length and the longest common subsequence.
    """
    # If one of the string is none, there is no common subsequence, hence return 0
    if not s1 or not s2:
        return 0

    # Create the matrix for use for tabulation
    result = [[0] * (len(s1) + 1) for _ in range(len(s2) + 1)]

    for row in range(1, len(result)):  # Iterate over the rows
        for col in range(1, len(result[0])):  # Iterate over the cols
            if s2[row - 1] == s1[col - 1]:  # If they are the same they are adding to the longest subsequence
                result[row][col] = 1 + result[row - 1][col - 1]
            else:
                result[row][col] = max(result[row - 1][col], result[row][col - 1])

    # Return the last element as the length of the longest common subsquence

    # Find the longest common subsequence
    lcs = []
    row = len(result) - 1
    col = len(result[0]) - 1
    while row and col:
        # Check if the value is same as the adjacent cells, if not it is coming from diagonals
        if result[row][col] != result[row - 1][col] and result[row][col] != result[row][col - 1]:
            lcs.append(s1[col - 1])
            col -= 1
            row -= 1
        elif result[row][col] == result[row][col - 1]:  # Matches the column
            col -= 1
        else:
            row -= 1
    return ''.join(str(i) for i in reversed(lcs)), result[len(s2)][len(s1)]


class TestLongestCommonSubsequence(unittest.TestCase):
    def test_longest_subsequence(self):
        lcs, length = longest_subsequence('abcdaf', 'acbcf')
        self.assertEqual(length, 4)
        self.assertEqual(lcs, 'abcf')
