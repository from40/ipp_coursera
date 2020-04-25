# Rock-paper-scissors-lizard-Spock template

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

import random
db_choice = ["rock", "paper", "scissors", "lizard", "Spock"]


def name_to_number(name):
    for i in range(len(db_choice)):
        if db_choice[i] == name:
            return i
    else:
        print("name_to_number: no player choice found in database")


def number_to_name(number):
    for i in range(len(db_choice)):
        if i == number:
            return db_choice[i]


def rpsls():
    print("\nWhat\'s your choice for next round?\n\
    >>> 0 - rock\n    >>> 1 - Spock\n    >>> 2 - paper\n\
    >>> 3 - lizard\n    >>> 4 - scissors\n")
    player_number = int(input("What's your choice? "))

    random.seed()
    comp_number = random.randrange(0, 5)
    comp_choice = number_to_name(comp_number)
    print("Comp choose " + comp_choice + "!")

    player_vs_comp = (player_number - comp_number) % 5
    if player_vs_comp <= 2:
        print("Hey, man! You just have won!")
    elif player_vs_comp == 0:
        print("None-to-none!")
    elif player_vs_comp >= 3:
        print("Sorry, man... You lose!")
    else:
        print("rpsls: difference between numbers is not valid")

rpsls()
