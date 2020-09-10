# Cameron Walcott , cwalcott@usc.edu
# ITP 115, Spring 2020
# Assignment 5
# Description:
# This program shuffles the letters in a word in a list/wordbank and the user inputs their guesses as to what the word is.

import random

def main():
    words = ["dolphin","snake","whale","elephant","gorilla","cheetah","turtle"]
    selection = random.choice(words)
    correct = selection

    jumble = " "
    turns = 0
    #for letter in selection:
    n = 1
    while selection:
        position = random.randrange(len(selection))
        jumble += selection[position]
        selection = selection[:position] + selection[(position + 1):]

    print("The jumbled word is: " , '"'+ jumble + '"')
    guess = input("Please enter your guess: ")

    while n != 0:
        turns = turns + 1
        #print(jumble)
        if guess == correct:
            print("You got it!")
            if turns == 1:
                print("It took you " + str(turns) + " try.")
            else:
                print("It took you " + str(turns) + " tries.")
            n = 0
        else:
            print("Try again.")
            guess = input("Please enter your guess: ")
main()
