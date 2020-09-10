# Cameron Walcott
# ITP 115, Spring 2020
# Assignment 6
# Description:
# Describe what this program does.


def main():
    reservations = ["", "", "", "", "", "", "", "", "", ""]
    TOTAL_SEATS = 10  # the plane’s TOTAL capacity which doesn’t change
    numFilledSeats = 0
    decision = 0

    while decision != -1:
        print("1: Assign Seat" + '\n' + "2: Print Seat Map" + '\n' + "3: Print Boarding Pass" + '\n' + "-1: Quit")
        decision = int(input())
        if decision == 1:
            if numFilledSeats == 10:
                print("Next flight leaves in 3 hours.")
            else:
                reservations[numFilledSeats] = input("Please enter your first name: ")
                numFilledSeats += 1
        if decision == 2:
            print("***************************************")
            for num in range(TOTAL_SEATS):
                if reservations[num] == "":
                    print("Seat #" + str(num+1) + ":" + '\t' + "Empty")
                else:
                    print("Seat #" + str(num+1) + ":" + '\t' + reservations[num])
            print("***************************************")
        if decision == 3:
            which = int(input("Type 1 to get Boarding Pass by seat number" + '\n' + "Type 2 to get Boarding Pass by name"))
            if which == 1:
                seat = int(input("Please enter your seat number: "))
                print("======= BOARDING PASS =======")
                print("Seat #: " + str(seat))
                print("Passenger Name: " + reservations[seat-1])
                print("=============================")
            else:
                name = input("Please enter your first name: ")
                if name in reservations:
                    index = reservations.index(name)
                    seat = index + 1
                    print("======= BOARDING PASS =======")
                    print("Seat #" + ":" + str(index+1))
                    print("Passenger Name: " + name)
                    print("=============================")
main()

# for the advanced part find a random index from 5-10 to place in economy and random choice from 1-4 for