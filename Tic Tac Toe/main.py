# Michelle Kweon, mkweon@usc.edu
# ITP 115, Fall 2021
# Section: Boba
# Assignment 8
# Description:
# This program uses functions to stimulate a two-player game of Tic Tac Toe.

# import file
import TicTacToeHelper  # tells current state of game and displays board

# function: isValidMove() looks at a specified spot on board
# parameter 1: list representing the board
# parameter 2: integer corresponding to index position of user's letter spot
# return value: boolean true (if spot open) or false (spot taken/parameter not valid index)
def isValidMove(boardList, spot):
    if spot < 0 or spot > 8:  # not valid index
        return False
    if boardList[spot] != "x" and boardList[spot] != "o":  # spot open
        return True
    else:  # spot taken
        return False

# function: updateBoard() takes current board list and places player's letter in specified spot
# parameter 3: string representing user's letter ("x" or "o")
# no return value
def updateBoard(boardList, spot, playerLetter):
    boardList[spot] = playerLetter

# function: plays game
# no parameters or return value
def playGame():
    board_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
    choice = -1
    playerLetter = ""
    checkWinner = "n"
    move_counter = 0  # count to track number of moves

    # # extra credit: allows the user to choose which player begins
    # optionChoice = input("\nChoose starting player (x or o): ")
    # while optionChoice != "x" and optionChoice != "o":
    #     print("Invalid Option")
    #     optionChoice = input("Choose starting player (x or o): ")


    # if optionChoice == "x":
    #     move_counter = 0
    # else:
    #     move_counter = 1

    # player inputs round choice and updates board
    while checkWinner == "n":
        move_counter += 1
        TicTacToeHelper.printUglyBoard(board_list)
        if move_counter % 2 == 1:
            while isValidMove(board_list, choice) == False:
                playerLetter = "x"
                choice = int(input("Player x, pick a spot: "))
            updateBoard(board_list, choice, playerLetter)
        else:
            while isValidMove(board_list, choice) == False:
                playerLetter = "o"
                choice = int(input("Player o, pick a spot: "))
            updateBoard(board_list, choice, playerLetter)

        # game is over when checkForWinner() does not return an "n"
        checkWinner = TicTacToeHelper.checkForWinner(board_list, move_counter)

    TicTacToeHelper.printUglyBoard(board_list)

# print results
    print("\nGame Over!")
    if checkWinner == "x":
        print("Player x is the winner!")
    elif checkWinner == "o":
        print("Player o is the winner!")
    else:
        print("Stalemate reached!")

# define main (no parameters or return value)
def main():
    print("Welcome to Tic Tac Toe!")
    playGame()
    newGame = input("Would you like to play another round? (y or n): ")
    while newGame.lower() == "y":
        playGame()
        newGame = input("Would you like to play another round? (y or n): ")
    print("Goodbye!")

# call main
main()