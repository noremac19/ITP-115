# Cameron Walcott , cwalcott@usc.edu
# ITP 115, Spring 2020
# Lab 10-2

def readFile(fileName="people.csv"):
    nameList = []
    fileIn = open(fileName, "r")
    for line in fileIn:
        line = line.strip()
        info = line.split(",")
        age = int(info[3])
        if age < 30:
            nameList.append(info[0])

    fileIn.close()
    return nameList

def writeFile(outputList, fileName="output.txt"):
    fileOut = open(fileName, "w")
    for name in outputList:
        print(name,file=fileOut)
    fileOut.close()

    num = len(outputList)
    print(num, "names were written to", fileName)

def main():
    csvFile = input("Enter the name of the csv file: ")
    outputFIle = input("Enter the name of the iutput file: ")
    if csvFile: # a non empty string for csv file
        names = readFile(csvFile)
    else:
        names = readFile()
    #print(names)

    if outputFIle:
        writeFile(names,outputFIle)
    else:
        writeFile(names)
main()