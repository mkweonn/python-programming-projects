# Michelle Kweon, mkweon@usc.edu
# ITP 115, Fall 2021
# Section: Boba
# Lab 11

# import random
import random

# define class
# class: Die
class Die:
    # define constructor
    # parameter: numSides is an int with a default value of 6
    def __init__(self, numSides=6):
        # attributes/instance variables
        self.sides = numSides
        self.rollValue = 0

    # method: roll
    # parameters: None
    # return value: None
    # sets the rollValue by calling random
    def roll(self):
        self.rollValue = random.randrange(1, self.sides + 1)

    # method: __str__
    # parameter: None
    # return value: string with info
    def __str__(self):
        info = "Die has " + str(self.sides) + " sides "
        info += "and rolled a " + str(self.rollValue)
        return info

# define functions

# function: calculateSum
# parameters (2): die1 and die2 are Die objects
# return value: an int which is the sum of the roll values for each die
def calculateSum(die1, die2):
    # call roll method
    die1.roll()
    die2.roll()
    print(die1)  # will call __str__
    print(die2)
    total = die1.rollValue + die2.rollValue
    return total

# function: main
# parameter: None
# return value: None
def main():
    default = input("Use the default number of sides for first die (y/n)? ")
    if default.lower() == "y":
        dieOne = Die()
    else:
        sides = int(input("How many sides? "))
        dieOne = Die(sides)

    default = input("Use the default number of sides for second die (y/n)? ")
    if default.lower() == "y":
        dieTwo = Die()
    else:
        sides = int(input("How many sides? "))
        dieTwo = Die(sides)

    numRolls = int(input("How many times do you want to roll the dice? "))
    for num in range(numRolls):
        sum = calculateSum(dieOne, dieTwo)
        print("The sum of the dice is", sum)

# call main
main()


