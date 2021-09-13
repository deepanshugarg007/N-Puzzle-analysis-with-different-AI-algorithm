# Importing Python Libraries
import time
import random
import math

# Global Variable Define to Acknowledge a Case is passed or Failed
FAILED = False


# Heuristic cost - Manhattan_distance
def get_manhattan_distance(board):
    distance = 0
    width = math.sqrt(len(board))
    for i in range(len(board)):
        # Value in the Board at index i
        value = board[i]
        # Current position in X and Y Axis
        current_pos_x = i / width
        current_pos_y = i % width
        # Expected position in X and Y Axis
        expected_pos_x = value / width
        expected_pos_y = value % width
        distance += abs(current_pos_x - expected_pos_x) + abs(current_pos_y - expected_pos_y)
    return distance


def first_choice_hill_climbing_util(board):
    n = len(board)-1
    width = int(math.sqrt(len(board)))
    down_feasible = int(n-width+1)

    for i in range(len(board)):
        if board[i] == 0:
            break
    distance = get_manhattan_distance(board)
    max_round = 50
    count = 0
    while True:
        count += 1
        if count >= max_round:
            global FAILED
            FAILED = True
            return board
        direction = random.randint(0, 4)

        # Directions: Up->0, Down->1, Left->2, Right->3

        if direction == 0:
            if i >= width:
                upBoard = list(board)
                # Swap the Piece
                upBoard[i] = board[i-width]
                upBoard[i-width] = 0
                # If Heuristic cost  is reducing then return the board
                if get_manhattan_distance(upBoard) < distance:
                    return upBoard
        elif direction == 1:
            if i < down_feasible:
                downBoard = list(board)
                # Swap the Piece
                downBoard[i] = board[i+width]
                downBoard[i+width] = 0
                # If Heuristic cost  is reducing then return the board
                if get_manhattan_distance(downBoard) < distance:
                    return downBoard
        elif direction == 2:
            if i % width != 0:
                leftBoard = list(board)
                # Swap the Piece
                leftBoard[i] = board[i-1]
                leftBoard[i-1] = 0
                # If Heuristic cost  is reducing then return the board
                if get_manhattan_distance(leftBoard) < distance:
                    return leftBoard
        else:    
            if (i+1) % width != 0:
                rightBoard = list(board)
                # Swap the Piece
                rightBoard[i] = board[i+1]
                rightBoard[i+1] = 0
                # If Heuristic cost  is reducing then return the board
                if get_manhattan_distance(rightBoard) < distance:
                    return rightBoard
        
    return board


def first_choice_hill_climbing(board):
    max_round_permitted = 250
    count = 0
    while True:
        cost = get_manhattan_distance(board)
        if cost == 0:
            return board
        board = first_choice_hill_climbing_util(board)
        count += 1
        if count >= max_round_permitted:
            global FAILED
            FAILED = True
            return board


def main():
    title = "../Reports Generated/NPuzzle_FirstChoiceHillClimbing_Results"
    start_time_solving = time.time()
    test_case_passed = 0
    total_case = 0
    summary =''
    result = title + " result:\n\n"
    with open("../testCases.txt", "r") as ins:
        for line in ins:
            print("Test Case: ", total_case)
            global FAILED
            FAILED = False
            total_case += 1
            board = []
            for col in line.split():
                board.append(int(col))
            n_puzzle = len(board)
            board = first_choice_hill_climbing(board)
            if FAILED:
                result += "Failed!"
                print("Failed!")
            else:
                test_case_passed += 1
                print("Successful!")
                for col in range(len(board)):
                    result += str(board[col]) + " "
            result += "\n"
    
    end_time_solving = time.time()
    print('╔════════════════════════════════════════════════════════╗')
    print('║ Summary of First Choice Algorithm :'+str(n_puzzle-1)+"-Puzzle Analysis ║")
    print('╚════════════════════════════════════════════════════════╝')
    summary += "Total Time for Search: " + str(end_time_solving - start_time_solving) + '\n'
    summary += "Total Case Tested: " + str(total_case) + "\nSuccess case number: " + str(test_case_passed) + \
              "\nFailed case number: " + str(total_case-test_case_passed) + '\n'
    summary += "Success Percentage: " + str((test_case_passed / float(total_case)*100)) + '% \n'
    print(summary)
    
    f = open(title + '.txt', 'w')
    f.write(result)
    f.close()


if __name__ == '__main__':
    main()
