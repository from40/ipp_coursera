# https://py3.codeskulptor.org/#user305_gaXLQCIhDw8dbfk.py

# template for "Stopwatch: The Game"
import simplegui


# define global variables
wigth = 500
hight = 400
button_wigth = 80
time_tracker = 0
flag_running = False
counter_stops = 0
counter_stops_hit = 0


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    time_list = ["0", ":", "0", "0", ".", "0"]
    d = t % 10
    c = (t // 10) % 10
    b = (t // 100) % 6
    a = (t // 100) // 6
    time_list[0] = str(a)
    time_list[2] = str(b)
    time_list[3] = str(c)
    time_list[5] = str(d)
    return("".join(time_list))


# define event handlers for buttons; "Start", "Stop", "Reset"
def run_timer():
    global time_tracker
    time_tracker += 1


def start_game():
    global flag_running
    timer.start()
    flag_running = True


def stop_game():
    global flag_running, counter_stops, counter_stops_hit
    if flag_running == True:
        counter_stops += 1
        if time_tracker % 10 == 0:
            counter_stops_hit += 1
    timer.stop()
    flag_running = False


def reset_game():
    global time_tracker, flag_running, counter_stops, counter_stops_hit
    timer.stop()
    print(time_tracker / 10)
    time_tracker = 0
    flag_running = False
    counter_stops = 0
    counter_stops_hit = 0

# define draw handler
def draw_handler(canvas):
    csh_calc = 1
    if counter_stops > 1:
        csh_calc = counter_stops
    canvas.draw_text(format(time_tracker),
                     (wigth // 2 - 30, hight // 2), 30, "White"
                     )
    canvas.draw_text("Total stops are {}".format(counter_stops),
                     (wigth // 20, hight // 18), 15, "White"
                     )
    canvas.draw_text("Stops at a whole second are {}".format(counter_stops_hit),
                     (wigth // 20, hight // 10), 15, "White"
                     )
    canvas.draw_text("Success rate is {:.2f}".format(counter_stops_hit / csh_calc),
                     (wigth // 2 + 50, hight // 10), 15, "Red"
                     )


# create frame
frame = simplegui.create_frame("Stopwatch Game", wigth, hight)


# register event handlers
frame.set_draw_handler(draw_handler)
button_start = frame.add_button("Start", start_game, button_wigth)
button_stop = frame.add_button("Stop", stop_game, button_wigth)
button_reset = frame.add_button("Reset", reset_game, button_wigth)
timer = simplegui.create_timer(100, run_timer)


# start frame
frame.start()
