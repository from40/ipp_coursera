""""
test suite of SolitaireMancala class

"""

import poc_simpletest


def run_suite(game_class):
    """
    Some informal testing code
    """

    # create a TestSuite object
    suite = poc_simpletest.TestSuite()

    # create a game
    game = game_class()

    # add tests using suite.run_test(....) here
    # test the initial configuration of the board using the str method
    suite.run_test(str(game), str([0]), "Test #0: init")

    # check the str and get_num_seeds methods
    test_configuration = [5, 0, 2, 4, 2, 0, 0]
    game.set_board(test_configuration)
    suite.run_test(game.get_num_seeds(2), test_configuration[2],
                   "Test #1: set_board for 2nd house")
    suite.run_test(game.get_num_seeds(5), test_configuration[5],
                   "Test #1b: get_num_seeds for 5th house")

    # report number of tests and failures
    suite.report_results()
