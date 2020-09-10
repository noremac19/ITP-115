# Cameron Walcott , cwalcott@usc.edu
# ITP 115, Spring 2020
# Assignment 10
# Description:
# Describe what this program does.

class Animal(object):
    #set up constructors/ which attributes will exist within the animalobject
    def __init__(self,hunger,happiness,health,energy,animalAge,name,species):
        self.hung = int(hunger)
        self.happy = int(happiness)
        self.heal = int(health)
        self.ener = int(energy)
        self.age = int(animalAge)
        self.nme = name
        self.spec = species
    # play,feed,giveMedicine, and sleep are a series of methods that change attribute values
    def play(self):
        self.happy += 10
        self.hung += 5

    def feed(self):
        self.hung -= 10

    def giveMedicine(self):
        self.happy -= 20
        self.heal += 20

    def sleep(self):
        self.ener += 20
        self.age += 1
    # creates a string that will be printed when the object is printed
    def __str__(self):
        strna = "Name: " + self.nme + " the " + self.spec
        strhe = "Health: " + str(self.heal)
        strha = "Happiness: " + str(self.happy)
        strhu = "Hunger: " + str(self.hung)
        stren = "Energy: " + str(self.ener)
        strag = "Age: " + str(self.age)
        msg = strna +'\n'+ strhe +'\n'+ strha +'\n'+ strhu +'\n'+ stren +'\n'+ strag
        msg += '\n' + "********************************"
        return msg


def loadAnimals(fileName="animals.csv"):
    animalObjects = []
    contents = []
    # opens file
    inFile = open(fileName,"r")
    # reads the file and puts each line into an index in a list
    for line in inFile:
        line = line.strip()
        contents.append(line)
    # gathers the info from the contents list and puts each comma separated value
    # in the correct variable
    for line in contents:
        info = line.split(",")
        hunger = info[0]
        happiness = info[1]
        health = info[2]
        energy = info[3]
        age = info[4]
        name = info[5]
        species = info[6]
        # creates an object with vsriables
        animalObjects.append(Animal(int(hunger),int(happiness),int(health),int(energy),int(age),name,species))
    inFile.close()
    # returns a list of animal objects
    return animalObjects

def displayMenu():
    # prints a menu of possible/reccommended user inputs
    print("1) Play")
    print("2) Feed")
    print("3) Give Medicine")
    print("4) Sleep")
    print("5) Print an Animal's stats")
    print("6) View All Animals")
    print("7) Exit" + '\n')

def selectAnimal(listAnimals):
    # Prints the list of animals and their names
    num = 1
    for animal in listAnimals:
        msg = str(num) + ") " + animal.nme + " the " + animal.spec
        print(msg)
        num += 1

    true = True
    ani = 0
    while true:
        # receives the input from user about which animal they choose
        ani = int(input("Please select an animal from the list (enter the 1-5): "))
        if ani == 1:
            true = False
        elif ani == 2:
            true = False
        elif ani == 3:
            true = False
        elif ani == 4:
            true = False
        elif ani == 5:
            true = False
        else:
            print("Invalid input, please try again!")

    return listAnimals[ani-1].spec

def writeToFile(animales,fileName = "results.csv"):
    # creates file and loops through list of animal objects and places
    # each attribute into a variable
    outFile = open(fileName,"w")
    for item in animales:
        shung = item.hung
        shappy = item.happy
        sheal = item.heal
        sener = item.ener
        sage = item.age
        snme = item.nme
        sspec = item.spec
        # concanates elements to create a comma separated list of elements
        line = str(shung)+","+str(shappy)+","+str(sheal)+","+str(sener)+","+str(sage)+","+snme+","+sspec
        line = line.strip()
        # prints each line to output file
        print(line, file=outFile)
    outFile.close()
