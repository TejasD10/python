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

    layer, i = len(inp) // 2, 0  # Identify the layers in the matrix
    for i in range(layer):
        first = i
        last = len(inp[i]) - i - 1
        for k in range(first, last):
            # Get the first element out in a temporary variable
            temp = inp[first][k]

            inp[first][k] = inp[last - k][first]

            inp[last - k][first] = inp[last][last - k]

            inp[last][last - k] = inp[first + k][last]

            inp[first + k][last] = temp

    return inp


class MatrixRotationTest(unittest.TestCase):
    """
    Test Cases for rotating a matrix at 90 degrees
    """
    # Tuple for an input and output
    data = [([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]],
             [[13, 9, 5, 1],
              [14, 10, 6, 2],
              [15, 11, 7, 3],
              [16, 12, 8, 4]])]

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
