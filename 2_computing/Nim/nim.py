"""
A simple Monte Carlo solver for Nim
http://en.wikipedia.org/wiki/Nim#The_21_game
"""

import random
import codeskulptor
codeskulptor.set_timeout(20)

MAX_REMOVE = 3
TRIALS = 10000


def evaluate_position(num_items):
    """
    Using Monte Carlo simulation to compute a good move
    for a given number of items in the heap
    """
    best_move = 0
    best_ratio = 0.0
    for initial_move in range(1, MAX_REMOVE + 1):
        comp_wins = 0
        for game in range(TRIALS):
            still_items = num_items - initial_move
            while True:
                if still_items <=0:
                    comp_wins += 1
                    break
                player_move = random.randrange(1, MAX_REMOVE + 1)
                still_items -= player_move
                if still_items <= 0:
                    break
                comp_move = random.randrange(1, MAX_REMOVE + 1)
                still_items -= comp_move
                if still_items <= 0:
                    comp_wins += 1
                    break
        current_ratio = float(comp_wins) / float(TRIALS)
        if current_ratio > best_ratio:
            best_ratio = current_ratio
            best_move = initial_move
        # print("For initial move", initial_move, "ratio of comp wins equal", current_ratio)
        # print("Best move is", best_move)
    return best_move


def play_game(start_items):
    """
    Play game of Nim against Monte Carlo bot
    """
    current_items = start_items
    print("Starting game with value", current_items)
    while True:
        comp_move = evaluate_position(current_items)
        current_items -= comp_move
        print("Computer choose", comp_move, ", current value is", current_items)
        if current_items <= 0:
            print("Computer wins")
            break
        player_move = int(input("Enter your current move"))
        current_items -= player_move
        print("Player choose", player_move, ", current value is", current_items)
        if current_items <= 0:
            print("Player wins")
            break


play_game(10)