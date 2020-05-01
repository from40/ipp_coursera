import simplegui
import random

TILE_WIDTH = 50
TILE_HEIGHT = 100

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


deck = []
state = 0
counter_turns = 0
first_tile = None
second_tile = None


def new_game():
    global deck, state, counter_turns, first_tile, second_tile
    state = 0
    counter_turns = 0
    first_tile = None
    second_tile = None
    label.set_text("Turns = " + str(counter_turns))

    numbers_list = [i for i in range(0, 8)]
    random.shuffle(numbers_list)
    numbers_list = numbers_list + numbers_list
    random.shuffle(numbers_list)
    deck = []
    for i in range(16):
        deck.append(Tile(numbers_list[i], False, [TILE_WIDTH * i, TILE_HEIGHT]))


def draw(canvas):
    global deck
    for i in range(len(deck)):
        deck[i].draw_tile(canvas)


def mouseclick(pos):
    global state, counter_turns, first_tile, second_tile
    for tile in deck:
        if tile.is_selected(pos):
            if tile.is_exposed():
                pass
            else:
                tile.expose_tile()
                if state == 0:
                    state = 1
                    first_tile = tile
                elif state == 1:
                    counter_turns += 1
                    state = 2
                    second_tile = tile
                elif state == 2:
                    state = 1
                    if first_tile.get_number() != second_tile.get_number():
                        first_tile.hide_tile()
                        second_tile.hide_tile()
                        first_tile = tile
                        second_tile = None
                    else:
                        first_tile = tile
                        second_tile = None
    label.set_text("Turns = " + str(counter_turns))


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
button = frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")


# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)


# get things rolling
new_game()
frame.start()
