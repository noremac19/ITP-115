# Cameron Walcott , cwalcott@usc.edu
# ITP 115, Spring 2020
# Assignment 7
# Description:
# Rock paper scissors game using functions.

import random

def displayMenu():
    print("Welcome! Let's play rock, paper, scissors." + '\n' + "The rules of the game are:")
    print("Rock smashes scissors" + '\n' + "Scissors cut paper" + '\n' + "Paper covers rock")
    print("If both the choices are the same, it's a tie")

def getComputerChoice():
    return random.randrange(3)

def getPlayerChoice():
    user = int(input("Please choose (0) for rock, (1) for paper or (2) for scissors"))
    return user

def playRound(computerChoice,playerChoice):
    if computerChoice == playerChoice:
        return 0
    elif computerChoice == 0 and playerChoice == 1:
        return 1
    elif computerChoice == 0 and playerChoice == 2:
        return -1
    elif computerChoice == 1 and playerChoice == 0:
        return -1
    elif computerChoice == 1 and playerChoice == 2:
        return 1
    elif computerChoice == 2 and playerChoice == 0:
        return 1
    elif computerChoice == 2 and playerChoice == 1:
        return -1

def continueGame():
    game = input("Would you like to continue? (Y/N): ")
    if game.upper() == "Y":
        return True
    else:
        return False

def main():
    condition = True
    displayMenu()
    ties = 0
    player = 0
    computer = 0
    while condition:
        computerChoice = getComputerChoice()
        playerChoice = getPlayerChoice()
        if playRound(computerChoice, playerChoice) == 0:
            if computerChoice == 0 and playerChoice == 0:
                print("You chose Rock")
                print("Computer chose Rock")
                print("It's a tie.")
            elif computerChoice == 1 and playerChoice == 1:
                print("You chose Paper")
                print("Computer chose Paper")
                print("It's a tie.")
            elif computerChoice == 2 and playerChoice == 2:
                print("You chose Scissors")
                print("Computer chose Scissors")
                print("It's a tie")
            ties += 1
        if playRound(computerChoice, playerChoice) == 1:
            if computerChoice == 0 and playerChoice == 1:
                print("You chose Paper")
                print("Computer chose Rock")
                print("Paper covers rock. You win!")
            elif computerChoice == 1 and playerChoice == 2:
                print("You chose Scissors")
                print("Computer chose Paper")
                print("Scissors cut paper. You win!")
            elif computerChoice == 2 and playerChoice == 0:
                print("You chose Rock")
                print("Computer chose Scissors")
                print("Rock smashes scissors. You win!")
            player += 1
        if playRound(computerChoice, playerChoice) == -1:
            if computerChoice == 0 and playerChoice == 2:
                print("You chose Scissors")
                print("Computer chose Rock")
                print("Rock smashes scissors. Computer wins!")
            elif computerChoice == 1 and playerChoice == 0:
                print("You chose Rock")
                print("Computer chose Paper")
                print("Paper covers rock. Computer wins!")
                return -1
            elif computerChoice == 2 and playerChoice == 1:
                print("You chose Paper")
                print("Computer chose Scissors")
                print("Scissors cut paper. Computer wins!")
                return -1
            computer += 1
        condition = continueGame()
    print("You won" + str(player) + "game(s).")
    print("The computer won" + str(computer) + "game(s).")
    print("You tied with the computer" + str(ties) + "time(s).")


main()
