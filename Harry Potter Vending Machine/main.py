# Michelle Kweon, mkweon@usc.edu
# ITP 115, Fall 2021
# Section: Boba
# Assignment 3
# Description:
# This program creates a Harry Potter vending machine.
# It determines the change to be returned using Harry Potter currency.

# Extra information:
# Harry Potter currency
# 1 knut = 1 knut
# 1 sickle = 29 knuts
# 1 galleon = 493 knuts

# print menu
print("Please select an item from the vending machine:")
print("\ta) Assortment of Candy for 11 sickles and 7 knuts")
print("\tb) Butterbeer for 2 sickles")
print("\tc) Quill for 6 sickles")
print("\td) Daily Prophet for 5 knuts")

# get user input for item
choice = input("Choice: ")

# branching statements for user choice
# Harry Potter conversion values are used to find cost
if choice == "a" or choice == "A":
    item = "Assortment of Candy"
    cost = (11 * 29) + 7
    print()
elif choice == "b" or choice == "B":
    item = "Butterbeer"
    cost = 2 * 29
    print()
elif choice == "c" or choice == "C":
    item = "Quill"
    cost = 6 * 29
    print()
elif choice == "d" or choice == "D":
    item = "Daily Prophet"
    cost = 5
    print()
else:
    print("You entered an invalid choice, thus the item selected is the Quill")
    item = "Quill"
    cost = 6 * 29
    print()

# get user input for payment
print("Please pay by entering the number of each coin")
galleon = int(input("Number of galleons: "))
sickle = int(input("Number of sickles: "))
knut = int(input("Number of knuts: "))
print()

# cost of the item in knuts
# conversion values are used to convert to knuts
print("Cost in knuts: " + str(cost))
payment = (galleon * 493) + (sickle * 29) + knut
print("Payment in knuts: " + str(payment))

# calculate amount of change using arithmetic operators and store into variable
change = payment - cost
changeG = change // 493
changeS = (change % 493) // 29
changeK = ((change % 493) % 29) // 1

# branching statement output
if payment < cost:
    print("You did not enter enough money and will not receive the " + item)
else:
    print()
    print("You purchased the " + item)
    print("Your change is " + str(change) + " knuts")
    print("You will be given")
    print("\tGalleons: " + str(changeG))
    print("\tSickles: " + str(changeS))
    print("\tKnuts: " + str(changeK))