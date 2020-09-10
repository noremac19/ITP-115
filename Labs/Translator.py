# Cameron Walcott
# ITP 115, Spring 2020
# Assignment 9
# Description:
# Describe what this program does.

# Reads first line of file and stores it into a list
def getLanguages(fileName="languages.csv"):
    fileIn = open(fileName, "r")
    languages = fileIn.readline()
    lang = languages.strip()
    langList = lang.split(",")
    fileIn.close()
    return langList

#
def getSecondLanguage(langList):
    copy = getLanguages()
    i = 0
    copy.remove("English")
    print("Language Translator")
    print("Translate English words to one of the following languages:")
    # prints list of languages
    for language in copy:
        if i == 7:
            print("\t")
            print('\t' + language, end=" ")
        elif i == 0:
            print('\t' + language, end=" ")
        elif i == 14:
            print(language)
        else:
            print(language, end=" ")
        i += 1
    print()
    # gets language for translation and checks to see if the language is in file
    second = input("What language would you like to translate into?: ")
    second = second.capitalize()
    if second in langList:
        return second
    else:
        print("This program does not support", second)
        yes = True
        # Keeps requesting user input until valid value is chosen
        while yes:
            next = input("What language?: ")
            next = next.capitalize
            if next in langList:
                return next
            else:
                print("This program does not support",next)

# Reads in a file and finds the index where the second language resides
# Then creates and appends to a list of the words in stated language
def readFile(langList, langStr, fileName="languages.csv"):
    fileIn = open(fileName, "r")
    ind = langList.index(langStr)
    specific = []
    fileIn.readline()
    for line in fileIn:
        line = line.strip()
        info = line.split(",")
        specific.append(info[ind])
    fileIn.close()
    return specific

# Creates file that will be written on containing the translations
def createResultsFile(language, fileName="results.txt"):
    fileOut = open(fileName, "w")
    print("Words translated from English to" , language , file=fileOut)
    fileOut.close()

# Finds the respective translation for each english word inputted thst is in the list
def translateWords(englishList,secondList,resultsFile):
    fileOut = open(resultsFile,"a")
    cont = True
    word = input("Enter an English word to translate: ")
    # Loops if user wishes to translate more words
    while cont:
        # checks to see if inputted word is in the list of english words
        if word in englishList:
            spot = englishList.index(word)
            # checks if there is a translation for the inputted word in the second language
            # If not then statement is printed to recognize this occurrence
            if secondList[spot] == "-":
                print("There is no translation for", word + ".")
            else:
                print(word, "is translsted to", secondList[spot])
                print(word , "=" , secondList[spot] , file=fileOut)
        elif word not in englishList:
            print(word,"is not in the English List.")
        # Asks if the user wants to translate another word
        another = input("Another word (y/n)? ")
        if another.lower() == "n":
            cont = False
        elif another.lower() == "y":
            word = input("Enter an English word to translate: ")
        else:
            true = True
            n = 0
            y = 0
            # Nested while loop that repeats request for user input until valid value is chosen
            while true:
                other = input("Another word (y/n)? ")
                if other.lower() == "n":
                    n = 1
                    true = False
                elif other.lower() == "y":
                    y = 1
                    true = False
            if n == 1:
                cont = False
            elif y == 1:
                word = input("Enter an English word to translate: ")
    fileOut.close()

def main():
    lengua = getLanguages("languages.csv")
    english = readFile(lengua, "English", "languages.csv")
    trans = getSecondLanguage(lengua)
    allwords = readFile(lengua, trans, "languages.csv")

    file = input("Enter a name for the results file (return key for (Language).txt): ")
    # creates name for results file
    newname = trans + ".txt"
    # Creates reults file based on whether user entered filename or hit enter key
    if file == "":
        createResultsFile(trans, newname)
        translateWords(english, allwords, newname)
        print("Translated words have been saved to", newname)
    else:
        createResultsFile(trans,file)
        translateWords(english,allwords,file)
        print("Translated words have been saved to" , file)

main()


