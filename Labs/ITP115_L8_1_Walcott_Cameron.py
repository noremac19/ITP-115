# Cameron Walcott
# ITP 115, Spring 2020
# Lab 6


def temperatureConverter(conversionType,inputTemperature):
    if conversionType == 1:
        return ((inputTemperature - 32) * 5 ) / 9
    elif conversionType == 2:
        return (inputTemperature * (9/5)) + 32
    else:
        print("Incorrect Input.")

def wantsToContinue():
    decision = input("Do you want to continue (y/n)? ")
    if decision.lower() == "y":
        return True
    elif decision.lower() == "n":
        return False

def main():
    print("Welcome to the Temperature Converter 1.0")
    run = True
    while run:
        type = int(input("Enter 1 for F->C, or 2 for C->F: "))
        temp = int(input("Enter input temperature: "))
        print("The temperature is " + str(temperatureConverter(type,temp)))
        run = wantsToContinue()

main()

# Welcome to the Temperature Converter 1.0
# Enter 1 for F->C, or 2 for C->F: 1
# Enter input temperature: 212
# The converted temperature is 100
# Do you want to continue (y/n)? y
