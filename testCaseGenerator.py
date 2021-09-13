# Importing Python Libraries
import random
import math
import sys
import time


def shuffling_util(board, n):
    width = int(math.sqrt(n+1))
    down_feasible = int(n-width+1)

    for i in range(n+1):
        if board[i] == 0:
            break
    while True:
        randCase = random.randint(0,4)
        if randCase == 0:
            if i >= width:
                upBoard = list(board)
                # Swap the Piece
                upBoard[i] = board[i-width]
                upBoard[i-width] = 0
                return upBoard
        elif randCase == 1:
            if i < down_feasible:
                downBoard = list(board)
                # Swap the Piece
                downBoard[i] = board[i+width]
                downBoard[i+width] = 0
                return downBoard
        elif randCase == 2:
            if i % width != 0:
                leftBoard = list(board)
                # Swap the Piece
                leftBoard[i] = board[i-1]
                leftBoard[i-1] = 0
                return leftBoard
        else:    
            if (i+1) % width != 0:
                rightBoard = list(board)
                # Swap the Piece
                rightBoard[i] = board[i+1]
                rightBoard[i+1] = 0
                return rightBoard
        
    return board


def shuffling(board, n, shuffleCount):
    count = 0
    while True:
        if (count >= shuffleCount):
            return board
        board = shuffling_util(board, n)
        count += 1


def validate(n):
    root = math.sqrt(n+1)
    if (root - math.floor(root)) == 0:
        print(n, "-Puzzle is a Valid Puzzle Problem")
    else:
        print("Oops! Not a Valid N-Puzzle. Please Try Again")
        time.sleep(2)
        sys.exit()


if __name__ == '__main__':
    print('  _   _            _____                        _       ')
    print(' | \ | |          |  __ \                      | |      ')
    print(' |  \| |  ______  | |__) |  _   _   ____  ____ | | ___  ')
    print(' | . ` | |______| |  ___/  | | | | |_  / |_  / | |/ _ \ ')
    print(' | |\  |          | |      | |_| |  / /   / /  | |  __/ ')
    print(' |_| \_|          |_|       \__,_| /___| /___| |_|\___| ')

    print('╔══════════════════════════════════════════════════════╗')
    print('║ Creating Environment, Please wait for a minute...    ║')
    print('║ Solving N-Puzzle with Following Algorithm:           ║')
    print('║                                                      ║')
    print('║ 1. Simple Hill Climbing                              ║')
    print('║ 2. Random Restart Hill Climbing                      ║')
    print('║ 3. Simulated Annealing                               ║')
    print('║                                                      ║')
    print('║ DO NOT Close this window.                            ║')
    print('║ This Will Generate the Test Cases for N-Puzzle       ║')
    print('╚══════════════════════════════════════════════════════╝')
    print('╔══════════════════════════════════════════════════════╗')
    print('║ Choose the Value of N: For Generating Test Cases     ║')
    print('║    | WIDTH  | N  |                                   ║')
    print('║    ---------------                                   ║')
    print('║       3x3   | 8                                      ║')
    print('║       4x4   | 15                                     ║')
    print('║       5x5   | 24                                     ║')
    print('║       6x6   | 35                                     ║')
    print('║       7x7   | 48                                     ║')
    print('║       8x8   | 63                                     ║')
    print('║       9x9   | 80                                     ║')
    print('║      10x10  | 99                                     ║')
    print('║      11x11  | 120                                    ║')
    print('║      12x12  | 143                                    ║')
    print('║      13x13  | 168                                    ║')
    print('║      14x14  | 195                                    ║')
    print('║      15x15  | 224                                    ║')
    print('║       .....So On                                     ║')
    print('╚══════════════════════════════════════════════════════╝')

    n = int(input("Enter your value of N: "))
    # n=24
    testCaseCount = int(input("Enter No. Of Test Cases: "))
    # testCaseCount =25

    shuffleCount = int(input("Enter Shuffle Count: "))
    # shuffleCount=100

    # Validate N: if wrong n then print wrong input and exit
    validate(n)

    file = open("testCases.txt", "w")
    result = ""
    while testCaseCount > 0:
        testCaseCount = testCaseCount - 1
        board = []

        # Initialize Board with Default Board Settings
        for j in range(n + 1):
            board.append(j)

        # Prepare Test Case
        board = shuffling(board, n, shuffleCount)
        for i in range(n):
            result += str(board[i]) + ' '
        result += str(board[i+1]) + '\n'

    print(result)
    file.write(result)
    file.close()
