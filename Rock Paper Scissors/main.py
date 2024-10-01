# Michelle Kweon, mkweon@usc.edu
# ITP 115, Fall 2021
# Section: Boba
# Assignment 7
# Description:
# This program stimulates a game of rock-paper-scissors against the computer.

# modules
import random

# define functions
# display game rules to the user
# displayMenu() no parameters and no returns
def displayMenu():
    print("\nLet's play Rock Paper Scissors.")
    print("The rules of the game are:")
    print("\tRock smashes Scissors")
    print("\tScissors cut Paper")
    print("\tPaper covers Rock")
    print("\tIf both the choices are the same, it's a tie")

# get computer's choice
# no parameters
# returns random integer to indicate choice
def getComputerChoice():
    # randomly choose computer's choice of rock (0), paper (1), or scissors (2)
    # use random module for number (integer) between 0-2 (inclusive)
    return random.randrange(0,3)

# get player's choice
# no parameters
# returns user's input
def getPlayerChoice():
    print("Enter 0 for Rock, 1 for Paper, or 2 for Scissors")
    choice = int(input("> "))
    # loop if user does not input a number between 0 - 2
    while choice not in range(0, 3):
        choice = int(input("> "))
    return choice

# determine winner of round
# returns result of round (win, lose, tie)
def playRound(computerChoice, playerChoice):
    # parameter 1: integer representing the computer's choice
    # parameter 2: integer representing the player's choice
    # branching
    if computerChoice == playerChoice:
        return 0  # return 0 means tie
    # return 1 means player wins
    elif computerChoice == 0 and playerChoice == 1:  # rock vs paper
        return 1
    elif computerChoice == 1 and playerChoice == 2:  # paper vs scissors
        return 1
    elif computerChoice == 2 and playerChoice == 0:  # scissors vs rock
        return 1
    else:
        return -1  # return -1 means computer wins

# loop to repeat game
# no parameters
def continueGame():
    repeat = input("Do you want to continue playing (y or n)? ")
    # return boolean statements in order to stop or continue loop
    if repeat.lower() == "y":
        return True
    else:
        return False

# define main
# no parameters or returns
def main():
    # count variables
    tie = 0
    loss = 0
    win = 0
    checkGame = True  # initial condition to start while loop
    while checkGame == True:
        displayMenu()
        callPlayerChoice = getPlayerChoice()
        callComputerChoice = getComputerChoice()
        callPlayRound = playRound(callComputerChoice, callPlayerChoice)

        if callPlayRound == 0:
            tie += 1
            print("You and the computer tied.")
        elif callPlayRound == 1:
            print("You win!")
            win += 1
        else:
            print("Computer wins.")
            loss += 1

        # call function to repeat round
        checkGame = continueGame()

    # display score
    print("\nYou won", win, "game(s).")
    print("The computer won", loss, "game(s).")
    print("You tied with the computer", tie, "time(s).")

# call main
main()