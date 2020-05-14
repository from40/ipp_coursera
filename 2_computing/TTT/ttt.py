"""
Monte Carlo Tic-Tac-Toe Player
Submitted version: http://www.codeskulptor.org/#user47_PdIVJXWuMRY39lf.py
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided


NTRIALS = 15  # Number of trials to run
SCORE_CURRENT = 1.0  # Score for squares played by the current player
SCORE_OTHER = 1.0  # Score for squares played by the other player


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
            # print "\nTrial result:\n", str(board)
            break
        current_player = provided.switch_player(current_player)


def mc_update_scores(scores, board, player):
    """
    Updated scores based on each NTRIAL results
    """
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
                    scores[raw][col] = scores[raw][col] + multi_current * SCORE_CURRENT
                else:
                    scores[raw][col] = scores[raw][col] + multi_other * SCORE_OTHER
    # print "Updated scores\n", scores, "\n\n"


def get_best_move(board, scores):
    """
    Randomly choose from best possible moves one
    and return its coordinates on the board
    """
    board_empty_squares = board.get_empty_squares()

    best_score = float("-inf")
    for square in board_empty_squares:
        if scores[square[0]][square[1]] >= best_score:
            best_score = scores[square[0]][square[1]]

    best_moves = []
    for square in board_empty_squares:
        if scores[square[0]][square[1]] == best_score:
            best_moves.append(square)
    # print "Best moves", best_moves, "\n\n"
    return random.choice(best_moves)


def mc_move(board, player, trials):
    """
    Initiate next player move
    """
    dim = board.get_dim()
    scores = [[0 for dummy_col in range(dim)] for dummy_row in range(dim)]
    # print "Start series of trials for next move choice.\n", board
    for dummy_trial in range(trials):
        shadow_board = board.clone()
        shadow_player = int(player)
        mc_trial(shadow_board, shadow_player)
        mc_update_scores(scores, shadow_board, shadow_player)
    return get_best_move(board, scores)


# create_board(3)
# Test game with the console or the GUI.  Uncomment whichever
# you prefer.  Both should be commented out when you submit
# for testing to save time.
provided.play_game(mc_move, NTRIALS, False)
