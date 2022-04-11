# If we were to set up a Tic-Tac-Toe game,
# we would want to know whether the board's
# current state is solved, wouldn't we? Our
# goal is to create a function that will check that for us!
# Assume that the board comes in the form of a
# 3x3 array, where the value is 0 if a spot is empty,
# 1 if it is an "X", or 2 if it is an "O", like so:


def check_vertical(arr, el):
    for item in range(3):
        if arr[0][item] == el and arr[1][item] == el and arr[2][item] == el:
            return True
    return False


def check_horizontal(arr, el):
    for item in range(3):
        if arr[item][0] == el and arr[item][1] == el and arr[item][2] == el:
            return True
    return False


def check_diagonal(arr, el):
    if arr[0][0] == el and arr[1][1] == el and arr[2][2] == el:
        return True
    if arr[0][2] == el and arr[1][1] == el and arr[2][0] == el:
        return True
    return False


def is_solved(board):
    for ple in range(1, 3):
        if check_horizontal(board, ple) or check_vertical(board, ple) or check_diagonal(board, ple):
            return ple
    if 0 in board[0] or 0 in board[1] or 0 in board[2]:
        return -1
    return 0

board = [[0, 0, 1],
         [0, 1, 2],
         [2, 1, 0]]

print(is_solved(board))