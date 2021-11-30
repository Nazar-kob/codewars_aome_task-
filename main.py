# task1, 5kyu
# If we were to set up a Tic-Tac-Toe game, we would want to
# know whether the board's current state is solved, wouldn't
# we? Our goal is to create a function that will check that for us!
# Assume that the board comes in the form of a 3x3 array, where
# the value is 0 if a spot is empty, 1 if it is an "X", or 2
# if it is an "O", like so:
# [[0, 0, 1],
#  [0, 1, 2],
#  [2, 1, 0]]
# We want our function to return:
# -1 if the board is not yet finished AND no one has won yet
# (there are empty spots),
# 1 if "X" won,
# 2 if "O" won,
# 0 if it's a cat's game (i.e. a draw).
# You may assume that the board passed in is valid in the context of a game of Tic-Tac-Toe.
def is_solved(board):
    for item, i in enumerate(board):
        if i[0] == 1 and i[1] == 1 and i[2] == 1:
            return 1
        if i[0] == 2 and i[1] == 2 and i[2] == 2:
            return 2
        if board[0][item] == 1 and board[1][item] == 1 and board[2][item] == 1:
            return 1
        if board[0][item] == 2 and board[1][item] == 2 and board[2][item] == 2:
            return 2
        if board[0][0] == 1 and board[1][1] == 1 and board[2][2] == 1:
            return 1
        if board[0][0] == 2 and board[1][1] == 2 and board[2][2] == 2:
            return 2
        if board[0][2] == 1 and board[1][1] == 1 and board[2][0] == 1:
            return 1
        if board[0][2] == 2 and board[1][1] == 2 and board[2][0] == 1:
            return 2
    for item, i in enumerate(board):
        if board[0][item] == 0 or board[1][item] == 0 or board[2][item] == 0:
            return -1
    return 0


test_1 = [[2, 1, 2],
         [1, 1, 2],
         [2, 1, 2]]
test_2 = [[1, 2, 0],
        [0, 1, 2],
        [0, 0, 1]]

print(is_solved(test_1))
print(is_solved(test_2))

