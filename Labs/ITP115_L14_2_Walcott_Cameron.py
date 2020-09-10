# Cameron Walcott
# ITP 115, Spring 2020 # Lab 14-2
# cwalcott@usc.edu

def readFile(fileName="story.txt"):
    wordDict = {}
    fileIn = open(fileName,"r")
    lineNum = 1

    for line in fileIn:
        line = line.strip()
        wordList = line.split()

        for word in wordList:
            word = word.lower()
            word = word.strip(".,;:?\'")
            if word in wordDict:
                wordDict[word].append(lineNum)
            else:
                wordDict[word] = [lineNum]
        lineNum += 1
    fileIn.close()
    return wordDict

def sortKeys(dictionary):
    dictKeys = dictionary.keys()
    dictKeys = list(dictKeys)
    dictKeys.sort()
    return dictKeys

def main():
    storyDict = readFile()

    storyKeys = sortKeys(storyDict)
    print("Here's the concordance:")
    for key in storyKeys:
        print(key + ":" , storyDict[key])

main()