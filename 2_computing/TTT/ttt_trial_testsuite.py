"""
Testing function mc_trial for Tic-Tac-Toe game
mc_trial(board, player): This function
1. takes a current board and the next player to move.
2. The function should play a game starting with the given player
by making random moves, alternating between players.
3. The function should return when the game is over.
4. The modified board will contain the state of the game,
so the function does not return anything.
In other words, the function should modify the board input.
"""

import sys
sys.path.append('TTT')
import poc_simpletest


def run_test(mc_trial):
    """
    tests function mc_trial for Tic-Tac-Toe game
    """
    # create a TestSuite object
    suite = poc_simpletest.Testsuite()

    # add tests using suite.run_test(....)
    suite.run_test(mc_trial(board, PLAYERO, 1), str(board), "Test #01: Reset().\n")

    # report number of tests and failures
    suite.report_results()
