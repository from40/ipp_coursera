#!/usr/bin/env python3

"""
Student facing implement of solitaire version of Mancala - Tchoukaillon

Goal: Move as many seeds from given houses into the store

In GUI, you make ask computer AI to make move or click to attempt a legal move
"""

import random
import solitaire_mancala_testsuite_01 as testsuite


class SolitaireMancala:
    """
    Models the current configuration of a game of Solitaire Mancala
    and provide several methods for analyzing and updating the game
    """
    def __init__(self):
        """
        Initiate object of class Solitaire Mancala
        with 1 empty "store" and 6 empty "houses"
        where board[0] - is Store
        """
        self.board = [0, 0, 0, 0, 0, 0, 0]

    def __str__(self):
        return str(self.board[0]) + ", " + \
               str(self.board[1]) + ", " + \
               str(self.board[2]) + ", " + \
               str(self.board[3]) + ", " + \
               str(self.board[4]) + ", " + \
               str(self.board[5]) + ", " + \
               str(self.board[6])

    def set_board(self, configuration):
        """
        puts numbers of seeds in store/houses
        according given "configuration" parameter
        """
        for i in range(len(configuration)):
            self.board[i] = configuration[i]

    def get_num_seeds(self, house_num):
        """
        returns number of seeds in defined by parameter house
        """
        return self.board[house_num]

    def is_legal_move(self, house_num):
        if house_num == 0:
            return False
        else:
            if self.get_num_seeds(house_num) == house_num:
                return True
            else:
                return False

    def apply_move(self, house_num):
        if self.is_legal_move(house_num):
            self.board[house_num] = 0
            for i in range(house_num):
                self.board[i] = self.board[i] + 1
        else:
            print("Move is illigal!")

    def choose_move(self):
        for i in range(1, len(self.board)):
            if self.is_legal_move(i):
                return i
        return False

    def is_game_won(self):
        for i in range(1, len(self.board)):
            if self.board[i] != 0:
                return False
        return True

    def plan_moves(self):
        self.shadow_board = self.board
        self.moves_plan = []
        self.next_move = self.choose_move()
        while self.next_move:
            self.moves_plan.append(self.next_move)
            self.apply_move(self.next_move)
            self.next_move = self.choose_move()
        self.board = self.shadow_board
        return self.moves_plan


# test for SolitaireMancala class
if __name__ == '__main__':
    testsuite.run_suite(SolitaireMancala)


# Create tests to check the correctness of your code
def test_mancala():
    """
    Test code for Solitaire Mancala
    """
    # test __init__()
    my_game = SolitaireMancala()
    print("__init__. # Initialize Mancala game with empty board")
    print("Testing init - Expected: 0, 0, 0, 0, 0, 0, 0")
    print("Testing init - Computed:", my_game, "\n")

    # test set_board()
    config1 = [0, 0, 1, 1, 3, 5, 0]
    my_game.set_board(config1)
    config1_reverse = list(config1)
    config1_reverse.reverse()
    print("set_board. # Seeds stones inside houses according give config")
    print("Testing set_board - Expected:", config1_reverse)
    print("Testing set_board - Computed: [", str(my_game), "]\n", sep="")

    # test get_num_seeds()
    print("get_num_seeds. # Return number of seeds in dedicated house")
    print("Testing get_num_seeds - Expected:", config1[1])
    print("Testing get_num_seeds - Computed:", my_game.get_num_seeds(1))
    print("Testing get_num_seeds - Expected:", config1[3])
    print("Testing get_num_seeds - Computed:", my_game.get_num_seeds(3))
    print("Testing get_num_seeds - Expected:", config1[5])
    print("Testing get_num_seeds - Computed:", my_game.get_num_seeds(5))

    # is_legal_move()
    print("\nis_legal_move. Calculate if move from give house_num is legal, return True (of False)")
    print("Testing is_legal_move - move from Store - Expected: False")
    print("Testing is_legal_move - move from Store - Computed:", my_game.is_legal_move(0))
    print("Testing is_legal_move - move from 2nd house - Expected: False")
    print("Testing is_legal_move - move from 2nd house - Computed:", my_game.is_legal_move(2))
    print("Testing is_legal_move - move from 5th house - Expected:", bool(config1[5]))
    print("Testing is_legal_move - move from 5th house - Computed:", my_game.is_legal_move(5))

    # apply_move()
    print("\napply_move.Testing move from give house_num")
    print("Testing apply_move - situation after move from 1st house - Expected: [1, 1, 2, 2, 4, 0, 0]")
    my_game.apply_move(5)
    print("Testing apply_move - situation after move from 1st house - Computed: [", str(my_game), "]\n", sep="")
    print("Testing apply_move - situation after move from 3rd house - Expected: [2, 2, 3, 0, 4, 0, 0]")
    my_game.apply_move(3)
    print("Testing apply_move - situation after move from 3rd house - Computed: [", str(my_game), "]\n", sep="")

    # choose_move()
    print("\nchoose_move. Returns number of house with best move according strategy")
    config1 = [0, 0, 2, 1, 3, 5, 0]
    my_game.set_board(config1)
    print("Testing choose_move - Expected: 2")
    print("Testing choose_move - Computed:", my_game.choose_move())
    config1 = [0, 0, 0, 0, 0, 0, 6]
    my_game.set_board(config1)
    print("Testing choose_move - Expected: 6")
    print("Testing choose_move - Computed:", my_game.choose_move())


