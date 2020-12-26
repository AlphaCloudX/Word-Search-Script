import time
from Methods import *

tabQuestion = int(input("Is The Word Search Spaced Using Tab?  1 = True or 2 = False"))

# Start Timer
start_time = time.time()

# Unpacking Array
txtData = []
f = open("wordSearch.txt", "r")

if tabQuestion == 1:
    print("Word Search Spaced Using TAB")
    for lines in f:
        txtData.append(lines.replace("\t", "").replace("\n", "").upper())
    arrayy = txtData

if tabQuestion == 2:
    print("Word Search NOT Spaced Using TAB")
    for lines in f:
        txtData.append(lines.replace(" ", "").replace("\n", "").upper())
    arrayy = txtData

# Words To Locate
txtData = []
f = open("wordsToFind.txt", "r")
for lines in f:
    txtData.append(lines.replace(" ", "").replace("\n", "").upper())
wordToFindd = txtData

# Saving A Final List
finalList = []

array = arrayy
wordToFind = wordToFindd

# Basic Methods
for waysToFind in range(4):

    # Row
    if waysToFind == 0: row = True; board = array; reversee = False; print("Searching Row")

    # Reverse Row
    if waysToFind == 1: row = True; board = array; reversee = True; print("Searching Reverse Row")

    # Column
    if waysToFind == 2: row = False; board = column(array); reversee = False; print("Searching Column")

    # Reverse Column
    if waysToFind == 3: row = False; board = column(array); reversee = True; print("Searching Reverse Column")

    for words in range(len(wordToFind)):

        for lengthOfBoard in range(len(board)):

            for i in range(len(board[lengthOfBoard])):

                wordBeingSearched = []
                t = []

                wordBeingSearched.append(board[lengthOfBoard][i:len(wordToFind[words]) + i])

                if reversee:
                    wordBeingSearched = reverse(wordBeingSearched)

                if len(wordBeingSearched[0]) == len(wordToFind[words]):

                    print("Checking Combination: " + str(wordBeingSearched))

                    if wordBeingSearched[0] == wordToFind[words]:

                        for x in range(0, len(wordToFind[words])):
                            t.append(i+x+1)

                        print(str(wordToFind[words]) + str(" is found at " + "Row: " if row else "Column: ") + str(lengthOfBoard) + " | Letter Positions are: " + str(t))

                        finalList.append([wordToFind[words], str("Row: " if row else "Column: ") + str(int(lengthOfBoard) +1), str("Column: " if row else "Row: ") + str(t)])
                else:
                    pass


print(finalList)
