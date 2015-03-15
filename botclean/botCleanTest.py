__author__ = 'Richard S. Stansbury'

"""
Author:     Richard S. Stansbury
Project:    HackerRank - botClean
Date:       2015-03-14

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

    def test_closest(self):
        """
        Confirms can find closest dirty cell.
        :return: N/A
        """

        grid = ['b--d-',
                '-d---',
                '-----',
                'd---d',
                '-----']
        result = botClean.find_closest([0, 0], grid, 5, 5)
        self.assertEqual(result, [1, 1])

        grid = ['d--d-',
                '-d---',
                '-----',
                'd---d',
                '-----']
        result = botClean.find_closest([0, 0], grid, 5, 5)
        self.assertEqual(result, [0, 0])

        grid = ['--d--',
                '-d---',
                '-----',
                'd----',
                '----b']
        result = botClean.find_closest([4, 4], grid, 5, 5)
        self.assertEqual(result, [3, 0])


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

if __name__ == '__main__':
    unittest.main()
