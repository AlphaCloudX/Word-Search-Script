def column(t):
    board = []
    placeHolder = ""

    # Check how many letters in first row
    for i in range(len(t[0])):

        # Cycle Through every row
        for x in range(len(t)):
            placeHolder = placeHolder + str(t[x][i])

        board.append(placeHolder)

        placeHolder = ""

    return board


def reverse(listToReverse):
    t = []
    for x in range(len(listToReverse)):
        t.append(listToReverse[x][::-1])

    return t


def stringify(diag):
    text = ""
    for y in range(len(diag)):
        text = text + diag[y]

    return text