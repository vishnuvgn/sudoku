# This script assumes that with every "analysis of the board" iteration,
# there will be at least one square with only one possible entry
# NOTE: THIS IS NOT THE CASE FOR EVERY SUDOKU!!!

import time
# O(n)
def rowCheck(coords, possibleEntry, board):
    x, y = coords
    if possibleEntry not in board[y]:
        return True
    return False

# O(n)
def columnCheck(coords, possibleEntry, board):
    x, y = coords
    colInQ = []
    for row in board:
        colInQ.append(row[x])
    if possibleEntry not in colInQ:
        return True
    return False

# O(n)
def squareCheck(coords, possibleEntry, board):
    x, y = coords
    # floor divide by three to get "chunk" number
    xChunk = x // 3
    yChunk = y // 3

    xStart = xChunk * 3
    yStart = yChunk * 3

    square = []

    for i in range(3):
        for j in range(3):
            square.append(board[yStart + i][xStart + j])
    if possibleEntry not in square:
        return True
    return False

def check(coords, possibleEntry, board):
    x, y = coords
    if board[y][x] == None:
        return rowCheck(coords, possibleEntry, board) and columnCheck(coords, possibleEntry, board) and squareCheck(coords, possibleEntry, board)
    return False

def getPossibleEntries(coords, board):
    possibleEntries = []
    for num in range(1, 10):
        if check(coords, num, board):
            possibleEntries.append(num)
    return possibleEntries


board1 = [
    [None, None, 2, 7, None, 1, None, None, 6],
    [None, None, None, 6, 9, None, None, 1, None],
    [None, 9, 6, None, 8, None, None, 5, 3],
    [9, 8, 4, None, None, None, None, None, None],
    [2, None, None, None, None, None, 6, 4, None],
    [6, None, 3, None, None, 5, 8, None, None],
    [None, 7, 8, None, 1, 4, 9, None, None],
    [4, 2, None, 3, 6, 7, None, None, 5],
    [5, None, 1, None, None, 9, 3, None, 4],
]

board1 = [
    [None, None, 2, 7, None, 1, None, None, 6],
    [None, None, None, 6, 9, None, None, 1, None],
    [None, 9, 6, None, 8, None, None, 5, 3],
    [9, 8, 4, None, None, None, None, None, None],
    [2, None, None, None, None, None, 6, 4, None],
    [6, None, 3, None, None, 5, 8, None, None],
    [None, 7, 8, None, 1, 4, 9, None, None],
    [4, 2, None, 3, 6, 7, None, None, 5],
    [5, None, 1, None, None, 9, 3, None, 4],
]

board2 = [
    [3, 8, 6, None, None, 4, 7, None, None],
    [None, None, 9, None, None, None, 2, None, None],
    [None, 2, None, 1, None, 3, 8, None, 5],
    [None, 7, 8, None, 3, None, 6, 2, None],
    [None, 5, 2, None, None, 1, None, None, 4],
    [None, 4, None, 2, 7, None, None, None, None], # first val was 9
    [2, 3, None, 7, 4, 9, 5, 8, 6],
    [8, None, None, None, 1, None, 4, None, None],
    [4, None, None, None, None, None, None, None, 2],
]

def simple(board) -> tuple:
    startTime = time.time()
    possibleEntries = dict() # dictionary of coordinates (key) to possibleEntries (value)

    i = 0

    while i == 0 or len(possibleEntries) != 0:
        i = 1
        for y in range(9):
            for x in range(9):
                if board[y][x] == None:
                    possibleEntries[(x,y)] = getPossibleEntries((x,y), board)
        
        
        singleValExists = False
        for coords, possibleNums in possibleEntries.items():
            x, y = coords
            if len(possibleNums) == 1:
                singleValExists = True
                board[y][x] = possibleNums[0]
        if singleValExists == False:
            break 
        possibleEntries = {coords : possibleNums for coords, possibleNums in possibleEntries.items() if len(possibleNums) != 1}
        # print(possibleEntries)
    
    return (board, possibleEntries)
    # print(f'time for simple solve / analysis: {time.time()-startTime}')

# print(simple(board2)[0])