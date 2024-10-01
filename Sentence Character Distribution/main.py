# Michelle Kweon, mkweon@usc.edu
# ITP 115, Fall 2021
# Section: Boba
# Assignment 5
# Description:
# This program prints the character distribution of a user's sentence with asterisks(*).
# The program uses for for loops, nested loops, and branching.

alphabet = "abcdefghijklmnopqrstuvwxyz"

# menu and user input
print("Character Distribution")
number = int(input("Enter the number of times to run: "))

# outer range-based for loop to determine number of times to run
for run in range(number):
    # user input
    sentence = input("\nEnter a sentence: ")
    sentence = sentence.lower()
    count = 0 # starting variable to count special variables
    asterisk = "*"

    # loop to count special characters
    for letter in sentence:
        if letter not in alphabet: 
            if letter != " ":
                count += 1

    # print output for special characters
    if count > 0:
        print("Special characters:", count * asterisk )
    else:
        print("Special Characters: NONE")

    # loop to count letters in alphabet
    for letter in alphabet:
        countLetter = 0 # starting variable to count each letter
        for character in sentence: # nested loop
            if letter == character:
                countLetter += 1
        # print output for each letter
        if countLetter > 0:
            print(letter + ": " + asterisk * countLetter)
        else:
            print(letter + ": NONE")