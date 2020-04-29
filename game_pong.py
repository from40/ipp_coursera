# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
# LEFT = False
# RIGHT = True
direction = "RIGHT"

paddle1_pos = HEIGHT // 2
paddle2_pos = HEIGHT // 2

paddle1_vel = 0
paddle2_vel = 0

player_b = 0
player_a = 0


# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left

def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH // 2, HEIGHT // 2]
    ball_vel = [0, 0]
    if direction == "RIGHT":
        side = 1
    elif direction == "LEFT":
        side = -1
    ball_vel[0] = random.randrange(2, 4) * side
    ball_vel[1] = random.randrange(1, 3)


# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    spawn_ball(direction)


def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, player_a, player_b

    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")

    # update ball
    ball_pos[0] = ball_pos[0] + ball_vel[0]
    ball_pos[1] = ball_pos[1] + ball_vel[1]

    # reflection horizontally
    if ((ball_pos[0] - BALL_RADIUS) < PAD_WIDTH):
        if ball_pos[1] < (paddle1_pos + HALF_PAD_HEIGHT) and \
           ball_pos[1] > (paddle1_pos - HALF_PAD_HEIGHT):
           ball_vel[0] = (ball_vel[0] * -1) * 1.1
        else:
            player_a += 1
            spawn_ball("RIGHT")
    elif ((ball_pos[0] + BALL_RADIUS) > (WIDTH - PAD_WIDTH)):
        if ball_pos[1] < (paddle2_pos + HALF_PAD_HEIGHT) and \
           ball_pos[1] > (paddle2_pos - HALF_PAD_HEIGHT):
           ball_vel[0] = (ball_vel[0] * -1) * 1.1
        else:
            player_b += 1
            spawn_ball("LEFT")

    # reflection vertically
    if ((ball_pos[1] - BALL_RADIUS) <= 0) or \
       ((ball_pos[1] + BALL_RADIUS) >= HEIGHT):
        ball_vel[1] = ball_vel[1] * -1

    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 0.1, "white", "white")

    # update paddle's vertical position, keep paddle on the screen
    if ((paddle1_pos + paddle1_vel) - HALF_PAD_HEIGHT >= 0) and \
       ((paddle1_pos + paddle1_vel) + HALF_PAD_HEIGHT <= HEIGHT):
        paddle1_pos = paddle1_pos + paddle1_vel

    if ((paddle2_pos + paddle2_vel) - HALF_PAD_HEIGHT >= 0) and \
       ((paddle2_pos + paddle2_vel) + HALF_PAD_HEIGHT <= HEIGHT):
        paddle2_pos = paddle2_pos + paddle2_vel

    # draw paddles
    paddle1_object = [
                      [0, paddle1_pos - HALF_PAD_HEIGHT],
                      [PAD_WIDTH, paddle1_pos - HALF_PAD_HEIGHT],
                      [PAD_WIDTH, paddle1_pos + HALF_PAD_HEIGHT],
                      [0, paddle1_pos + HALF_PAD_HEIGHT]
                     ]
    canvas.draw_polygon(paddle1_object, 1, "white", "white")
    paddle2_object = [
                      [WIDTH - PAD_WIDTH, paddle2_pos - HALF_PAD_HEIGHT],
                      [WIDTH, paddle2_pos - HALF_PAD_HEIGHT],
                      [WIDTH, paddle2_pos + HALF_PAD_HEIGHT],
                      [WIDTH - PAD_WIDTH, paddle2_pos + HALF_PAD_HEIGHT]
                     ]
    canvas.draw_polygon(paddle2_object, 1, "white", "white")

    # draw scores
    canvas.draw_text(str(player_b), [140, 50], 25, 'Grey')
    canvas.draw_text(str(player_a), [450, 50], 25, 'Grey')

def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = -2
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 2
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel = -2
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 2

def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = 0
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 0
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel = 0
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)


# start frame
new_game()
frame.start()
