# Michelle Kweon, mkweon@usc.edu
# ITP 115, Fall 2021
# Section: Boba
# Lab 8
# Description:
# This program stimulates a coin flip experiment.

import random

# function: coin
def coin():
    flip = "heads"
    randomNum = random.randrange(0, 2)
    if randomNum == 1:
        flip = "tails"
    return flip

# alternative
# return random.choice(["heads", "tails"])

def experiment():
    # local variable
    flips = 0
    heads = 0
    # loops until we get 3 heads in a row
    while heads < 3:
        # flip the coin
        coinFlip = coin()
        flips += 1
        if coinFlip == "heads":
            heads += 1
        else:  # got tails
            heads = 0

    return flips

def main():
    # average = total / num
    total = 0
    numRuns = 10
    # run the experiment 10 times
    for count in range(numRuns):
        numFlips = experiment()
        total += numFlips

    average = total/numRuns
    print("The average for 3 heads in a row is", average)

# call main
main()