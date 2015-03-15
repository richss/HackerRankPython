__author__ = 'Richard S. Stansbury'

"""
Author:     Richard S. Stansbury
Project:    HackerRanks - Bot Saves the Princess - 2
Date:       2015-03-14

This file is holds the unit test test cases for princess2.py
"""

import unittest
import princess2


class MyTestCase(unittest.TestCase):

    def test_find(self):
        """
        Confirms successful location of mario and princess
        """
        n = 3
        grid = ['p--', '---', '--m']
        players = princess2.findPrincess(n, grid)
        self.assertEqual(players, [0, 0])

    def test_find2(self):
        """
        Confirms successful location of mario and princess
        """
        n = 3
        grid = ['---', '-p-', '--m']
        players = princess2.findPrincess(n, grid)
        self.assertEqual(players, [1, 1])

    def test_next_down(self):

        mr = 1
        mc = 1
        pr = 3
        pc = 3

        self.assertEqual(princess2.nextMove(mr, mc, pr, pc), "DOWN")

    def test_next_up(self):

        mr = 3
        mc = 3
        pr = 0
        pc = 0

        self.assertEqual(princess2.nextMove(mr, mc, pr, pc), "UP")

    def test_next_right(self):

        mr = 1
        mc = 1
        pr = 1
        pc = 3

        self.assertEqual(princess2.nextMove(mr, mc, pr, pc), "RIGHT")

    def test_next_left(self):

        mr = 1
        mc = 3
        pr = 1
        pc = 1

        self.assertEqual(princess2.nextMove(mr, mc, pr, pc), "LEFT")


if __name__ == '__main__':
    unittest.main()
