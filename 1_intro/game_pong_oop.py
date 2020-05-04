



class Paddle:
    def __init__(self):
        pass


class Ball:
    def __init__(self):
        pass



# version 1
key_inputs = {"w": paddle2_up, "s": paddle2_down,
              "up": paddle2_up, "down": paddle2_down}

def keydown(key):
    for i in key_inputs:
        if key == simplegui.KEY_MAP[i]:
            key_inputs[i]()


# version 2
# global value "paddle_velocity" which is an array of our two paddles
key_inputs = {"w": [1, -2], "s": [1, 2],
              "up": [2, -2], "down": [2, 2]}

def keydown(key):
    for i in key_inputs:
        if key == simplegui.KEY_MAP[i]:
            paddle_velocity[key_inputs[i][0]] += key_inputs[i][1]
