
import math
import copy

X = "X"
O = "O"
EMPTY = None

# Returns starting state of the board.


def initial_state():

    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

# Returns player who has the next turn on a board.


def player(board):
    # Count num of X's and O's on the board
    num_x = sum(row.count(X) for row in board)
    num_O = sum(row.count(O) for row in board)

    # If X has made more moves than O, its O's turn, else it's X's turn
    return O if num_x > num_O else X


# Returns set of all possible actions (i, j) available on the board.
def actions(board):

    # init possible actions availabe
    actions_available = set()

    # iterate over index "i" in range of 3
    for i in range(3):
        # iterate over index "j" in range of 3
        for j in range(3):
            # Check if cell is empty before adding possible action
            if board[i][j] == EMPTY:
                actions_available.add((i, j))

    return actions_available

# Returns the board that results from making move (i, j) on the board.


def result(board, action):
    # set i, j to an action
    i, j = action

    if not (0 <= i < 3 and 0 <= j < 3):
        raise ValueError("Invalid: Out of bounds")

    # Create a Deep copy of board
    board_deepcopy = copy.deepcopy(board)

    # Validate board
    if board_deepcopy[i][j] != EMPTY:
        raise ValueError("Invalid: Cell is already occupied")

    # Update board with player move
    board_deepcopy[i][j] = player(board)

    return board_deepcopy

# Returns the winner of the game, if there is one.


def winner(board):
    # Check for a winner in rows, columns, and diagonals for a winner
    for i in range(3):
        # Check rows
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] is not None:
            return board[i][0]

        # Check columns
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] is not None:
            return board[0][i]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][0] is not None:
        return board[0][2]

    # If there isn't a winner
    return None

# Returns True if game is over, False otherwise.


def terminal(board):
    # If winner or board is full, game is offically over
    if winner(board) is not None or all(board[i][j] is not None for i in range(3) for j in range(3)):
        return True
    return False

# Returns 1 if X has won the game, -1 if O has won, 0 otherwise.


def utility(board):
    # Get winner of the game
    player_won = winner(board)

    # Return utility based on winner
    if player_won == X:
        return 1
    elif player_won == O:
        return -1
    else:
        return 0

# Returns the optimal action for the current player on the board.


def minimax(board):
    if terminal(board):
        return None

    current_player = player(board)

    if current_player == X:
        # Maximize for X
        _, action = max_value(board)
    else:
        _, action = min_value(board)

    return action


def min_value(board):
    if terminal(board):
        return utility(board), None

    v = float('inf')
    best_action = None

    for action in actions(board):
      # checks if opponent wins in this action
        if utility(result(board, action)) == 1:
          # Blocks immediate threat
          return -1, action

        new_v, _ = max_value(result(board, action))
        if new_v < v:
            v = new_v
            best_action = action

    return v, best_action


def max_value(board):
    if terminal(board):
        return utility(board), None

    v = float('-inf')
    best_action = None

    for action in actions(board):
      # checks if AI wins in this action
        if utility(result(board, action)) == 1:
          # Winning move priority
          return 1, action

        new_v, _ = min_value(result(board, action))
        if new_v > v:
            v = new_v
            best_action = action

    return v, best_action
