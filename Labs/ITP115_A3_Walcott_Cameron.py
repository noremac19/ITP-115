# Cameron Walcott, cwalcott@usc.edu
# ITP 115, Spring 2020
# Assignment 3
# Description:
#
decision = "y"
while decision == "y":
    print("Input an integer greater than or equal to 0 (-1 to quit)")
    num = int(input())
    small = num
    large = num
    count = num
    n = 1
    while True:
        num = int(input())
        if num == -1 or num == 0:
            break
        if large <= num:
            large = num
            count = count + num
            n = n + 1
        elif small <= num:
            count = count +  num
            n = n + 1
        elif small >= num:
            small = num
            count = count + num
            n = n + 1
        elif large >= num:
            count = count + num
            n = n + 1


    print("The largest number is " , large)
    print("The smallest number is " , small)
    print("The average number is " , count/n)

    decision = input("Would you like to enter another set of numbers? (y/n): ")
    if decision == "n":
        print("Goodbye!")
        break
    else:
        continue

# outer loop: num != -1 or num != 0
# inner loop: decision == y and if not, the loop breaks