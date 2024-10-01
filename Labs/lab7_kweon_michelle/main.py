# Michelle Kweon, mkweon@usc.edu
# ITP 115, Fall 2021
# Section: Boba
# Lab 7
# Description:
# This program displays one of two possible shapes based on user input.

# define functions

# function: printRect
# parameter 1: length is an int for the height of the rectangle
# parameter 2: width is an int for the width of the rectangle
# return value: None
# side effect: print a rectangle
def printRect(length, width):
    # use - and |
    # top row
    print(" " + "-" * width)
    for line in range(length):
        print("|" + " " * width + "|")

    # bottom row
    print(" " + "-" * width)

# function: printSquare
# parameter: size is an int for the size of each side
# return value: None
# side-effect: print a square using - and |
def printSquare(size):
    printRect(size, size)

    # alternate way
    # print(" " + "-" * size)
    # for line in range(size):
    #     print("|" + " " * size + "|")

# define main
def main():
    # testing
    # printRect(5, 3)
    # printSquare(4)

    print("Welcome to the Shape Printer!")
    print("R) Rectangle")
    print("S) Square")
    shape = input("Enter the shape you want to print: ")
    if shape.lower() == "r":
        userLength = int(input("Enter the length: "))
        userWidth = int(input("Enter the width: "))
        printRect(userLength, userWidth)
    elif shape.lower() == "s":
        userSize = int(input("Enter the size: "))
        printSquare(userSize)
    else:
        print("That shape is not supported.")

# call main
main()
