# Michelle Kweon, mkweon@usc.edu
# ITP 115, Fall 2021
# Section: 31805
# Assignment 2
# Description:
# This program creates a Mad Libs story.
# It gets input from the user and prints output.

# obtain user input and store them in variables
# these variables are used for the Mad Libs story
# convert numbers for mathematical calculation to int
noun = input("Enter a person or animal: ")
adj = input("Enter an adjective: ")
food = input("Enter a plural food: ")
verb = input("Enter a verb: ")
place = input("Enter a place: ")
emotion = input("Enter emotion: ")
decimal = float(input("Enter a number with a decimal: "))
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a second number: "))
num3 = num1 + num2
num4 = int(input("Enter a third number: "))
print()

# Mad Libs Story
# output information to user using escape characters
# convert float and ints to str
print("Today is my \"" + noun + "\"'s birthday.")
print("I decided to make him/her \"" + adj + "\" \"" + food + "\".")
print("My \"" + noun + "\" went to go \"" + verb + "\", so I had \"" + str(decimal) + "\" hours to make the \"" + food + "\".")
print("I invited \"" + str(num1) +"\" people to the \"" + place + "\" for the party, but \"" + str(num2) + "\" guests showed up.")
print("There were \"" + str(num3) + "\" people at the \"" + place + "\".")
print("I only made \"" + str(num4) + "\" \"" + food + "\".")
print("I hope no one gets \"" + emotion + "\".")