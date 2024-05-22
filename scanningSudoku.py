import simpleSudoku

# squareAnalysis through scanning --> checks the potential entries
# in a square. If there a number (1-9) only appears in one square,
# then it must go in that square. 
# NOTE: this is different from finding a square with only one possibleEntry
# possibleEntries is a dictionary
# return a list of tuples => [(coordinates, value)]
def sqaureAnalysis(coords: tuple, possibleEntries: dict) -> list:
    x, y = coords
    
    xChunk = x // 3
    yChunk = y // 3

    xStart = xChunk * 3
    yStart = yChunk * 3

    squareCoords = []
    # left to right, then down
    for i in range(3):
        for j in range(3):
            squareCoords.append((xStart + j, yStart + i))
    
    squarePotentials = {coords : possibleNums for coords, possibleNums in possibleEntries.items() if coords in squareCoords}

    squareFrequencies = dict()
    for c, p in squarePotentials.items():
        for val in p:
            if val in squareFrequencies:
                squareFrequencies[val][0] += 1
                squareFrequencies[val][1].append(c)
            else:
                squareFrequencies[val] = [1, [c]]
    
    # val, freq, (coordinates)    
    # EX sqaureFrequencies: {3: [4, [(0, 0), (1, 0), (0, 1), (1, 1)]], 8: [2, [(0, 0), (0, 1)]]}

    fillableCoordinates  = [(lst[1][0], val) for val, lst in squareFrequencies.items() if lst[0] == 1]
    return fillableCoordinates

def scanning(board):
    # board and possible entries after a simple analysis
    board, possibleEntries = simpleSudoku.simple(board)
    # print(f"OLD = {board}")
    # print(f"OLD = {possibleEntries}")
    fillableCoordinates = []
    for i in range(3):
        for j in range(3):
            x = i * 3
            y = j * 3
            coords = (x,y)
            # coords will be the following: (0,0), (3,0), (6,0)
            #                               (0,3), (3,3), (6,3)
            #                               (0,6), (3,6), (6,6)

            fillableCoordinatesOnIteration = sqaureAnalysis(coords, possibleEntries)
            print(fillableCoordinatesOnIteration)
            for pair in fillableCoordinatesOnIteration:
                fillableCoordinates.append(pair)

    # print(fillableCoordinates)

    for (x, y), val in fillableCoordinates:
        print()
        board[y][x] = val
        possibleEntries[(x,y)].remove(val)
    
    # print(board)s
    # print(possibleEntries)
    
scanning(simpleSudoku.board2)