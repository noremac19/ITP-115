# Cameron Walcott, cwalcott@usc.edu
# ITP 115, Spring 2020
# Lab 2
# Description:
# Describe what this program does such as:
# This program takes in variable values and strings and uses conditional
# statements to build and output a coffee order.

import random

size = input("What size coffee do you want (S, M, L)? ")
question = input("Would you like your drink to be a random temperature (y/n)? ")
if question == "y" or question == "Y":
    num = random.randrange(120) + 32
    if num >= 90:
        temp = "hot"
    else:
        temp = "iced"
else:
    if int(input("What temperature would you like (in degrees)? ")) >= 90:
        temp = "hot"
    else: temp = "iced"

type = input("What type of beans / blend would you like? ")
ans = input("Would you like room for cream (y/n)? ")

if size == "S" or size == "s":
    size = "small"
elif size == "M" or size == "m":
    size = "medium"
else: size = "large"


if ans == "y":
    ans = "with cream"
else: ans = "without cream"

print("You ordered a" , size , temp , type , "coffee" , ans)


