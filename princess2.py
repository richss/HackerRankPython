__author__ = 'Richard S. Stansbury'

"""
Author:     Richard S. Stansbury
Project:    HackerRanks - Save the Princess - 2
Date:       2015-03-14
"""

def findPrincess(n, grid):
    """
     Brute force search for the princess

    :param n: width/height dimension of the search area
    :param grid: search area with bot position 'm' and princess position 'p'
    :return: array with location of the princess positions
    """
    for row in range(0, n):
        for col in range(0, n):

            if grid[row][col] == 'p':
                pRow = row
                pCol = col
                return [pRow, pCol]

    return None

def nextMove(mr, mc, pr, pc):
    """
    Determines the next move given the coordinates of mario and the princess
    :param mr: mario's row
    :param mc: mario's column
    :param pr: princess's row
    :param pc: princess's col
    :return: "UP" | "DOWN" | "LEFT" | "RIGHT"
    """

    if mr > pr:
        return "UP"
    elif mr < pr:
        return "DOWN"
    elif mc < pc:
        return "RIGHT"
    elif mc > pc:
        return "LEFT"

    return None


"""
Main
"""
if __name__ == '__main__':
    n = input()
    r,c = [int(i) for i in raw_input().strip().split()]
    grid = []
    for i in xrange(0, n):
        grid.append(raw_input())

    [pr, pc] = findPrincess(n, grid)
    print nextMove(r, c, pr, pc)