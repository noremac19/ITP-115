# Cameron Walcott, cwalcott@usc.edu
# ITP 115, Spring 2020
# Lab 4-1
#Pig Elvish

import random
def main():
    cond = "y"
    print("Elcómewó óten heten Igpén Lvísheá ránslátórtë!")
    print("(Welcome to the Pig Elvish translator!)")
    while cond.lower() == "y":
        # Get user input for word
        word = input("Please enter a word you would like to translate:")
        # translate word

        # print translation
        elvish = ""
        index = 0
        let = ""
        #loop throught input
        for letter in word:
            if index == 0:
                let = letter
            else:
                elvish = elvish + letter
            index = index + 1

        elvish = elvish + let

        numLetters = len(word)

        if numLetters >= 4:
            vowel = random.choice("aeiou")
            elvish = elvish + vowel
        else:
            elvish = elvish + "en"

        elvish = elvish.replace("k","c")

        print("\"" + word + "\"" " in elvish is: " + elvish)
        # ask the user if they want another word translated
        cond = input("Would you like to translate another word? (y/n): ")

    print("Oodbyega! Aveha aen icenë ayden!")
    print("(Goodbye! Have a nice day!)")

main()