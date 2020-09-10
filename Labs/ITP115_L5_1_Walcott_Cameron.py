# Cameron Walcott
# ITP 115, Spring 2020
# Lab 5


# Welcome to the Sentence Generator
#  Menu
#  1) View Words
#  2) Add Words
#  3) Remove Words
#  4) Generate Sentence
#  5) Exit

# Enter 1) for nouns or 2) for verbs: 1
# Enter the word:

# Invalid choice.

# Program will exit
# Have a great day!

import random

articles = ['a', 'the']
nouns = ['person', 'place', 'thing']
verbs = ['danced', 'ate', 'frolicked']

decision = 0
while decision != 5:
    print("Welcome to the Sentence Generator")
    print('\t' + "Menu")
    print('\t' + "1) View Words")
    print('\t' + "2) Add Words")
    print('\t' + "3) Remove")
    print('\t' + "4) Generate Sentence")
    print('\t' + "5) Exit" + '\n')

    decision = int(input())

    if decision == 1:
        print("articles: " , articles)
        print("nouns: " , nouns)
        print("verbs: " , verbs)
    elif decision == 2:
        type = int(input("Enter 1) for nouns or 2) for verbs: "))
        if type == 1:
            noun = input("Enter a noun: ")
            nouns.append(noun)
        else:
            verb = input("Enter a verb: ")
            verbs.append(verb)

    elif decision == 3:
        type = int(input("Enter 1) for nouns or 2) for verbs: "))
        if type == 1:
            noun = input("Enter a noun: ")
            # check if noun is in array
            nouns.remove(noun)
        else:
            # check if very is in array
            verb = input("Enter a verb: ")
            verbs.remove(verb)
    elif decision == 4:
        art1 = random.choice(articles)
        noun1 = random.choice(nouns)
        verb1 = random.choice(verbs)
        art2 = random.choice(articles)
        noun2 = random.choice(nouns)
        print(art1,noun1,verb1,art2,noun2)
    elif decision == 5:
        print("Program will exit")
        print("Have a great day!")
        break
    else:
        print("Invalid choice.")
        continue


