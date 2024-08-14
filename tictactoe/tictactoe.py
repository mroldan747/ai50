"""
Tic Tac Toe Player
"""
import copy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    turn = X
    count_x = 0
    count_o = 0
    for line in board:
        for space in line:
            if space == X:
                count_x += 1
            elif space == O:
                count_o += 1

    if count_x > count_o:
        turn = O

    return turn


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for i, line in enumerate(board):
        for j, space in enumerate(line):
            if space == EMPTY:
                possible_actions.add((i, j))

    return possible_actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    result_board = copy.deepcopy(board)
    if result_board[action[0]][action[1]] != EMPTY:
        raise Exception
    turn = player(result_board)
    result_board[action[0]][action[1]] = turn
    return result_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    a= 0
    for i in range(3):
        if i == 0:
            if board[i][i] == board[i+1][i+1] == board[-1][-1]:
                return board[i][i]
            if board[i][-1] == board[i+1][i+1] == board[-1][i]:
                return board[i][-1]
        if board[i][0] == board[i][1] == board[i][2]:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i]:
            return board[0][i]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True

    for i, line in enumerate(board):
        for j, space in enumerate(line):
            if space == EMPTY:
                return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winner_player = winner(board)
    if winner_player == X:
        return 1
    if winner_player == O:
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    optimal_action = None
    turn = player(board)
    if turn == X:
        v = float('-inf')
        for action in actions(board):
            value = min_value(result(board, action))
            if value > v:
                optimal_action = action
                v = value

    if turn == O:
        v = float('inf')
        for action in actions(board):
            value = max_value(result(board, action))
            if value < v:
                optimal_action = action
                v = value

    return optimal_action


def max_value(board):
    if terminal(board):
        return utility(board)

    v = float('-inf')
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v


def min_value(board):
    if terminal(board):
        return utility(board)

    v = float('inf')
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v