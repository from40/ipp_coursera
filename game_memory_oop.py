
# implementation of card game - Memory
#

TILE_WIDTH = 50
TILE_HEIGHT = 80

class Tile:
    def __init__(self, number, exp, position):
        self.number = number
        self.exposed = exp
        self.position = position

    def get_number(self):
        return self.number

    def is_exposed(self):
        return self.exposed

    def expose_tile(self):
        self.exposed = True

    def hide_tile(self):
        self.exposed = False

    def is_selected(self, pos):
        if pos[0] > self.position[0] and pos[0] < (self.position[0] + TILE_WIDTH):
            return True
        else:
            return False

    def draw_tile(self, canvas):
        if self.exposed == True:
            canvas.draw_text(str(self.number),
                                (self.position[0] + 4,
                                 self.position[1] - 20
                                ),
                             90, "White")
        else:
            canvas.draw_polygon([(self.position[0], self.position[1] - TILE_HEIGHT),
                                 (self.position[0] + TILE_WIDTH, self.position[1] - TILE_HEIGHT),
                                 (self.position[0] + TILE_WIDTH, self.position[1]),
                                 self.position],
                                1, 'Black', 'Green')

    def __str__(self):
        return "Number is " + str(self.number) + ", exposed is " + str(self.exposed)





my_tile = Tile(3)
your_tile = Tile(4)






























# ___________________________ below is old code ___________________________#


import simplegui
import random

deck = [] # list of 16 random numbers between 0 and 7 (inluded)
state = 0 # how many cards a open at the current moment
exposed = [] # which of the deck index card is open
deck_x_axe = [] # tuples of range of coordinate for each card on x axe
card1 = None # index (in the deck) of 1st open card
card2 = None # index (in the deck) of 2nd open card
counter_turns = 0

# helper function to initialize globals
def new_game():
    global deck
    numbers_list = [i for i in range(0, 8)]
    random.shuffle(numbers_list)
    deck = numbers_list + numbers_list
    random.shuffle(deck)

    global state
    state = 0

    global exposed
    exposed = [False] * 16

    global deck_x_axe
    deck_x_axe = []
    for x1 in range(0, 800, 50):
        deck_x_axe.append((x1, x1 + 49))

    global card1, card2
    card1 = None
    card2 = None

    global counter_turns
    counter_turns = 0

    label.set_text("Turns = 0")

# define event handlers
def mouseclick(pos):
    global exposed, state, card1, card2, counter_turns
    x_axis_position = pos[0]
    # card_clicked = None
    for i in range(len(deck_x_axe)):
        if x_axis_position >= deck_x_axe[i][0] and \
           x_axis_position <= deck_x_axe[i][1]:
            #card_clicked = i
            if exposed[i]:
                pass
            else:
                exposed[i] = True
                # print(card_clicked)
                if state == 0:
                    state = 1
                    card1 = i
                elif state == 1:
                    counter_turns += 1
                    state = 2
                    card2 = i
                elif state == 2:
                    state = 1
                    if deck[card1] != deck[card2]:
                        exposed[card1] = False
                        exposed[card2] = False
                        card1 = i
                        card2 = None
                    else:
                        card1 = i
                        card2 = None
            print("state = ", state)
            print("card 1 = ", card1)
            print("card 2 = ", card2, "\n")
    label_text = "Turns = " + str(counter_turns)
    label.set_text(label_text)


# cards are logically 50x100 pixels in size
def draw(canvas):
    number_position = [0, 80]
    for i in range(len(deck)):
        if exposed[i]:
            canvas.draw_text(str(deck[i]), number_position, 90, "White")
            number_position[0] = number_position[0] + (800 / 16)
        else:
            canvas.draw_polygon([(number_position[0], 0),
                                (number_position[0] + (800 / 16) - 1, 0),
                                (number_position[0] + (800 / 16) - 1, 100),
                                (number_position[0], 100)],
                                1, 'Black', 'Green')
            number_position[0] = number_position[0] + (800 / 16)

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()
