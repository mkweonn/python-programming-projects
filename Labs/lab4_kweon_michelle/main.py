# Michelle Kweon, mkweon@usc.edu
# ITP 115, Fall 2021
# Section: Boba
# Lab 4
# Description:
# This program uses for loops to print a triangle created with the ^ symbol.

# create variables
numSpaces = 18
numSymbols = 1

# loop
for row in range(10):
    print(" " * numSpaces + "^ " * numSymbols)
    numSymbols = numSymbols + 2
    numSpaces = numSpaces - 2

# challenge 1
print("\nChallenge #1")
for symbol in range (1, 20, 2):
    print(" " * (19 - symbol) + "^ " * symbol)

# challenge 2
print("\n Challenge #2")
for symbol in range(19, 0, -2):
    print(" " * (19 - symbol) + "^ " * symbol)