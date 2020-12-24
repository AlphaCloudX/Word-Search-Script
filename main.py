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
