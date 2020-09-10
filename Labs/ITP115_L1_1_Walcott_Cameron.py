# Cameron Walcott
# ITP 115, Spring 2020
# Lab 1
# cwalcott@usc.edu
# Description: This program prints a box,prints and formats a quote using a single ONE print statement, and
# asks the user day of the week, stores it in a variable, then prints out a message.
def main():
    print(" __" '\n' + "|  |" + '\n' + "|  |" '\n' + "|__|" + '\n')


    print("You don't frighten us, English pig-dogs!" + '\n' + "Go and boil your bottoms, sons of a silly person!"
          + '\n' + '\t' + '\t'+ '\t' + "-\"Monty Python and the Holy Grail\"" + '\n')


    month = input("What month are we in? ")
    day = input("What day is it? ")
    date = int(input("What day of the month is today? "))
    print("Today is" , day , month , date , "and Tomorrow will be" , month , end=" ")
    print(date + 1)

main()