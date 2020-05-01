# http://www.codeskulptor.org/#examples-blackjack.py
# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank),
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)

# define hand class
class Hand:
    def __init__(self):
        self.cards_in_hand = []

    def __str__(self):
        # return a string representation of a hand
        hands_view = ""
        for card in self.cards_in_hand:
            hands_view = hands_view + str(card.get_suit()) + str(card.get_rank()) + " "
        return "Hand contains " + hands_view

    def add_card(self, card):
        # add a card object to a hand
        self.cards_in_hand.append(card)

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        hand_value = 0
        aces = False
        for card in self.cards_in_hand:
            hand_value += VALUES[card.get_rank()]
            if card.get_rank() == "A":
                aces = True
        if not aces:
            return hand_value
        else:
            if hand_value + 10 <= 21:
                return hand_value + 10
            else:
                return hand_value


    def draw(self, canvas, pos):
        pass	# draw a hand on the canvas, use the draw method for cards


# define deck class
class Deck:
    def __init__(self):
        # create a Deck object
        self.deck = [Card(i, j) for i in SUITS for j in RANKS]

    def shuffle(self):
        # shuffle the deck
        random.shuffle(self.deck)

    def deal_card(self):
        # deal a card object from the deck
        return self.deck.pop(-1)

    def __str__(self):
        # return a string representing the deck
        deck_view = ""
        for card in self.deck:
            deck_view = deck_view + str(card.get_suit()) + str(card.get_rank()) + " "
        return "Deck contains " + deck_view


#define event handlers for buttons
def deal():
    global outcome, in_play, deck, player_hand, dealer_hand
    deck = Deck()
    deck.shuffle()
    player_hand = Hand()
    dealer_hand = Hand()
    in_play = True
    # your code goes here
    player_hand.add_card(deck.deal_card())
    player_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())
    print("Player " + str(player_hand))
    print("Dealer " + str(dealer_hand))


def hit():
    pass	# replace with your code below

    # if the hand is in play, hit the player

    # if busted, assign a message to outcome, update in_play and score

def stand():
    pass	# replace with your code below

    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score

# draw handler
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below

    card = Card("S", "A")
    card.draw(canvas, [300, 300])


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric





def stand():
    pass	# replace with your code below

    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    """
    while the value of the dealer's hand (use value methods) is less than 17:
        hit the dearler's hand (use hit function)

    """


# Grading rubric - 18 pts total (scaled to 100)

# 1 pt - The program opens a frame with the title "Blackjack" appearing on the canvas.
# 3 pts - The program displays 3 buttons ("Deal", "Hit" and "Stand") in the control area. (1 pt per button)
# 2 pts - The program graphically displays the player's hand using card sprites.
#		(1 pt if text is displayed in the console instead)
# 2 pts - The program graphically displays the dealer's hand using card sprites.
#		Displaying both of the dealer's cards face up is allowable when evaluating this bullet.
#		(1 pt if text displayed in the console instead)
# 1 pt - Hitting the "Deal" button deals out new hands to the player and dealer.
# 1 pt - Hitting the "Hit" button deals another card to the player.
# 1 pt - Hitting the "Stand" button deals cards to the dealer as necessary.
# 1 pt - The program correctly recognizes the player busting.
# 1 pt - The program correctly recognizes the dealer busting.
# 1 pt - The program correctly computes hand values and declares a winner.
#		Evalute based on player/dealer winner messages.
# 1 pt - The dealer's hole card is hidden until the hand is over when it is then displayed.
# 2 pts - The program accurately prompts the player for an action with the messages
#        "Hit or stand?" and "New deal?". (1 pt per message)
# 1 pt - The program keeps score correctly.


draw_method for cards:
card_size[x, y]
card_center[x / 2, y / 2]
card_raw_number = j
card_column_number = i

card_pos = [card_center[0] + (card_column_number * card_size[0]),
            card_center[1] + (card_raw_number * card_size[1])
           ]




# define globals for cards
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
SUITS = ('C', 'S', 'H', 'D')

# card sprite - 950x392
CARD_CENTER = (36.5, 49)
CARD_SIZE = (73, 98)
card_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")



# define card class
class Card:
    def __init__(self, suit, rank):
        self.rank = rank
        self.suit = suit

    def draw(self, canvas, loc):
        i = RANKS.index(self.rank)
        j = SUITS.index(self.suit)
        card_pos = [CARD_CENTER[0] + i * CARD_SIZE[0],
                    CARD_CENTER[1] + j * CARD_SIZE[1]]
        canvas.draw_image(card_image, card_pos, CARD_SIZE, loc, CARD_SIZE)
