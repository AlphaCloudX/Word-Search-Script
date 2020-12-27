# Method to get a column
def column(t):
    board = []
    placeHolder = ""

    # Checking How Many Letters Are in The first Row
    for i in range(len(t[0])):

        # Cycling For every Row
        for x in range(len(t)):
            # Appends all letters that are in x value(next row)
            placeHolder = placeHolder + str(t[x][i])

        # Appending Completed String to List
        board.append(placeHolder)

        # Clearing The String
        placeHolder = ""

    return board


def reverse(listToReverse):
    t = []
    for x in range(len(listToReverse)):
        # appends Backwards
        t.append(listToReverse[x][::-1])

    return t


# Diagonal Methods:

# Used by the lower methods
def stringify(diag):
    text = ""
    # Turning indices into 1 whole string
    for y in range(len(diag)):
        text = text + diag[y]

    return text


def methodOne(array):
    board = []
    positions = []
    # For top Left to Bottom Right | Top Half
    for x in range(len(array[0])):
        diag = stringify([row[i + x] for i, row in enumerate(array) if 0 <= i + x < len(row)])
        board.append(diag)

        position = [(i + x+1, i+1) for i, row in enumerate(array) if 0 <= i + x < len(row)]
        positions.append(position)

    return board, positions


def methodTwo(array):
    board = []
    positions = []
    # For top Left to Bottom Right | Bottom Half
    for x in range(len(array)):
        diag = stringify([array[x + i][i] for i, row in enumerate(array) if 0 <= i + x < len(array)])
        board.append(diag)

        position = [(i+1, x + i+1) for i, row in enumerate(array) if 0 <= i + x < len(array)]
        positions.append(position)

    return board, positions


def methodThree(array):
    board = []
    positions = []
    # For Top Right to bottom Left | Right Half, Need to search left half
    for x in range(len(array)):
        diag = stringify([array[x + i][-1 - i] for i, row in enumerate(array) if 0 <= i + x < len(array)])
        board.append(diag)

        position = [(x + i + 1, (-i + len(array[0]))) for i, row in enumerate(array) if 0 <= i + x < len(array)]
        positions.append(position)

    return board, positions


def methodFour(array):
    board = []
    positions = []
    # For Top Right to bottom Left | Right Half, Need to search left half | Remove First 2
    for x in range(len(array[0]) + 1):
        if x != 0:
            diag = stringify([row[-(i + x)] for i, row in enumerate(array) if -(i + x) >= -(len(array[0]))])
            board.append(diag)

            position = [(i+1, -(i + x) + len(array[0])+1) for i, row in enumerate(array) if -(i + x) >= -(len(array[0]))]
            positions.append(position)

    return board, positions