def main():
    # asks user for filename of their choice of .csv file with data
    file = input("Please enter filename (add '.csv' to end of string)")
    if file == "":
        list = loadAnimals()
    else:
        list = loadAnimals(file)

    print("Welcome to the Animal Daycare! Here is what we can do:" + '\n')
    cont = True
    while cont:
        displayMenu()
        # Asks which method the user wants to use from the list in displayMenu
        slatt = input("Please make a selection: ")
        if slatt == "1":
            index = 0
            selection = selectAnimal(list)
            for item in list:
                # checks if the animal returned from selectAnimal is in the list
                # of animal objects and finds the index in the animal objects list
                # where selection is
                if item.spec == selection:
                    index = list.index(item)
            # Performs method function and changes object attribute values
            list[index].play()
            print("You played with "+list[index].nme + " the " + list[index].spec+"!")
        elif slatt == "2":
            index = 0
            selection = selectAnimal(list)
            for item in list:
                # checks if the animal returned from selectAnimal is in the list
                # of animal objects and finds the index in the animal objects list
                # where selection is
                if item.spec == selection:
                    index = list.index(item)
            # Performs method function and changes object attribute values
            list[index].feed()
            print("You fed " + list[index].nme + " the " + list[index].spec + "!")
        elif slatt == "3":
            index = 0
            selection = selectAnimal(list)
            for item in list:
                # checks if the animal returned from selectAnimal is in the list
                # of animal objects and finds the index in the animal objects list
                # where selection is
                if item.spec == selection:
                    index = list.index(item)
            # Performs method function and changes object attribute values
            list[index].giveMedicine()
            print("You gave " + list[index].nme + " the " + list[index].spec + " some medicine!")
        elif slatt == "4":
            index = 0
            selection = selectAnimal(list)
            for item in list:
                # checks if the animal returned from selectAnimal is in the list
                # of animal objects and finds the index in the animal objects list
                # where selection is
                if item.spec == selection:
                    index = list.index(item)
            # Performs method function and changes object attribute values
            list[index].sleep()
            print(list[index].nme + " the " + list[index].spec + " took a nap!")
        elif slatt == "5":
            selection = selectAnimal(list)
            index = 0
            for item in list:
                # checks if the animal returned from selectAnimal is in the list
                # of animal objects and finds the index in the animal objects list
                # where selection is
                if item.spec == selection:
                    index = list.index(item)
            # prints the __str__ method value, which is all the values of the attributes
            # in the specific object
            print(list[index])
        elif slatt == "6":
            # prints all of the all the values of the attributes of all objects
            # by using the __str__ method
            for item in list:
                stats = item.__str__()
                print(stats)
        # breaks out of while loop
        elif slatt == "7":
            cont = False
        else:
            end = 0
            true = True
            # instance if the user enters a value other than numbers 1-7
            # the program will loop until a correct input is inputted
            # Identical to while loop that surrounds it
            while true:
                print("*Invalid selection, please try again.")
                displayMenu()
                slatt = input("Please make a selection: ")
                if slatt == "1":
                    index = 0
                    selection = selectAnimal(list)
                    for item in list:
                        if item.spec == selection:
                            index = list.index(item)
                    list[index].play()
                    print("You played with " + list[index].nme + " the " + list[index].spec + "!")
                    true = False
                elif slatt == "2":
                    index = 0
                    selection = selectAnimal(list)
                    for item in list:
                        if item.spec == selection:
                            index = list.index(item)
                    list[index].feed()
                    print("You fed " + list[index].nme + " the " + list[index].spec + "!")
                    true = False
                elif slatt == "3":
                    index = 0
                    selection = selectAnimal(list)
                    for item in list:
                        if item.spec == selection:
                            index = list.index(item)
                    list[index].giveMedicine()
                    print("You gave " + list[index].nme + " the " + list[index].spec + " some medicine!")
                    true = False
                elif slatt == "4":
                    index = 0
                    selection = selectAnimal(list)
                    for item in list:
                        if item.spec == selection:
                            index = list.index(item)
                    list[index].sleep()
                    print(list[index].nme + " the " + list[index].spec + " took a nap!")
                    true = False
                elif slatt == "5":
                    selection = selectAnimal(list)
                    index = 0
                    for item in list:
                        if item.spec == selection:
                            index = list.index(item)
                    print(list[index])
                    true = False
                elif slatt == "6":
                    for item in list:
                        stats = item.__str__()
                        print(stats)
                    true = False
                #breaks out of inner while loop
                elif slatt == "7":
                    end = 1
                    true = False
            # breaks out of outer while loop
            if end == 1:
                cont = False

    print("Goodbye!")
    # creates and writes data stored in the animal objects list to a .csv file
    writeToFile(list,)

main()