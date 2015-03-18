__author__ = 'Richard S. Stansbury'

"""
This file defines unit tests for princess.py.
"""

import unittest
import princess

class MyTestCase(unittest.TestCase):

    def test_find(self):
        """
        Confirms successful location of mario and princess
        """
        n = 3
        grid = ['p--', '---', '--m']
        players = princess.findPlayers(n, grid)
        self.assertEqual(players, [2, 2, 0, 0])


    def test_solve1(self):
        """
        Confirms solution of 3x3
        """
        n = 3
        grid = ['p--', '---', '--m']
        results = princess.displayPathtoPrincess(n, grid)
        self.assertEqual(results, ['UP', 'UP', 'LEFT', 'LEFT'])


    def test_solve2(self):
        """
        Confirms solution of 5x5
        """
        n = 5
        grid = ['-----', 'p----', '-----', '-----', '--m--']
        results = princess.displayPathtoPrincess(n, grid)
        self.assertEqual(results, ['UP', 'UP', 'UP', 'LEFT', 'LEFT'])


if __name__ == '__main__':
    unittest.main()
