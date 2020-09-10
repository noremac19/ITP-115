# Cameron Walcott , cwalcott@usc.edu
# ITP 115, Spring 2020
# Lab 10-1

# fileIn = open("words.txt","r")

def readDictionaryFile(fileName):
    wordList = []
    fileIn = open(fileName,"r")
    for line in fileName:
        word = line.strip()
        wordList.append(word)
    fileIn.close()
    return wordList

def checkWord(dictionaryList,word):
    if word in dictionaryList:
        return True
    else:
        return False

def main():
    print("Welcome to the Spell Check!")
    userFile = input("Please enter the dictionary file")
    list = readDictionaryFile(userFile)
    userWord = input("Please enter word you wish to spell check: ")
    validWord = checkWord(list,userWord)
    if validWord:
        print("That word is in the dictionary.")
    else:
        print("That word is not in the dictionary, so it must be spelled wrong.")
main()