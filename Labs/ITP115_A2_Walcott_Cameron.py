# Cameron Walcott, cwalcott@usc.edu
# ITP 115, Spring 2020
# Assignment 2
# Description:
# This program creates a harry potter vending machine.
# It determines change and gives a discount.



butterbeer = 380
quill = 945
dailyprophet = 720
spells = 4000
wand = 3456
wizard = 123456
hat = 1234
dragon = 4528
print("Please select an item from the vending machine: ")
print("     a) Butterbeer: 380 knuts")
print("     b) Quill: 945 knuts")
print("     c) The Daily Prophet: 720 knuts")
print("     d) Book of Spells: 4000 knuts")
print("     e) Magic Wand: 3456 knuts")
print("     f) Wizard: 123456 knuts")
print("     g) Sorcerers Hat: 1234 knuts")
print("     h) Mini Dragon: 4528 knuts")
choice = input()
cash = int(input("How many galleons do you have?: "))
discount = input("Would you like to share your post on Instagram for a 5 knut discount (y/n)?: ")
if discount == "y" or discount == "Y":
    butterbeer -= 5
    quill -= 5
    dailyprophet -= 5
    spells -= 5
elif discount == "n" or discount == "N":
    butterbeer = butterbeer
    quill = quill
    dailyprophet = dailyprophet
    spells = spells
else:
    print("You have entered an invalid option. No coupon will be used.")

cash = cash * 493

if choice == "a" or choice == "A":
    price = cash - butterbeer
    galleons = price // 493
    sickles = (price % 493) // 29
    knuts = (price % 493) % 29
    choice = "Butterbeer"
    if discount == "y" or discount == "Y":
        print("You bought a", choice, "for", price, "knuts (with a coupon of 5 knuts) and paid with", galleons,
              "galleon(s).")
        print("Here is your change", "(" , price, "knuts" + "):")
        print("Galleons:", galleons)
        print("Sickles:", sickles)
        print("Knuts:", knuts)
    else:
        print("You bought a", choice, "for", price, "knuts (with a coupon of 0 knuts) and paid with", galleons,
              "galleon(s).")
        print("Here is your change", "(" , price, "knuts" + "):")
        print("Galleons:", galleons)
        print("Sickles:", sickles)
        print("Knuts:", knuts)
elif choice == "b" or choice == "B":
    price = cash - quill
    galleons = price // 493
    sickles = (price % 493) // 29
    knuts = (price % 493) % 29
    choice = "Quill"
    if discount == "y" or discount == "Y":
        print("You bought a", choice, "for", price, "knuts (with a coupon of 5 knuts) and paid with", galleons,
              "galleon(s).")
        print("Here is your change", "(" , price, "knuts" + "):")
        print("Galleons:", galleons)
        print("Sickles:", sickles)
        print("Knuts:", knuts)
    else:
        print("You bought a", choice, "for", price, "knuts (with a coupon of 0 knuts) and paid with", galleons,
              "galleon(s).")
        print("Here is your change", "(" , price, "knuts" + "):")
        print("Galleons:", galleons)
        print("Sickles:", sickles)
        print("Knuts:", knuts)
elif choice == "c" or choice == "C":
    price = cash - dailyprophet
    galleons = price // 493
    sickles = (price % 493) // 29
    knuts = (price % 493) % 29
    choice = "The Daily Prophet"
    if discount == "y" or discount == "Y":
        print("You bought a", choice, "for", price, "knuts (with a coupon of 5 knuts) and paid with", galleons,
              "galleon(s).")
        print("Here is your change", "(" , price, "knuts" + "):")
        print("Galleons:", galleons)
        print("Sickles:", sickles)
        print("Knuts:", knuts)
    else:
        print("You bought a", choice, "for", price, "knuts (with a coupon of 0 knuts) and paid with", galleons,
              "galleon(s).")
        print("Here is your change", "(" , price, "knuts" + "):")
        print("Galleons:", galleons)
        print("Sickles:", sickles)
        print("Knuts:", knuts)
