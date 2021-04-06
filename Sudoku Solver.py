import numpy as np

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


print(np.matrix(board))

def possible(row, column, number):
    global board

    #is the number appearing in the given row?
    for i in range(0,9):
        if board[row][i] == number:
            return False

    ##is the number appearing in the given column?
    for i in range(0,9):
        if board[i][column] == number:
            return False

    #is the number appearing in the given square?
    x0 = (column // 3)*3
    yo = (row // 3)*3

    for i in range(0,3):
        for j in range(0,3):
            if board[yo+i][x0+j] ==  number:
                return False
    return True


def solve():
    global board
    for row in range(0,9):
        for column in range(0,9):
            if board[row][column] == 0:
                for number in range(1,10):
                    if possible(row, column,number):
                        board[row][column] = number
                        solve()
                        board[row][column] = 0
                return

    print(np.matrix(board))

    input("Enter to check if there are any more soltion possible")

print("Solved sudoku is:")
print("------------------")
solve()
