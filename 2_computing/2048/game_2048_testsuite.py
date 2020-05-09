"""
Testing class for 2048 game TwentyFortyEight class
based on poc_simpletest provided by RICE university
"""

import sys
sys.path.append('2048')
import poc_simpletest


def run_test(user_class):
    """
    tests TwentyFortyEight class of 2048 game
    """
    # create a TestSuite object
    suite = poc_simpletest.Testsuite()

    # create a game
    game = user_class(4, 4)

    # add basic default output
    init_grid = [[0 for dummy_column in range(4)] for dummy_row in range(4)]
    init_grid_msg = ""
    for elem in init_grid:
        init_grid_msg += str(elem)

    # add tests using suite.run_test(....)
    suite.run_test(str(game), init_grid_msg, "Test #01: Reset().\n")
    suite.run_test(game.move(3), str([0, 1]), "Test #02: Move().\n")

    # report number of tests and failures
    suite.report_results()