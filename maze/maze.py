"""
    Author: Richard S. Stansbury
    Project: HackerRank - Maze Bot Challenge

    Filename: maze.py
    Test Cases: mazeTest.py
"""

__author__ = 'richss'
_filename = 'state.out'

def rotate_cw(mat):
    """
    Rotates the matrix clockwise
    Reference: http://stackoverflow.com/questions/42519/how-do-you-rotate-a-two-dimensional-array
    :param mat: matrix to rate
    :return: matrix rotated clockwise
    """
    rot_mat = [list(x) for x in zip(*mat[::-1])]
    return rot_mat


def rotate_ccw(mat):
    """
    Rotates the matrix counter-clockwise
    Reference: http://stackoverflow.com/questions/42519/how-do-you-rotate-a-two-dimensional-array
    :param mat: matrix to rate
    :return: matrix rotated counter-clockwise
    """
    rot_mat = [list(x) for x in zip(*mat)[::-1]]
    return rot_mat


def rotate_180(mat):
    """
    Rotates the matrix 180 degrees
    :param mat: matrix to rate
    :return: matrix rotated 180 degrees
    """
    return rotate_cw(rotate_cw(mat))


def print_state(mat):
    """
    Prints a matrix to the console for debugging.
    :param mat:
    :return:
    """
    for row in mat:
        print row


def initialize_matrix(h,w):
    """
    Initializes world for the robot
    :return:
    """
    matrix = []
    for row in range(0,h):
        row = []
        for col in range(0,w):
            row.append('?')
        matrix.append(row)
    return matrix


def update_world(world, update, row, col, orientation='UP'):
    """
    Updates the world given the world view, update matrix,
    row and column of the bot, and the move that got it
    here (i.e. last move).

    :param world: world view of the state
    :param update: changes to the state given current percept (3x3 matrix)
    :param row: row location of bot
    :param col: col location of bot
    :param move: last move of bot (determines rotation.
    :return:
    """
    # if robot went down, must turn update 180 to align
    # with world view
    if orientation == 'DOWN':
        update = rotate_180(update)

    # if robot went left, must turn update counter clockwise
    # to align with world view
    elif orientation == 'LEFT':
        update = rotate_ccw(update)

    # if robot went right, must turn update clockwise
    # to align with world view
    elif orientation == 'RIGHT':
        update = rotate_cw(update)

    # copy update matrix into world view
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            world[row+dr][col+dc] = update[1+dr][1+dc]
    return world


def save_state(orientation, world, h, w):
    """
    Creates an output file with
    <orientation>
    <world matrix>

    :param world: world state to save
    :param orientation: robot's final orientation given move
    :param h: height of world matrix
    :param w: width of world matrix
    :return: N/A
    """
    with open(_filename, 'w') as f:
        f.write(orientation+'\n')
        for row in range(h):
            f.write(''.join(world[row]) + '\n')


def load_state(h, w):
    """
    Load's the previous state (world map matrix and orientation)
    :param h:
    :param w:
    :return:
    """
    try:
        f = open(_filename)
        orientation = f.readline().strip()
        world = [[x for x in f.readline().strip()] for i in range(h)]

    except IOError:
        return ['UP', None]

    else:
        return [orientation, world]

    finally:
        f.close()


def main():

    # Read Console I/O - Add orientation and stack
    # Load Saved State
    # Merge Worlds
    # Select Next Move
    # Determine New Orientation
    # Write Final State - Add orientation and stack

    pass

if __name__ == '__main__':
    main()
