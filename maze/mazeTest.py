__author__ = 'richss'

import unittest
import maze


class MyTestCase(unittest.TestCase):

    """

        Testing Rotations

    """

    def test_rotate_right(self):
        """
        Tests rotation if agent moved right
        """

        matrix = [['#', '#', '#'],
                  ['#', ' ', ' '],
                  ['#', ' ', ' ']]

        target = [['#', ' ', ' '],
                  ['#', ' ', ' '],
                  ['#', '#', '#']]

        result = maze.rotate_ccw(matrix)

        self.assertEqual(target, result)

    def test_rotate_left(self):
        """
        Tests rotation if agent moved left
        """

        matrix = [['#', '#', '#'],
                  ['#', ' ', ' '],
                  ['#', ' ', ' ']]

        target = [['#', '#', '#'],
                  [' ', ' ', '#'],
                  [' ', ' ', '#']]

        result = maze.rotate_cw(matrix)

        self.assertEqual(target, result)


    def test_rotate_down(self):
        """
        Tests rotation if agent moved down
        """

        matrix = [['#', '#', '#'],
                  ['#', ' ', ' '],
                  ['#', ' ', ' ']]

        target = [[' ', ' ', '#'],
                  [' ', ' ', '#'],
                  ['#', '#', '#']]

        result = maze.rotate_180(matrix)

        self.assertEqual(target, result)

    def test_init(self):

        target = [['?', '?', '?', '?', '?'],
                  ['?', '?', '?', '?', '?'],
                  ['?', '?', '?', '?', '?'],
                  ['?', '?', '?', '?', '?'],
                  ['?', '?', '?', '?', '?']]

        self.assertEqual(maze.initialize_matrix(5, 5), target)


    """

        Testing Rotations

    """
    def test_update_world_up(self):
        """
        Tests updating the world with the percept matrix
        :return: N/A
        """
        matrix = maze.initialize_matrix(5, 5)

        update = [[' ', ' ', '#'],
                  [' ', ' ', '#'],
                  ['#', '#', '#']]

        target = [['?', '?', '?', '?', '?'],
                  ['?', ' ', ' ', '#', '?'],
                  ['?', ' ', ' ', '#', '?'],
                  ['?', '#', '#', '#', '?'],
                  ['?', '?', '?', '?', '?']]

        row, col = 2,2

        self.assertEqual(target,
                         maze.update_world(matrix, update, row, col, 'UP'))

    def test_update_world_down(self):
        """
        Tests updating the world after a rotation down of the
        percept matrix.
        :return: N/A
        """
        matrix = maze.initialize_matrix(5, 5)

        update = [[' ', ' ', '#'],
                  [' ', ' ', '#'],
                  ['#', '#', '#']]

        target = [['?', '?', '?', '?', '?'],
                  ['?', '#', '#', '#', '?'],
                  ['?', '#', ' ', ' ', '?'],
                  ['?', '#', ' ', ' ', '?'],
                  ['?', '?', '?', '?', '?']]

        row, col = 2,2

        self.assertEqual(target,
                         maze.update_world(matrix, update, row, col, 'DOWN'))

    def test_update_world_right(self):
        """
        Tests updating the world after a rotation left of the
        percept matrix.
        :return: N/A
        """
        matrix = maze.initialize_matrix(5, 5)

        update = [[' ', ' ', '#'],
                  [' ', ' ', '#'],
                  ['#', '#', '#']]

        target = [['?', '?', '?', '?', '?'],
                  ['?', '#', ' ', ' ', '?'],
                  ['?', '#', ' ', ' ', '?'],
                  ['?', '#', '#', '#', '?'],
                  ['?', '?', '?', '?', '?']]

        row, col = 2,2

        self.assertEqual(target,
                         maze.update_world(matrix, update, row, col, 'RIGHT'))

    def test_update_world_left(self):
        """
        Tests updating the world after a rotation right of the
        percept matrix.
        :return: N/A
        """
        matrix = maze.initialize_matrix(5, 5)

        update = [[' ', ' ', '#'],
                  [' ', ' ', '#'],
                  ['#', '#', '#']]

        target = [['?', '?', '?', '?', '?'],
                  ['?', '#', '#', '#', '?'],
                  ['?', ' ', ' ', '#', '?'],
                  ['?', ' ', ' ', '#', '?'],
                  ['?', '?', '?', '?', '?']]

        row, col = 2, 2

        self.assertEqual(target,
                         maze.update_world(matrix, update, row, col, 'LEFT'))

    def test_save_load(self):

        orientation = 'DOWN'
        world = [['?', '?', '?', '?', '?'],
                 ['?', '#', '#', '#', '?'],
                 ['?', ' ', ' ', '#', '?'],
                 ['?', ' ', ' ', '#', '?'],
                 ['?', '?', '?', '?', '?']]

        maze.save_state(orientation, world, 5, 5)
        [loadOr, loadWorld] = maze.load_state(5, 5)
        self.assertEqual(orientation, loadOr)
        self.assertEqual(world, loadWorld)


if __name__ == '__main__':
    unittest.main()
