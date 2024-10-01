# Michelle Kweon, mkweon@usc.edu
# ITP 115, Fall 2021
# Section: Boba
# Final Project
# main_kweon_michelle.py
# Description:
# This file acts as the point of execution for the program.
# The program as a whole allows the user to get information and learn about national parks.

# import files
import tasks
import interface

def main():
    print("National Parks")
    parksList = tasks.createListOfParks()  # list of dictionaries holding information for one national park.
    choice = ""
    while choice != "Q":
        print()
        menuDict = interface.getMenuDict()
        interface.displayMenu(menuDict)
        choice = interface.getUserInput(menuDict)
        if choice == "A":
            interface.printAllParks(parksList)
        elif choice == "B":
            interface.printParksInState(parksList)
        elif choice == "C":
            interface.printLargestPark(parksList)
        elif choice == "D":
            interface.printParksForSearch(parksList)

main()