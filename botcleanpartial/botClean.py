__author__ = 'Richard S. Stansbury'

"""
Author:     Richard S. Stansbury
Project:    HackerRank - botClean Partial
Date:       2015-03-15

Solves the botClean Partially Observable challenge on HackerRank (difficulty difficult).

Unlike the previous case, you can only sense the 8 cells adjacent to you.

Action: Move Up "UP", Move Down "DOWN", Move Left "LEFT",
Move Right "RIGHT", "CLEAN"

"""

from collections import deque

_filename = 'board.out'

def write_board(grid, h, w):
    """
    Writes the board to an output file.

    :param grid: board to write to file
    :param h: height (num rows) of board
    :param w: width (num cols) of board
    :return: N/A
    """
    with open(_filename, "w") as f:
        for row in range(0, h):
            for col in range(0, w):
                f.write(grid[row][col])
            f.write('\n')


def read_board(h, w):
    """
    Reads a board state from a file.

    :param h: height (num rows) of board
    :param w: width (num cols) of board
    :return: restored board array
    """
    grid = []
    try:
        f = open(_filename)
        for row in range(0, h):
            grid.append(f.readline().strip())
    except IOError:
        return None
    else:
        return grid


def merge_boards(old, new, h, w):
    """
    Merges two boards and returns the final merged copy.

    If old board has a blank or dirty, it gets updated on
    new; except for location of b in new

    :param old: old board state
    :param new: new board state
    :return: merged
    """
    if old is None:
        return new

    merged = []
    for row in range(0, h):

        rowlist = [] # initialize the new row as empty string
        for col in range(0, w):

            # Determine which value gets appended to the row
            if old[row][col] == '-' and new[row][col] != 'b':
                rowlist.append('-')
            elif old[row][col] == 'd' and new[row][col] != 'b':
                rowlist.append('d')
            else:
                rowlist.append(new[row][col])

            # Append the row the the merged board
            if col == w-1:
                merged.append(rowlist)

    return merged  # return new board

def calc_manhattan(row1, col1, row2, col2):
    """

    :param row1: row coordinate of point 1
    :param col1: col coordinate of point 1
    :param row2: row coordinate of point 2
    :param col2: col coordinate of point 2
    :return: manhattan distance between point 1 and point 2
    """
    return abs(row1-row2) + abs(col1-col2)


def find_closest(bot, grid, h, w, target):
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
    visited = []

    while len(queue) != 0:

        cur = queue.popleft()
        visited.append(cur)
        row, col = cur[0], cur[1]


        # See if on dirty location
        if grid[row][col] == target:
            return cur

        # add neighbors

        #up
        if row > 0 and [row-1, col] not in visited:
            queue.append([row-1, col])

        #down
        if row < (h-1)and [row+1, col] not in visited:
            queue.append([row+1, col])

        #left
        if col > 0 and [row, col-1] not in visited:
            queue.append([row, col-1])

        #right
        if col < (w-1) and [row, col+1] not in visited:
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

    # Setup
    pos = [int(i) for i in raw_input().strip().split()]
    newboard = [[j for j in raw_input().strip()] for i in range(5)]
    width, height = 5, 5

    # handle history by merging with previous state
    oldboard = read_board(height, width)
    board = merge_boards(oldboard, newboard, height, width)
    write_board(board, height, width)

    # Perform Task
    closest = find_closest(pos, board, height, width, 'd')
    if closest is None:
        closest = find_closest(pos, board, height, width, 'o')
    if closest is not None:
        print get_next_move(pos, closest)
