# Michelle Kweon, mkweon@usc.edu
# ITP 115, Fall 2021
# Section: Boba
# Assignment 4
# Description:
# This program gets user input for a unknown amount numbers and quits when -1 is entered.
# This program determines the smallest and largest number entered.

# set initial variables
small = 0
large = 0
count = 0
sum = 0
num = 0
count2 = 1 # count2 = 1 to leave out "-1/quit" in count
question = "y" # declare a variable for do while loop

# print to user
print("Input an integer greater than or equal to 0 (-1 to quit):")

# while loops with condition that causes us to stop looping
while question == "y" or question == "Y": # condition for second outer loop
    while num != -1: # inner while loop
        # user input
        if count2 == 1:
            num = int(input("> "))
            small = num

        # branching to find large and small numbers
        if num > large:
            large = num
        elif num < small and count != 0 and num != -1:
            small = num
        if count == 0:  # condition in order to prevent small = 0 if 0 not entered
            small = num

        # arithmetic to find average number
        sum = sum + num
        count = count + 1
        count2 = count2 + 1

        num = int(input("> "))

    # leave while loop
    average = sum / count

    # print output
    print("The largest number is " + str(large))
    print("The smallest number is " + str(small))
    print("The average number is " + str(average))
    print()

    # new set of inputs
    question = input("Would you like to enter another set of numbers (y/n)?: ")
    if question == "y" or question == "Y":
        print("Input an integer greater than or equal to 0 (-1 to quit):")
        # new variables to reset
        small = 0
        large = 0
        count = 0
        sum = 0
        num = 0
        count2 = 1

# if question != yes leave while loop and stop
print()
print("Goodbye!")