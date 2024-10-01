# Michelle Kweon, mkweon@usc.edu
# ITP 115, Fall 2021
# Section: Boba
# Lab 3
# Description:
# This program uses a while loop and branching to respond to user input.

# while loop
answer = ""

# What condition causes us to stop looping?
while answer != "q" and answer != "Q":
    # print menu
    print("\nWhat would you like to know?")
    print("a) Favorite Animal")
    print("c) Favorite Color")
    print("f) Favorite Food")
    print("q) Quit")
    answer = input("> ")

    # branching
    if answer == "a" or answer == "A":
        print("My favorite animal is a dolphin.")
    elif answer == "c" or answer == "C":
        print("My favorite color is green.")
    elif answer == "f" or answer == "F":
        print("My favorite food is chocolate.")
    elif answer == "q" or answer == "Q":
        print("Goodbye")
    else:
        print("That option is not available.")


