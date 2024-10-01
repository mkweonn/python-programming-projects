# Michelle Kweon, mkweon@usc.edu
# ITP 115, Fall 2021
# Section: Boba
# Assignment 6
# Description:
# This program displays a jumbled word to the users and has them the word until correct.
# The program offers hints and also displays the number of guesses took.

# import random module
import random

# list of strings
wordList = ["python", "candy", "coffee", "traveler"]
hintList = ["code", "sweets", "caffeine", "horse"]

# get random word and corresponding hint
wordRandom = random.choice(wordList)  # get random word from list
wordIndex = wordList.index(wordRandom)  # get the index for the random word
hint = hintList[wordIndex]  # get corresponding hint

# making random word into jumbled word
word = list(wordRandom)  # make str into list since str is immutable
jumbled = ""
length = len(word)

# loop to create jumbled word
while length != 0:
    letter = random.choice(word)  # getting random letter from random word
    jumbled += letter  # adding the letter to the empty string/jumbled to create jumbled word
    word.remove(letter)  # remove letter from list
    length = len(word)

# print jumbled word
print("The jumbled word is \"" + jumbled + "\"")

# asking for guess
guess = input("Enter your guess: ")
guess = guess.lower()

# counting number of guesses
count = 1

# while loop to allow multiple guesses
# loops until the user gets word correct
while guess != wordRandom:
    count += 1  # adding count for each guess
    print("This is not correct")
    question = input("Do you want a hint (y or n)? ")
    if question.lower() == "y":
        # print hint
        print("The hint is \"" + hint + "\"")
    print("The jumbled word is \"" + jumbled + "\"")
    guess = input("Enter your guess: ")
    guess = guess.lower()

# print output after loop
print("You got it!")
print("It took you", count, "guesses.")
