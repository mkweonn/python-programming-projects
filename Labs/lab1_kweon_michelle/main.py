# Michelle Kweon, mkweon@usc.edu
# ITP 115, Fall 2021
# Section: 31805
# Lab 1

# print quote
print("\"It always seems impossible until it's done.\"")
print("- Nelson Mandela")

# get input from user
# input () always returns as string
day = input("Enter the day of the week: ")
month = input("Enter the month: ")
date = int(input("Enter the date: "))
next = date + 1

# output to the user
print("Today is " + day + ", " + month + " " + str(date) + ".")
print("Tomorrow will be " + month + " " + str(next) + ".")
