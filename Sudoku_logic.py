#1. Function to read the board
#2. Check that every moves falls into the rules of Sudoku
#3. Make it such that the num is placed by the system
#4.

sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]
def print_sudoku(board):
    for row in board:
        print(" ".join(map(str,row)))

def follow_rules(num, board, row, col):
    #check row & col for dups
    for i in range(len(board)) :
        if board[row][i] == num or board[i][col] == num:
            return False
    #check box for 1-9
    start_row = row//3
    start_col = col//3
    box = []
    for i in range(3):
        for j in range(3):
            box.append(board[start_row * 3 + i][start_col * 3 + j])

    if num in box:
        return False

    return board

def valid_num(board):

    find_empty = empty_slot(board)
    if not find_empty:
        return True
    else:
        row, col = find_empty

    for num in range(1,10):
        if follow_rules(num, board, row, col):
            board[row][col] = num
            if valid_num(board):
                return True

            board[row][col] = 0

    return False

def empty_slot(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i,j
                break
    return None


print("Puzzle: \n")
print_sudoku(sudoku_board)
print("\n")

if valid_num(sudoku_board):
    print(f"Completed board: \n")
    print_sudoku(sudoku_board)
else:
    print("No solution found")
