# Cameron Walcott
# ITP 115, Spring 2020
# Assignment 6
# Description:
# Use list, loops and conditional statements to construct an airport reservation algorithm.


def main():
    first =["", "", "", ""]
    economy = ["", "", "", "", "", ""]
    decision = 0
    numEconomy = 0
    numFirst = 0

    while decision != -1:
        print("1: Assign Seat" + '\n' + "2: Print Seat Map" + '\n' + "3: Print Boarding Pass" + '\n' + "-1: Quit")
        decision = int(input())
        if decision == 1:
            if numEconomy == 6 and numFirst == 4:
                print("Next flight leaves in 3 hours.")
            else:
                price = int(input("Type 1 for First Class or Type 2 for Economy. "))
                if price == 1:
                    if numFirst == 4:
                        switch = input("Would you like to select a seat in economy? (y/n): ")
                        if switch.lower() == "y":
                            economy[numEconomy] = input("Please enter your first name: ")
                            numEconomy += 1
                        else:
                            decision = -1
                    else:
                        first[numFirst] = input("Please enter your first name: ")
                        numFirst += 1
                elif price == 2:
                    if numEconomy == 6:
                        switch = input("Would you like to select a seat in first class? (y/n): ")
                        if switch.lower() == "y":
                            first[numFirst] = input("Please enter your first name: ")
                            numFirst += 1
                    else:
                        economy[numEconomy] = input("Please enter your first name: ")
                        numEconomy += 1
        if decision == 2:
            print("***************************************")
            print("First Class:")
            for num in range(len(first)):
                if first[num] == "":
                    print('\t' + "Seat #" + str(num+1) + ":" + '\t' + "Empty")
                else:
                    print('\t' + "Seat #" + str(num+1) + ":" + '\t' + first[num])
            print("Economy:")
            for num in range(len(economy)):
                if economy[num] == "":
                    print('\t' + "Seat #" + str(num + 5) + ":" + '\t' + "Empty")
                else:
                    print('\t' + "Seat #" + str(num + 5) + ":" + '\t' + economy[num])
            print("***************************************")
        if decision == 3:
            which = int(input("Type 1 to get Boarding Pass by seat number" + '\n' + "Type 2 to get Boarding Pass by name" + '\n'))
            if which == 1:
                seat = int(input("Please enter your seat number: "))
                if seat > 10:
                    print("Invalid number--no boarding pass found")
                else:
                    total = first + economy
                    print("======= BOARDING PASS =======")
                    print("First-Class Passenger")
                    print("Seat #: " + str(seat))
                    print("Passenger Name: " + total[seat - 1])
                    print("=============================")
            else:
                name = input("Please enter your first name: ")
                if name in first:
                    index = first.index(name)
                    seat = index + 1
                    print("======= BOARDING PASS =======")
                    print("First-Class Passenger")
                    print("Seat #" + ": " + str(index + 1))
                    print("Passenger Name: " + name)
                    print("=============================")
                elif name in economy:
                    index = economy.index(name)
                    seat = index + 5
                    print("======= BOARDING PASS =======")
                    print("Economy Passenger")
                    print("Seat #" + ": " + str(index + 5))
                    print("Passenger Name: " + name)
                    print("=============================")
                else:
                    print("No passenger with name " + name + " was found")
main()
