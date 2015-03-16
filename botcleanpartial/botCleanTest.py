__author__ = 'Richard S. Stansbury'

"""
Author:     Richard S. Stansbury
Project:    HackerRank - botClean Partially Observable
Date:       2015-03-15

Tests botClean.py

"""

import unittest
import botClean


class MyTestCase(unittest.TestCase):
    def test_manhattan1(self):
        """
        Confirms manhattan distance function
        :return: N/A
        """

        dist = botClean.calc_manhattan(0, 0, 1, 1)
        assert dist == 2

        dist = botClean.calc_manhattan(1, 1, 0, 0)
        assert dist == 2

        dist = botClean.calc_manhattan(0, 0, 5, 0)
        assert dist == 5

        dist = botClean.calc_manhattan(0, 5, 0, 0)
        assert dist == 5

    def test_closest_dirty(self):
        """
        Confirms can find closest dirty cell.
        :return: N/A
        """

        grid = ['b-ooo',
                '-dooo',
                'ooooo',
                'ooooo',
                'ooooo']
        result = botClean.find_closest([0, 0], grid, 5, 5, 'd')
        self.assertEqual(result, [1, 1])

        grid = ['d-ooo',
                '-dooo',
                'ooooo',
                'ooooo',
                'ooooo']
        result = botClean.find_closest([0, 0], grid, 5, 5, 'd')
        self.assertEqual(result, [0, 0])

        grid = ['ooooo',
                'ooooo',
                'ooooo',
                'ooo--',
                'ooo-b']
        result = botClean.find_closest([4, 4], grid, 5, 5, 'd')
        self.assertEqual(result, None)

    def test_closest_unknown(self):
        """
        Confirms can find closest dirty cell.
        :return: N/A
        """

        grid = ['b-ooo',
                '-dooo',
                'ooooo',
                'ooooo',
                'ooooo']
        result = botClean.find_closest([0, 0], grid, 5, 5, 'o')
        self.assertEqual(result, [2, 0])

        grid = ['ooooo',
                'ooooo',
                'ooooo',
                'ooo--',
                'ooo-b']
        result = botClean.find_closest([4, 4], grid, 5, 5, 'o')
        self.assertEqual(result, [2, 4])

    def test_merge(self):
        """
        Confirms merge of two grids works
        :return:
        """
        old = ['ooooo',
               'ooooo',
               'ooooo',
               'oood-',
               '-----']

        new = ['ooooo',
               'ooooo',
               'oo---',
               'oo-b-',
               'oo---']

        merged = [['o', 'o', 'o', 'o', 'o'],
                  ['o', 'o', 'o', 'o', 'o'],
                  ['o', 'o', '-', '-', '-'],
                  ['o', 'o', '-', 'b', '-'],
                  ['-', '-', '-', '-', '-']]

        self.assertEqual(botClean.merge_boards(old, new, 5, 5),
                         merged)

    def test_move(self):
        """
        Confirms successful determination of next move
        for agent give its location and location of
        closest dirty location.
        :return: N/A
        """

        assert botClean.get_next_move([1, 1], [1, 1]) == 'CLEAN'
        assert botClean.get_next_move([1, 1], [0, 0]) == 'UP'
        assert botClean.get_next_move([0, 0], [1, 1]) == 'DOWN'
        assert botClean.get_next_move([1, 2], [1, 1]) == 'LEFT'
        assert botClean.get_next_move([1, 1], [1, 2]) == 'RIGHT'

    def test_save_restore(self):
        """
        Confirms the ability to save and restore a board
        state.

        :return: N/A
        """
        old = ['ooooo',
               'ooooo',
               'ooooo',
               'ooo--',
               '----b']

        botClean.write_board(old, 5, 5)
        result = botClean.read_board(5, 5)

        self.assertEqual(old, result)

if __name__ == '__main__':
    unittest.main()
