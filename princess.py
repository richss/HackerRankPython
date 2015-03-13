#!/bin/python

#########################################################
#  Author: Richard S. Stansbury
#  Project:  HackerRank - Bot Saves Princess
#
#  This is my first Python program beyond hello world


# Brute Force Search for the bot 'm' and the princess 'p'
def findPlayers(n, grid):
    for row in xrange(0, m):
        for col in xrange(0, m):

            if grid[row][col] == 'p':
                pRow = row
                pCol = col

            elif grid[row][col] == 'm':
                sRow = row
                sCol = col

    return [sRow, sCol, pRow, pCol]


# Moves the bot to the princess following a simple zig-zag
#  pattern
def displayPathtoPrincess(n, grid):

    [row, col, pRow, pCol] = findPlayers(n, grid)

    while row != pRow or col != pCol:

        #Row Move
        if row > pRow:
            print "UP"
            row -= 1

        elif row < pRow:
            print "DOWN"
            row += 1

        #Column Move
        if col > pCol:
            print "LEFT"
            col -= 1

        elif col < pCol:
            print "RIGHT"
            col += 1

#Setup
m = input()

grid = []
for i in xrange(0, m):
    grid.append(raw_input().strip())


#Run
displayPathtoPrincess(m, grid)



