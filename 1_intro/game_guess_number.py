import simplegui
import random
import math

# ---------------------- Global variables default set up ---------------------- #
secret_number_range = 100
secret_number_value = None
user_attempts_value = None


# -------------------------- New game initialization -------------------------- #
def new_game():
    global secret_number_value, user_attempts_value
    secret_number_value = random.randrange(secret_number_range)
    user_attempts_value = math.ceil(math.log(secret_number_range + 1, 2))
    print("Welcome to the new game!\nGuess what number Big Brother thinks about.")
    print("Tip: it's something between zero and ", secret_number_range, ".", sep="")
    print("...and you have only", user_attempts_value, "allowed attempts left\n")

def range100():
    global secret_number_range
    secret_number_range = 100
    new_game()

def range1000():
    global secret_number_range
    secret_number_range = 1000
    new_game()


# ----------------------------- Comparing numbers ----------------------------- #
def input_guess(guess):
    def game_over():
        print("No, no... It's not", user_guess, "at all.")
        print("It was your last chance, but your failed...\
              \nSorry, Bro, but this is a new game for you\n")
        new_game()

    global user_attempts_value
    user_guess = int(player_input.get_text())

    if user_guess == secret_number_value:
        print("You guessed right!")
        print("Big Brother thought was", user_guess, "indeed. Congratulations!\n\n")
        new_game()
    elif user_guess > secret_number_value:
        user_attempts_value -= 1
        if not user_attempts_value:
            game_over()
        else:
            print("Ugh! You missed it.")
            print("You choosed ", user_guess, ", but it should be lower.", sep="")
            print("Try again. You have", user_attempts_value,"attempts left.\n")
    elif user_guess < secret_number_value:
        user_attempts_value -= 1
        if not user_attempts_value:
            game_over()
        else:
            print("Pah! You missed it.")
            print("You choosed ", user_guess, ", but it should be higher.", sep="")
            print("Try again. You have", user_attempts_value,"attempts left.\n")


# ---------------------------- Initiationg objects ---------------------------- #
frame = simplegui.create_frame("Guess the number", 350, 300)
button_r100X = frame.add_button("Range is [0,100)", range100, 180)
button_r1000 = frame.add_button("Range is [0,1000)", range1000, 180)
player_input = frame.add_input("Enter your choice here", input_guess, 80)


# ---------------------------- Call for a new game ---------------------------- #
new_game()
frame.start()
