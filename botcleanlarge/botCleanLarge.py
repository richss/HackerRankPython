__author__ = 'Richard S. Stansbury'

"""
Author:     Richard S. Stansbury
Project:    HackerRank - botCleanLarge
Date:       2015-03-14

Solves the botClean challenge on HackerRank (difficulty easy).

Action: Move Up "UP", Move Down "DOWN", Move Left "LEFT",
Move Right "RIGHT", "CLEAN"

Clean's if on a dirty location

Sample Input:

0 0
b---d
-d--d
--dd-
--d--
----d

Sample Output:

RIGHT

Reference:
https://www.hackerrank.com/challenges/botclean

"""

from collections import deque

def calc_manhattan(row1, col1, row2, col2):
    """

    :param row1: row coordinate of point 1
    :param col1: col coordinate of point 1
    :param row2: row coordinate of point 2
    :param col2: col coordinate of point 2
    :return: manhattan distance between point 1 and point 2
    """
    return abs(row1-row2) + abs(col1-col2)


def find_closest(bot, grid, h, w):
    """
    Find's the closest dirty cell to the bot location using
    a breadth first search.

    :param bot: bot position
    :param grid: grid environment
    :param h - height of grid
    :param w - width of grid
    :return: point of closest dirt
    """
    queue = deque([bot])

    while len(queue) != 0:

        cur = queue.popleft()
        row, col = cur[0], cur[1]

        # See if on dirty location
        if grid[row][col] == 'd':
            return cur

        # add neighbors

        #up
        if row > 0:
            queue.append([row-1, col])

        #down
        if row < (h-1):
            queue.append([row+1, col])

        #left
        if col > 0:
            queue.append([row, col-1])

        #right
        if col < (w-1):
            queue.append([row, col+1])

    return None


def get_next_move(bot, dirt):
    """
    Prints the next move.

    :param bot:
    :param dirt:
    :return:
    """

    if bot[0] > dirt[0]:
        return 'UP'

    elif bot[0] < dirt[0]:
        return 'DOWN'

    elif bot[1] > dirt[1]:
        return 'LEFT'

    elif bot[1] < dirt[1]:
        return 'RIGHT'

    else:
        return 'CLEAN'




if __name__ == "__main__":

    #Setup
    pos = [int(i) for i in raw_input().strip().split()]
    dim = [int(i) for i in raw_input().strip().split()]
    board = [[j for j in raw_input().strip()] for i in range(dim[0])]


    #Perform Task
    closest = find_closest(pos, board, dim[0], dim[1])
    if closest is not None:
        print get_next_move(pos, closest)
