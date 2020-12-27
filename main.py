import time
from Methods import *

tabQuestion = int(input("Is The Word Search Spaced Using Tab?  1 = True or 2 = False"))
subQuestion = int(input("Output answers at the end?  1 = True or 2 = False"))
mainQuestion = int(input("Save answers in \"Coordinate.txt\" file?  1 = True or 2 = False"))

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

                    # Showing What Combination it is on
                    print("Checking Combination: " + str(wordBeingSearched))

                    # Check if the word in the list is equal to the word to be found
                    if wordBeingSearched[0] == wordToFind[words]:

                        # Looping to append each position
                        for x in range(0, len(wordToFind[words])):
                            t.append(i + x + 1)  # +1 for easy use can leave without if using pythonic way

                        print(str(wordToFind[words]) + str(" is found at " + "Row: " if row else "Column: ") + str(lengthOfBoard) + " | Letter Positions are: " + str(t))

                        finalList.append([wordToFind[words], str("Row: " if row else "Column: ") + str(int(lengthOfBoard) +1), str("Column: " if row else "Row: ") + str(t)])
                else:
                    pass

print()
print("Basic Check Complete")
print()
print(finalList)
# Basic Methods
for waysToFind in range(7):

    # Regular diagonal
    if waysToFind == 0: position = methodOne(array)[1]; board = methodOne(array)[0]; reversee = False; print("Top Left to Bottom Right | Top Half")
    if waysToFind == 1: position = methodTwo(array)[1]; board = methodTwo(array)[0]; reversee = False; print("Top Left to Bottom Right | Bottom Half")
    if waysToFind == 2: position = methodThree(array)[1]; board = methodThree(array)[0]; reversee = False; print("Top Right to Bottom left | Right Half")
    if waysToFind == 3: position = methodFour(array)[1]; board = methodFour(array)[0]; reversee = False; print("Top Right to Bottom Left | Left Half")

    #Diagonal Reverse
    if waysToFind == 4: position = methodOne(array)[1]; board = methodOne(array)[0]; reversee = True; print("Top Left to Bottom Right | Top Half")
    if waysToFind == 5: position = methodTwo(array)[1]; board = methodTwo(array)[0]; reversee = True; print("Top Left to Bottom Right | Bottom Half")
    if waysToFind == 6: position = methodThree(array)[1]; board = methodThree(array)[0]; reversee = True; print("Top Right to Bottom left | Right Half")
    if waysToFind == 7: position = methodFour(array)[1]; board = methodFour(array)[0]; reversee = True; print("Top Right to Bottom Left | Left Half")

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

                        t.append(position[lengthOfBoard][i:i + len(wordBeingSearched[0])])

                        print(str(wordToFind[words]) + str(" is found at XY: ") + str(position[lengthOfBoard][i:i + len(wordBeingSearched[0])]))

                        finalList.append([wordToFind[words], str("Coordinates: ") + str(t[0])])
                else:
                    pass

print()
print(finalList)
print("Done in: " + str(time.time() - start_time) + " Seconds")

if subQuestion == 1:
    subQuestion == True

if mainQuestion == 1:
    print()
    print("File Saved as \"Coordinate.txt\"")

    f = open("Coordinate.txt", "w+")

    for i in range(len(finalList)):
        f.write(str(finalList[i]) + "\n")
        if subQuestion:
            print(str(finalList[i]))

    f.close()

print("All done, program closing in 5 seconds!")
time.sleep(5)
