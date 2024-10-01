# Michelle Kweon, mkweon@usc.edu
# ITP 115, Fall 2021
# Section: Boba
# Lab 6
# Description:
# This program determines if a users words/phrases are anagrams/palindrome.

# Anagram
print("Anagram")
# get 2 words from the user
word1 = input("Enter word #1: ")
word2 = input("Enter word #2: ")

# change the words to lower case
# strings are immutable
word1 = word1.lower()
word2 = word2.lower()

# remove white space from the beginning and end
word1 = word1.strip()
word2 = word2.strip()

# anagram = all letters are the same
# convert words to lists, alphabetize (sort) and compare
list1 = list(word1)
list2 = list(word2)
list1.sort() # no =, avoid NONE
list2.sort()

if list1 == list2:
    print("The words are anagrams!")
else:
    print("The words are NOT anagrams.")

# Palindrome
print("\nPalindrome")
# get a phrase from the user
phrase = input("Enter a phrase: ")

# convert to all lowercase
phrase = phrase.lower()

# remove spaces using new_str = str.replace(find_str, replace_str)
phrase = phrase.replace(" ", "")

# convert string to list
phrase_list = list(phrase)

# reverse the list
phrase_list.reverse()

# convert the list into a string
# new_str = sep.join(list)
sep = "" # empty string
phrase_reverse = sep.join(phrase_list)

# compare the two strings
if phrase == phrase_reverse:
    print("The phrase is a palindrome!")
else:
    print("The phrase is NOT a palindrome.")