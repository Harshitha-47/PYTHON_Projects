# Sudoku Solver using Backtracking Algorithm
# This program solves a 9x9 Sudoku puzzle automatically.
# Empty cells are represented using 0.
# The solver fills the grid while ensuring that each row,
# column, and 3x3 subgrid follows Sudoku rules.
GRID_SIZE = 9
# Print Sudoku Board in Professional Format
def print_board(board):

    print("\n========== SUDOKU BOARD ==========\n")

    for i in range(GRID_SIZE):

        if i % 3 == 0 and i != 0:
            print("-" * 21)

        for j in range(GRID_SIZE):

            if j % 3 == 0 and j != 0:
                print("|", end=" ")

            print(board[i][j], end=" ")

        print()

    print("\n==================================")


# Find empty cell
def find_empty(board):

    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):

            if board[row][col] == 0:
                return row, col

    return None


# Check if number placement is valid
def is_valid(board, num, position):

    row, col = position

    # Check row
    for i in range(GRID_SIZE):
        if board[row][i] == num and col != i:
            return False

    # Check column
    for i in range(GRID_SIZE):
        if board[i][col] == num and row != i:
            return False

    # Check 3x3 box
    box_x = col // 3
    box_y = row // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):

            if board[i][j] == num and (i, j) != position:
                return False

    return True
# Backtracking Sudoku Solver
def solve_sudoku(board):

    empty = find_empty(board)

    if not empty:
        return True

    row, col = empty

    for num in range(1, 10):

        if is_valid(board, num, (row, col)):

            board[row][col] = num

            if solve_sudoku(board):
                return True

            board[row][col] = 0

    return False
# Sample Sudoku Puzzle
board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]
# Program Execution
print("\n========= ORIGINAL SUDOKU =========")
print_board(board)

if solve_sudoku(board):

    print("\n========= SOLVED SUDOKU =========")
    print_board(board)

else:
    print("No solution exists.")
