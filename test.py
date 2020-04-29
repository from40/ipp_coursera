point = [0, 0]

def function1():
    point[0] += 1
    point[1] += 2
# CodeSkulptor is tested to run in recent versions of
# Chrome, Firefox, and Safari.

import simplegui

circle_coord = [50, 50]
circle_radius = 10
vel = [0.5, 0.2]
time_interval = 1
acceleration = 1.2


# Handler for mouse click
def timer_handler():
    global circle_coord
    circle_coord[0] += vel[0]
    circle_coord[1] += vel[1]

# Handler to draw on canvas
def draw(canvas):
    global circle_coord, vel
    canvas.draw_circle(circle_coord, circle_radius, 0.1, 'Green', 'Green')
    circle_coord[0] = circle_coord[0] + (time_interval * vel[0])
    circle_coord[1] = circle_coord[1] + (time_interval * vel[1])
    vel[0] = vel[0] + (time_interval * acceleration)
    vel[1] = vel[1] + (time_interval * acceleration)



# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 500, 400)
frame.set_canvas_background('white')
timer = simplegui.create_timer(10000, timer_handler)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()
