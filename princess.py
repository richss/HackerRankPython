"""
Author: Richard S. Stansbury
Project:  HackerRank - Bot Saves Princess

This is my first Python program beyond hello world
"""


def findPlayers(n, grid):
    """
     Brute force search for the bot and princess

    :param n: width/height dimension of the search area
    :param grid: search area with bot position 'm' and princess position 'p'
    :return: array with location of the bot and princess positions
    """
    for row in xrange(0, n):
        for col in xrange(0, n):

            if grid[row][col] == 'p':
                pRow = row
                pCol = col

            elif grid[row][col] == 'm':
                sRow = row
                sCol = col

    return [sRow, sCol, pRow, pCol]


def displayPathtoPrincess(n, grid):
    """
    Moves the bot to the princess following a simple zig-zag
    pattern.

    :param n: width/height dimension of the search area
    :param grid: search area with bot position 'm' and princess position 'p'
    :return: list
    """

    [row, col, pRow, pCol] = findPlayers(n, grid)

    moves = []

    while not (row == pRow and col == pCol):

        # Row Move
        if row > pRow:
            moves.append("UP")
            row -= 1

        elif row < pRow:
            moves.append("DOWN")
            row += 1

        #Column Move
        elif col > pCol:
            moves.append("LEFT")
            col -= 1

        elif col < pCol:
            moves.append("RIGHT")
            col += 1

    return moves


if __name__ == "__main__":

    # Setup
    m = input()

    grid = []
    for i in xrange(0, m):
        grid.append(raw_input().strip())


    #Run
    results = displayPathtoPrincess(m, grid)
    for result in results:
        print result





