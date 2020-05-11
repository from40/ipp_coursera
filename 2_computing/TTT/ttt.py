"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
# do not change their names.
NTRIALS = 1  # Number of trials to run
SCORE_CURRENT = 1.0  # Score for squares played by the current player
SCORE_OTHER = 1.0  # Score for squares played by the other player


def create_board(dim):
    board = provided.TTTBoard(dim)
    scores = [[0 for col in range(dim)] for row in range(dim)]
    first_player = provided.PLAYERX
    mc_trial(board, first_player)
    mc_update_scores(scores, board, first_player)
    get_best_move(board, scores)


def mc_trial(board, player):
    """
    Plays give board, starting with given player
    by making random moves within empty squares
    alternating between players after each move
    """
    current_player = player
    while board.get_empty_squares():
        square = random.choice(board.get_empty_squares())
        board.move(square[0], square[1], current_player)
        if board.check_win() is not None:
            print(str(board))
            break
        current_player = provided.switch_player(current_player)


def mc_update_scores(scores, board, player):
    winner = board.check_win()
    if winner == provided.DRAW:
        multi_current = 0
        multi_other = 0
    elif winner == player:
        multi_current = 1
        multi_other = -1
    else:
        multi_current = -1
        multi_other = 1
    dim = board.get_dim()
    for raw in range(dim):
        for col in range(dim):
            if board.square(raw, col) == provided.EMPTY:
                pass
            else:
                if board.square(raw, col) == player:
                    scores[raw][col] = multi_current * SCORE_CURRENT
                else:
                    scores[raw][col] = multi_other * SCORE_OTHER
    print(scores)


def get_best_move(board, scores):
    board_empty_squares = board.get_empty_squares()

    best_score = float("-inf")
    for square in board_empty_squares:
        if scores[square[0]][square[1]] >= best_score:
            best_score = scores[square[0]][square[1]]

    best_moves = []
    for square in board_empty_squares:
        if scores[square[0]][square[1]] == best_score:
            best_moves.append(square)
    return random.choice(best_moves)


def mc_move(board, player, trials):
    dim = board.get_dim()
    scores = [[0 for col in range(dim)] for row in range(dim)]
    for trial in range(trials):
        shadow_board = board
        shadow_player = player
        mc_trial(shadow_board, shadow_player)
        mc_update_scores(scores, shadow_board, shadow_player)
    return get_best_move(board, scores)


create_board(3)


# Test game with the console or the GUI.  Uncomment whichever
# you prefer.  Both should be commented out when you submit
# for testing to save time.
#provided.play_game(mc_move, NTRIALS, False)
