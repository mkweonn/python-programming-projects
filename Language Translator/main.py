# Michelle Kweon, mkweon@usc.edu
# ITP 115, Fall 2021
# Section: Boba
# Assignment 9
# Description:
# This language translator program translates English words to another language.
# The program reads data from a CSV file with 15 languages and writes data to another file.

# function: getLanguages
# parameter: fileName is a str containing the name of a CSV file to read from. It has a default value
# return value: list of strings representing the languages in the header row
def getLanguages(fileName="languages.csv"):
    openFile = open(fileName, "r")
    headerRow = openFile.readline()
    headerRow = headerRow.strip()
    listLanguages = headerRow.split(",")
    openFile.close()
    return listLanguages

# function: getTranslationLanguage
# parameter: langList is a list of the languages
# return value: str for the language to translate words into
def getTranslationLanguage(langList):
    langList = langList[1:16]
    langString = " ".join(langList)
    print("Translate English words to one of the following languages:")
    print(langString)
    choice = input("Enter a language: ")
    choice = choice.capitalize()
    while choice not in langList:
        print("This program does not support", choice)
        choice = input("Enter a language: ")
        choice = choice.capitalize()
    return choice

# function: readFile
# parameter 1: langList is a list of the languages
# parameter 2: langStr is a str containing name of a language. It has a default value of "English"
# parameter 3: fileName is a str containing name of a CSV file to read from. It has a default value
# return: list of words in the language identified by the langStr parameter
def readFile(langList, langStr="English", fileName="languages.csv"):
    wordList = []
    openFile = open(fileName, "r")
    openFile.readline()  # skip header row
    langIndex = langList.index(langStr)
    for line in openFile:
        line = line.strip()
        lineList = line.split(",")
        wordList.append(lineList[langIndex])
    openFile.close()
    return wordList

# function: createResultsFile
# parameter: language is a str containing the name of the language for translation
# return value: none
def createResultsFile(language):
    resultsFile = language + ".txt"
    outFile = open(resultsFile, "w")
    print("Words translated from English to " + language, file=outFile)
    outFile.close()

# function: translateWords
# parameter 1: englishList is a list of words in English
# parameter 2: translationList is a list of words in another language (not English)
# parameter 3: language is a str containing the language of the words in translationList
# return value: none
def translateWords(englishList, translationList, language):
    outFile = open(language + ".txt", "a")
    anotherWord = True
    while anotherWord == True:
        word = input("\nEnter a word to translate: ")
        if word not in englishList:
            print(word, "is not in the list")
        else:
            englishIndex = englishList.index(word)
            translation = translationList[englishIndex]
            if translation == "-":
                print(word, "did not have a translation")
            else:
                print(word, "is translated to", translation)
                print(word + " = " + translation, file=outFile)

        # asking user if they want to translate another word
        anotherWord = input("Another word (y or n)? ")
        if anotherWord.lower() == "y":
            anotherWord = True
        else:
            anotherWord = False

    print("\nTranslated words have been saved to " + language + ".txt")
    outFile.close()

def main():
    print("Language Translator")
    languageList = getLanguages()
    englishList = readFile(languageList)
    translationChoice = getTranslationLanguage(languageList)
    translationList = readFile(languageList, translationChoice)
    createResultsFile(translationChoice)
    translateWords(englishList, translationList, translationChoice)
main()



