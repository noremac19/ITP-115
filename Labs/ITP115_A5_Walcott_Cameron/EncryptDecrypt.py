# Cameron Walcott , cwalcott@usc.edu
# ITP 115, Spring 2020
# Assignment 5
# Description:
# Program encrypts a secret message by shifting the letters of the alphabet and decrypts the message as well.

def main():
    message = input("Enter a message: ")
    shift = int(input("Enter a number to shift by (0-25): "))

    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    bet = []
    indicies = []

    for num in range(len(alpha)):
        index = num + shift
        if index >= len(alpha):
            index = index - 26
        bet.append(alpha[index])

    bet.append(" ")
    alpha.append(" ")

    encrypt = ""
    decrypt = ""

    for letter in message:
        for num in range(len(alpha)):
            if letter == alpha[num]:
                indicies.append(alpha.index(letter))
        if letter == "":
            indicies.append(bet.index(letter))

    print("Encrypting message....")
    for letter in range(len(indicies)):
        encrypt = encrypt + bet[indicies[letter]]
    print(" Encrypted message: " + encrypt)

    print("Decrypting message....")
    for letter in range(len(indicies)):
        decrypt = decrypt + alpha[indicies[letter]]
    print(" Decrypted message: " + decrypt)
    print("Original message: " + message)
main()
