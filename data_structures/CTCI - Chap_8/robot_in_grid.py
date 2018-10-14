import unittest


def find_path(maze):
    if not maze or len(maze) == 0:
        return
    paths = []
    visited = set()
    if get_path(maze, len(maze) - 1, len(maze[0]) - 1, paths, visited):
        return paths

    return


def get_path(maze, row, col, paths, visited):
    """
    Find the path in the maze from the origin to the given cell
    :param maze: Two dimensional grid
    :param row: row in the maze
    :param col: col in the maze
    :param paths: path to the current node
    :return:
    """
    # Base Case - If we go out of bounds or there is an off limit cell
    if row < 0 or col < 0 or not maze[row][col]:
        return False

    p = Point(row, col)
    if p in visited:
        print(f'returning false for {row}, {col}')
        return False
    # Check if we are at origin
    is_at_origin = (row == 0 and col == 0)

    if is_at_origin or get_path(maze, row - 1, col, paths, visited) or get_path(maze, row, col - 1, paths, visited):
        paths.append(str(p))
        return True

    visited.add(p)
    return False


class Point:
    def __init__(self, r, c):
        self.row = r
        self.col = c

    def __str__(self):
        return f'({self.row}, {self.col})'

    def __eq__(self, other):
        if type(other) != type(self):
            return False
        return self.row == other.row and self.col == other.col

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return 41 * (41 + self.col) + self.row


class TestRobotInGrid(unittest.TestCase):

    def setUp(self):
        # Create a 4x4 maze
        # self.maze = [[False] * 4 for row in range(4)]
        self.maze = [[True, True, True, True],
                     [True, True, False, True],
                     [True, False, True, False],
                     [True, True, True, True]]

    def test_path_in_maze(self):
        result = find_path(self.maze)
        print(result)
        self.assertIsNotNone(result)


if __name__ == '__main__':
    unittest.main()
