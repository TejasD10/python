import unittest


def matrix_rotate(inp):
    """
    Rotate the given n x n square matrix by 90 degrees clock wise
    :param inp: n x n square matrix
    :return: rotated matrix
    """
    if not inp:
        return None

    for item in inp:
        if len(inp) != len(item):
            raise TypeError('Input matrix is not a square matrix')

    for layer in range(len(inp) // 2):
        first = layer
        last = len(inp) - layer - 1
        for k in range(first, last):
            # top
            top = inp[first][k]

            # left -> top
            inp[first][k] = inp[-k - 1][first]

            # bottom -> left
            inp[-k - 1][first] = inp[-first - 1][-k - 1]

            # right -> bottom
            inp[-first - 1][-k - 1] = inp[k][-first - 1]

            inp[k][-first - 1] = top

    return inp


class MatrixRotationTest(unittest.TestCase):
    """
    Test Cases for rotating a matrix at 90 degrees
    """
    # Tuple for an input and output
    data = [([
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [21, 16, 11, 6, 1],
            [22, 17, 12, 7, 2],
            [23, 18, 13, 8, 3],
            [24, 19, 14, 9, 4],
            [25, 20, 15, 10, 5]
        ])]

    # Non squared matrix
    data_non_square = [([[1, 2, 3],
                         [4, 5, 6]], None)]

    def test_matrix_rotation(self):
        """
        Test Matrix Rotation
        """
        for inp, output in self.data:
            self.assertEqual(output, matrix_rotate(inp))

    def test_non_square_matrix(self):
        """
        Test for a non squared matrix which should return None
        :return: The method under test should raise a TypeError
        """
        for inp, output in self.data_non_square:
            self.assertRaises(TypeError)


if __name__ == '__main__':
    unittest.main()
