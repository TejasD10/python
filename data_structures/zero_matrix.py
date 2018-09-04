import unittest


def zero_matrix(inp):
    """
    Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
    column are set to 0
    :param inp: MxN matrix
    :return: MxN Matrix - Rows and columns are appropriately set to zeros as the problem suggests
    """
    # Store the position of zeros
    rows, cols = [], []

    for i in range(len(inp)):
        for j in range(len(inp[i])):
            if inp[i][j] == 0:
                rows.append(i)
                cols.append(j)

    for i in range(len(inp)):
        for j in range(len(inp[i])):
            if i in rows or j in cols:
                inp[i][j] = 0

    return inp


class ZeroMatrixTest(unittest.TestCase):
    data = [
        ([
             [1, 2, 3, 4, 0],
             [6, 0, 8, 9, 10],
             [11, 12, 13, 14, 15],
             [16, 0, 18, 19, 20],
             [21, 22, 23, 24, 25]
         ], [
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [11, 0, 13, 14, 0],
             [0, 0, 0, 0, 0],
             [21, 0, 23, 24, 0]
         ])
    ]

    def test_zero_matrix_valid_input(self):
        for inp, output in self.data:
            self.assertEqual(output, zero_matrix(inp))


if __name__ == '__main__':
    unittest.main()