elif choice == "d" or choice == "D":
    price = cash - spells
    galleons = price // 493
    sickles = (price % 493) // 29
    knuts = (price % 493) % 29
    choice = "Book of Spells"
    if discount == "y" or discount == "Y":
        print("You bought a", choice, "for", price, "knuts (with a coupon of 5 knuts) and paid with", galleons,
              "galleon(s).")
        print("Here is your change", "(" , price, "knuts" + "):")
        print("Galleons:", galleons)
        print("Sickles:", sickles)
        print("Knuts:", knuts)
    else:
        print("You bought a", choice, "for", price, "knuts (with a coupon of 0 knuts) and paid with", galleons,
              "galleon(s).")
        print("Here is your change", "(" , price, "knuts" + "):")
        print("Galleons:", galleons)
        print("Sickles:", sickles)
        print("Knuts:", knuts)
elif choice == "e" or choice == "E":
    price = cash - wand
    galleons = price // 493
    sickles = (price % 493) // 29
    knuts = (price % 493) % 29
    choice = "Magic Wand"
    if discount == "y" or discount == "Y":
        print("You bought a", choice, "for", price, "knuts (with a coupon of 5 knuts) and paid with", galleons,
              "galleon(s).")
        print("Here is your change", "(" , price, "knuts" + "):")
        print("Galleons:", galleons)
        print("Sickles:", sickles)
        print("Knuts:", knuts)
    else:
        print("You bought a", choice, "for", price, "knuts (with a coupon of 0 knuts) and paid with", galleons,
              "galleon(s).")
        print("Here is your change", "(" , price, "knuts" + "):")
        print("Galleons:", galleons)
        print("Sickles:", sickles)
        print("Knuts:", knuts)
elif choice == "f" or choice == "F":
    price = cash - wizard
    galleons = price // 493
    sickles = (price % 493) // 29
    knuts = (price % 493) % 29
    choice = "Wizard"
    if discount == "y" or discount == "Y":
        print("You bought a", choice, "for", price, "knuts (with a coupon of 5 knuts) and paid with", galleons,
              "galleon(s).")
        print("Here is your change", "(" , price, "knuts" + "):")
        print("Galleons:", galleons)
        print("Sickles:", sickles)
        print("Knuts:", knuts)
    else:
        print("You bought a", choice, "for", price, "knuts (with a coupon of 0 knuts) and paid with", galleons,
              "galleon(s).")
        print("Here is your change", "(" , price, "knuts" + "):")
        print("Galleons:", galleons)
        print("Sickles:", sickles)
        print("Knuts:", knuts)
elif choice == "g" or choice == "G":
    price = cash - hat
    galleons = price // 493
    sickles = (price % 493) // 29
    knuts = (price % 493) % 29
    choice = "Sorcerers Hat"
    if discount == "y" or discount == "Y":
        print("You bought a", choice, "for", price, "knuts (with a coupon of 5 knuts) and paid with", galleons,
              "galleon(s).")
        print("Here is your change", "(" , price, "knuts" + "):")
        print("Galleons:", galleons)
        print("Sickles:", sickles)
        print("Knuts:", knuts)
    else:
        print("You bought a", choice, "for", price, "knuts (with a coupon of 0 knuts) and paid with", galleons,
              "galleon(s).")
        print("Here is your change", "(" , price, "knuts" + "):")
        print("Galleons:", galleons)
        print("Sickles:", sickles)
        print("Knuts:", knuts)
elif choice == "h" or choice == "H":
    price = cash - dragon
    galleons = price // 493
    sickles = (price % 493) // 29
    knuts = (price % 493) % 29
    choice = "Chips"
    if discount == "y" or discount == "Y":
        print("You bought a", choice, "for", price, "knuts (with a coupon of 5 knuts) and paid with", galleons,
              "galleon(s).")
        print("Here is your change", "(" , price, "knuts" + "):")
        print("Galleons:", galleons)
        print("Sickles:", sickles)
        print("Knuts:", knuts)
    else:
        print("You bought a", choice, "for", price, "knuts (with a coupon of 0 knuts) and paid with", galleons,
              "galleon(s).")
        print("Here is your change", "(" , price, "knuts" , "):")
        print("Galleons:", galleons)
        print("Sickles:", sickles)
        print("Knuts:", knuts)
else:
    print("You have entered an invalid option. You will be given a Butterbeer for 58 knuts.")
    print("You bought a" , choice , "for 380 knuts" , "and paid with" , cash // 493 , "galleon(s).")
    print("Here is your change" , "(113 knuts):")
    print("Galleons: 0")
    print("Sickles: 3")
    print("Knuts: 26")

# 0 13 25

