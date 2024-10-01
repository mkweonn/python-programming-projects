# Michelle Kweon, mkweon@usc.edu
# ITP 115, Fall 2021
# Section: Boba
# Final Project
# interface.py
# Description:
# This file defines functions that will be called from other functions in another Python File.
# This file functions gets the menu dictionary, displays the menu, gets user input, and prints information about parks.
# The file also gets the state, prints the parks in state, prints largest park, and searches terms in each park data.

# import file
import tasks

# function getMenuDict
# parameters: None
# return value: dictionary where keys are letters for user to input and values are descriptions of menu options.
def getMenuDict():
    menuDict = {}  # create dictionary of choices
    menuDict["A"] = "All national parks"
    menuDict["B"] = "Parks in a particular state"
    menuDict["C"] = "The largest park"
    menuDict["D"] = "Search for a park"
    menuDict["Q"] = "Quit"
    return menuDict

# function displayMenu: prints menu to user
# parameters: menuDict is a dictionary for menu
# return value: none
def displayMenu(menuDict):
    for key in menuDict:
        print(key + " -> " + menuDict[key])

# function getUserInput
# parameters: menuDict is dictionary for menu
# return value: string that is a valid choice entered by user
def getUserInput(menuDict):
    choice = input("Choice: ")
    choice = choice.upper()
    while choice not in menuDict:
        choice = input("Choice: ")
        choice = choice.upper()
    return choice

# function printAllParks
# parameters: parkList is a list of the parks where each park is a dictionary
# return value: none
def printAllParks(parkList):
    for park in parkList:
        print(park["Name"] + " (" + park["Code"] + ")")
        print("\tLocation: " + park["State"])
        print("\tArea: " + park["Acres"] + " acres")
        dataStr = park["Date"]
        print("\tDate Established: " + tasks.getDate(dataStr))

# function getState: get user input for a state
# parameters: none
# return value: string with a two-letter abbreviation of a state
def getState():
    state = input("Enter a state: ")
    state = state.upper()
    while len(state) != 2:
        print("Need the two letter abbreviation")
        state = input("Enter a state: ")
        state = state.upper()
    return state

# function printParksInState
# parameter: parksList is list containing parks which are each represented with a dictionary object
# return value: none
def printParksInState(parksList):
    state = getState()
    parkFound = 0
    for park in parksList:
        if state in park["State"]:
            print(park["Name"] + " (" + park["Code"] + ")")
            print("\tLocation: " + park["State"])
            print("\tArea: " + park["Acres"] + " acres")
            dataStr = park["Date"]
            print("\tDate Established: " + tasks.getDate(dataStr))
            parkFound = 1
    if parkFound == 0:
        print("There are no national parks in " + state + " or it is not a valid state.")

# function printLargestPark
# parameter: parksList is list containing parks which are each represented with a dictionary object
# return value: none
def printLargestPark(parksList):
    codeLarge = tasks.getLargestPark(parksList)
    for park in parksList:
        if codeLarge in park["Code"]:
            print(park["Name"] + " (" + park["Code"] + ")")
            print("\tLocation: " + park["State"])
            print("\tArea: " + park["Acres"] + " acres")
            dataStr = park["Date"]
            print("\tDate Established: " + tasks.getDate(dataStr))
            print("\tDescription: " + park["Description"])

# function printParksForSearch
# parameter : parksList is list containing parks which are each represented with a dictionary object
# return value: none
def printParksForSearch(parksList):
    print()
    search = input("Enter text for searching: ")
    search = search.lower()
    parkFound = 0
    for park in parksList:
        if search in park["Code"].lower() or search in park["Name"].lower() or search in park["Description"].lower():
            print()
            print(park["Name"] + " (" + park["Code"] + ")")
            print("\tLocation: " + park["State"])
            print("\tArea: " + park["Acres"] + " acres")
            dataStr = park["Date"]
            print("\tDate Established: " + tasks.getDate(dataStr))
            print("\tDescription: " + park["Description"])
            parkFound = 1
    if parkFound == 0:
        print("There are no national parks for the search text of '" + search + "'.")