# level1-utils/janvi75/functions.py

import math

# -------------------------
# Activation Functions
# -------------------------

def sigmoid(x):
    """
    Compute the sigmoid activation function.

    Args:
        x (float): Input value.

    Returns:
        float: Sigmoid of x.
    """
    return 1 / (1 + math.exp(-x))

def relu(x):
    """
    Compute the ReLU (Rectified Linear Unit) activation function.

    Args:
        x (float): Input value.

    Returns:
        float: ReLU of x.
    """
    return max(0, x)

def tanh(x):
    """
    Compute the hyperbolic tangent (tanh) activation function.

    Args:
        x (float): Input value.

    Returns:
        float: Tanh of x.
    """
    return math.tanh(x)

# -------------------------
# Vector Operations
# -------------------------

def dot_product(v1, v2):
    """
    Compute the dot product of two vectors.

    Args:
        v1 (list of float): First vector.
        v2 (list of float): Second vector.

    Returns:
        float: Dot product result.
    """
    return sum(a * b for a, b in zip(v1, v2))

def magnitude(v):
    """
    Compute the magnitude (L2 norm) of a vector.

    Args:
        v (list of float): Vector.

    Returns:
        float: Magnitude.
    """
    return math.sqrt(sum(x ** 2 for x in v))

def cosine_similarity(v1, v2):
    """
    Compute the cosine similarity between two vectors.

    Args:
        v1 (list of float): First vector.
        v2 (list of float): Second vector.

    Returns:
        float: Cosine similarity score.
    """
    mag1 = magnitude(v1)
    mag2 = magnitude(v2)
    if mag1 == 0 or mag2 == 0:
        return 0
    return dot_product(v1, v2) / (mag1 * mag2)

# -------------------------
# Normalization Functions
# -------------------------

def l1_normalization(v):
    """
    Apply L1 normalization to a vector.

    Args:
        v (list of float): Input vector.

    Returns:
        list of float: L1-normalized vector.
    """
    norm = sum(abs(x) for x in v)
    return [x / norm if norm != 0 else 0 for x in v]

def l2_normalization(v):
    """
    Apply L2 normalization to a vector.

    Args:
        v (list of float): Input vector.

    Returns:
        list of float: L2-normalized vector.
    """
    norm = math.sqrt(sum(x ** 2 for x in v))
    return [x / norm if norm != 0 else 0 for x in v]

def min_max_normalization(v):
    """
    Apply Min-Max normalization to a vector.

    Args:
        v (list of float): Input vector.

    Returns:
        list of float: Min-Max normalized vector.
    """
    min_v = min(v)
    max_v = max(v)
    if max_v == min_v:
        return [0 for _ in v]
    return [(x - min_v) / (max_v - min_v) for x in v]

# -------------------------
# Simple Heuristic (Tic Tac Toe)
# -------------------------

def check_win(board, player):
    """
    Check if a player has won the game.

    Args:
        board (list of str): Flat list representing the board.
        player (str): 'X' or 'O'.

    Returns:
        bool: True if player has won, else False.
    """
    win_states = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    return any(all(board[i] == player for i in state) for state in win_states)

def get_available_moves(board):
    """
    Get a list of available moves on the board.

    Args:
        board (list of str): Game board.

    Returns:
        list of int: List of indices where a move can be made.
    """
    return [i for i, cell in enumerate(board) if cell == " "]

def greedy_move(board, player):
    """
    Make a greedy move: win if possible, block if opponent is winning.

    Args:
        board (list of str): Game board.
        player (str): Current player ('X' or 'O').

    Returns:
        int: Index of the move to make.
    """
    opponent = "O" if player == "X" else "X"
    for move in get_available_moves(board):
        board_copy = board[:]
        board_copy[move] = player
        if check_win(board_copy, player):
            return move
    for move in get_available_moves(board):
        board_copy = board[:]
        board_copy[move] = opponent
        if check_win(board_copy, opponent):
            return move
    return get_available_moves(board)[0] if get_available_moves(board) else -1
