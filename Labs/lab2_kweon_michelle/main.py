# Michelle Kweon, mkweon@usc.edu
# ITP 115, Fall 2021
# Section: Boba
# Lab 2
# Description:
# This program gets user input and uses branching to output Chinese zodiac animals.

# title
print("Chinese Zodiac")
print()

# get input from the user
year = int(input("Enter year: "))

# use modulus operator and create variable
zodiac = year % 12

# use branching to map number to animal
if zodiac == 0:
    animal = "Monkey"
elif zodiac == 1:
    animal = "Rooster"
elif zodiac == 2:
    animal = "Dog"
elif zodiac == 3:
    animal = "Pig"
elif zodiac == 4:
    animal = "Rat"
elif zodiac == 5:
    animal = "Ox"
elif zodiac == 6:
    animal = "Tiger"
elif zodiac == 7:
    animal = "Rabbit"
elif zodiac == 8:
    animal = "Dragon"
elif zodiac == 9:
    animal = "Snake"
elif zodiac == 10:
    animal = "Horse"
else:
    animal = "Goat"

# output animal to user
print(str(year) + " is the Year of the " + animal)
