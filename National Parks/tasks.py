# Michelle Kweon, mkweon@usc.edu
# ITP 115, Fall 2021
# Section: Boba
# Final Project
# tasks.py
# Description:
# This file defines functions that will be called from other functions in another Python file.
# The file functions creates a list of each park dictionary, gets the date, and gets the largest park.

# function createListOfParks
# parameter: fileName is CSV file name to read which has default value "national_parks.csv"
# return value: list of dictionary objects (keys: strs from header row and values: data from rest of CSV file)
def createListOfParks(fileName="national_parks.csv"):
    openFile = open(fileName, "r")  # read in CSV file
    headerRow = openFile.readline()  # get top header row for keys
    headerRow = headerRow.strip()
    listHeader = headerRow.split(",")
    parksList = []

    for line in openFile:
        parkDict = {}  # create dictionary holding information for one park
        lineList = line.strip().split(",")
        description = lineList[7:]  # slice to get full description after first comma
        descriptionStr = ",".join(description)
        descriptionStr = descriptionStr.strip("\"")
        lineList[7] = descriptionStr
        for item in listHeader:
            headerIndex = listHeader.index(item)
            parkDict[listHeader[headerIndex]] = lineList[headerIndex]  # add key/value into dictionary

        parksList.append(parkDict)  # create list of each park dictionary
    openFile.close()
    return parksList

# function getDate
# parameter: dataStr is a string containing the date (YYYY-MM-DD)
# return value: str with the date in the following format: Month Day, Year
def getDate(dataStr):
    data = dataStr.split("-")
    monthList = ["January", "February", "March", "April", "May", "June", "July", "August", "September",
                 "October", "November", "December"]
    month = int(data[1])
    monthStr = monthList[month-1]
    date = monthStr + " " + str(data[2]) + ", " + str(data[0])
    return date

# function getLargestPark
# parameter: parksList is a list of the parks where each park is a dictionary
# return value: a string that is the park code of the park with the largest area
def getLargestPark(parksList):
    largestAcre = 0
    code = ""

    for park in parksList:  # park is dictionary of one park
        acres = park.get("Acres")
        acresNum = int(acres)
        if acresNum > largestAcre:
            largestAcre = acresNum
            code = park.get("Code")
    return code