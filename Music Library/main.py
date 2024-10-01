# Michelle Kweon, mkweon@usc.edu
# ITP 115, Fall 2021
# Section: Boba
# Assignment 10
# Description:
# This program manages a user's music library which is represented using a dictionary.
# The keys in dictionary are artists' names (str) and each value is list of albums (str).
# The program also saves a dictionary/user's library to a binary file.

# import files/modules
import MusicLibraryHelper
import random

# function displayMenu: print menu option to the user
# parameter: none
# return value: none
def displayMenu():
    print("\nManage Your Music Library")
    print("\ta) Display library")
    print("\tb) Display artists")
    print("\tc) Add an artist/album")
    print("\td) Delete an album")
    print("\te) Delete an artist")
    print("\tf) Generate a random playlist")
    print("\tg) Exit")

# function displayLibrary: print out entire music library of artists/albums
# parameter: dictionary representing the music library
# return value: none
def displayLibrary(dictionary):
    # print artists
    for key in dictionary:
        print("Artist: " + key)
        print("\tAlbums: ")
        value = dictionary[key]
        # print albums
        for album in value:
            print("\t\t" + album)

# function displayArtists: print out the artists in the music library
# parameter: dictionary representing the music library
# return value: none
def displayArtists(dictionary):
    print("Artists: ")
    for key in dictionary:
        print("\t" + key)

# function addAlbum: get user input for artist name and album name they want to add
# parameter: dictionary representing the music library
# return value: none
def addAlbum(dictionary):
    artist = input("Enter artist: ")
    artist = artist.title()
    album = input("Enter album: ")
    album = album.title()
    if artist in dictionary:
        if album not in dictionary[artist]:  # add to existing list of albums
            dictionary[artist].append(album)
    if artist not in dictionary:
        dictionary[artist] = [album]

# function deleteAlbum: get user input for artist name and album name they want to delete
# parameter: dictionary representing the music library
# return value: boolean (True if album successfully deleted. False if album not successfully deleted)
def deleteAlbum(dictionary):
    artist = input("Enter artist: ")
    artist = artist.title()
    album = input("Enter album: ")
    album = album.title()
    if artist in dictionary:
        if album in dictionary[artist]:
            dictionary[artist].remove(album)
            if len(dictionary[artist]) == 0:  # delete artist if no more albums in dictionary
                del dictionary[artist]
            return True
    if artist or album not in dictionary:
        return False

# function deleteArtist: get user input for artist name and album name that they want to delete
# parameter: dictionary representing the music library
# return value: boolean value (True if  artist successfully deleted. False if artist not successfully deleted)
def deleteArtist(dictionary):
    artist = input("Enter artist to delete: ")
    artist = artist.title()
    if artist in dictionary:
        del dictionary[artist]
        return True
    if artist not in dictionary:
        return False

# function generateRandomPlaylist: generate random playlist by randomly selecting one album from every artist in library
# parameter: dictionary representing the music library
# return value: none
def generateRandomPlaylist(dictionary):
    print("Here is your random playlist:")
    for key in dictionary:
        randomAlbum = random.choice(dictionary[key])
        print("\t" + randomAlbum + " by " + key)

def main():
    libraryFileName = "musicLibrary.dat"  # initialize file name
    libraryDict = MusicLibraryHelper.loadLibrary(libraryFileName)
    choice = " "
    choices = "abcdefg"
    while choice != "g":
        displayMenu()
        choice = input("Choice: ")
        choice = choice.lower()
        if choice not in choices:  # user inputs invalid choice
            print("Invalid entry")
        else:
            if choice == "a":
                displayLibrary(libraryDict)
            elif choice == "b":
                displayArtists(libraryDict)
            elif choice == "c":
                addAlbum(libraryDict)
            elif choice == "d":
                if deleteAlbum(libraryDict) == True:
                    print("Delete album success")
                else:
                    print("Delete album failed")
            elif choice == "e":
                if deleteArtist(libraryDict) == True:
                    print("Delete artist success")
                else:
                    print("Delete artist failed")
            elif choice == "f":
                generateRandomPlaylist(libraryDict)

    libraryFileName = input("Enter a music filename: ")
    # save library
    MusicLibraryHelper.saveLibrary(libraryFileName, libraryDict)
    print("Saved music library to " + libraryFileName)

main()