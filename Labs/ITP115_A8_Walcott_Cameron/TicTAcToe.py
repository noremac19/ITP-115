# Name, USC email
# ITP 115, Spring 2020
# Assignment 8
# Description:
# Tic Tac Toe Game using fucntions, importing functions from other programs, conditional statements, and while loops.

import TicTacToeHelper


def isValidMove(boardList,spot):
    if "x" in boardList[spot] or "o" in boardList[spot]:
        return False
    else:
        return True

def updateBoard(boardList, spot, playerLetter):
    boardList[spot] = playerLetter

def playGame():
    board = ["0 ", "1 ", "2 ", "3 ", "4 ", "5 ", "6 ", "7 ", "8 "]
    TicTacToeHelper.printUglyBoard(board)
    moves = 0
    while TicTacToeHelper.checkForWinner(board,moves) == "n":
        if moves % 2 == 0:
            letter = "x"
            turn = int(input("Player x, pick a spot: "))
            if isValidMove(board,turn) == True:
                updateBoard(board,turn,letter)
                TicTacToeHelper.printUglyBoard(board)
            else:
                print("Invalid move, please try again.")
                while isValidMove(board,turn) == False:
                    turn = int(input("Player x, pick a spot: "))
                    if isValidMove(board, turn) == True:
                        updateBoard(board, turn, letter)
                        TicTacToeHelper.printUglyBoard(board)
                    else:
                        print("Invalid move, please try again.")
        else:
            letter = "o"
            turn = int(input("Player o, pick a spot: "))
            if isValidMove(board, turn) == True:
                updateBoard(board, turn, letter)
                TicTacToeHelper.printUglyBoard(board)
            else:
                print("Invalid move, please try again.")
                while isValidMove(board, turn) == False:
                    turn = int(input("Player o, pick a spot: "))
                    if isValidMove(board, turn) == True:
                        updateBoard(board, turn, letter)
                        TicTacToeHelper.printUglyBoard(board)
                    else:
                        print("Invalid move, please try again.")
        moves += 1
    if TicTacToeHelper.checkForWinner(board,moves) == "x":
        print("Game Over!")
        print("Player x is the winner!")
    elif TicTacToeHelper.checkForWinner(board,moves) == "o":
        print("Game Over!")
        print("Player o is the winner!")
    elif TicTacToeHelper.checkForWinner(board,moves) == "s":
        print("Game Over!")
        print("Stalemate reached!")

def main():
    playGame()
    keep = True
    while keep:
        play = input("Would you like to play another round? (y/n): ")
        if play.lower() == "y":
            keep = True
            playGame()
        elif play.lower() == "n":
            keep = False
            print("Goodbye!")
        else:
            keep = True
            playGame()

main()