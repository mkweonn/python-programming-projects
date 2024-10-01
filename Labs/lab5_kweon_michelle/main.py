# Michelle Kweon, mkweon@usc.edu
# ITP 115, Fall 2021
# Section: Boba
# Lab 5
# Description:
# This program uses lists and random library to generate a sentence.

# import random module
import random

# create 3 lists
nouns = ["pig", "tree", "door", "lamp", "computer"]
verbs = ["danced", "jumped", "swam", "crashed"]
articles = ["a", "an", "the"]

print("Welcome to the Sentence Generator")

# while loop - execute at least once (do while)
choice = 0
while choice != 5:
    # print menu
    print("\nMenu")
    print("1) View Words")
    print("2) Add Noun")
    print("3) Remove Verb")
    print("4) Generate Sentence")
    print("5) Exit")

    # get used input that is an integer
    choice = int(input("> "))

    # use branching
    if choice == 1:
        # view words
        print("articles:", articles)
        print("nouns:", nouns)
        print("verbs:", verbs)
    elif choice == 2:
        # add noun
        new_noun = input("Enter a noun: ")
        nouns.append(new_noun)
    elif choice == 3:
        # remove verb
        bad_verb = input("Enter a verb: ")
        # check to see if bad_verb is in the list of verbs
        if bad_verb in verbs:
            verbs.remove(bad_verb)
            print("verbs:", verbs)
        else:
            print(bad_verb, "is not in the list of verbs")
    elif choice == 4:
        # generate a sentence
        # ARTICLE NOUN VERB ARTICLE NOUN
        art1 = random.choice(articles)
        art2 = random.choice(articles)
        noun1 = random.choice(nouns)
        noun2 = random.choice(nouns)
        verb_random = random.choice(verbs)
        print(art1, noun1, verb_random, art2, noun2)
    elif choice == 5:
        print("Thank you for using the Sentence Generator!")
    else:
        print("Invalid choice.")