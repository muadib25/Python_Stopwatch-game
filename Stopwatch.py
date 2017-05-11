# template for "Stopwatch: The Game"
# Added a blinking ":" colon, LCD shadows as well as 
# an option to run old-timer LCD flickering on and off. Enjoy!!!
import simplegui



# define global variables
time = 0
time2 = 0
color1 = "Maroon"
color2 = "Red"
col3 = "Red"
col4 = "Blue"
tries = 0
success = 0
stopwatch_running = False
flicker_instant = 0
flicker_start = False

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    return str((t % 10000 - t % 600)/600) + " " + str((t % 600 - t % 100)/100) + str((t % 100 - t % 10)/10) + "." + str(t % 10)
    
    
# define event handler for timer with 0.1 sec interval
def timer1_handler():
    global time
    time += 1

# Timer for the ":" blinking.
def timer2_handler():
    global time2, color1, color2
    if time % 10 <= 4:
        color1 = "Maroon"
        color2 = "Red"
    else:
        color1 = "Black"
        color2 = "Black"

# Flickering handler
def flicker_handler():
    global flicker_instant, col3, col4, color2
    if flicker_instant != 0:
        if time % 10 <= 4:
            color2 = "Maroon"
        else:
            color2 = "Black"
        col3 = "Maroon"
        col4 = "Navy"
        flicker_instant = 0
    else:
        if time % 10 <= 4:
            color2 = "Red"
        else:
            color2 = "Black"
        col3 = "Red"
        col4 = "Blue"
        flicker_instant = 1

# define event handlers for buttons;    
# What the "Start" buton should do
def timer_start():
    global stopwatch_running
    timer.start()
    timer2.start()
    stopwatch_running = True

# What the "Stop" buton should do    
def timer_stop():
    global stopwatch_running, tries, success
    timer.stop()
    timer2.stop()
    if stopwatch_running == True:
        tries += 1
        if time % 10 == 0:
            success += 1
    stopwatch_running = False

# What the "Reset" button should do
def timer_reset():
    global time, tries, success 
    time = 0
    tries = 0
    success = 0
    
# What the "Flicker" button should do
def flicker_toggle():
    global flicker_start, col3, col4, color2
    if flicker_start == True:
        flicker.stop()
        flicker_handler()
        color2 = "Red"
        col3 = "Red"
        col4 = "Blue"
        flicker_start = False
    else:
        flicker.start()
        flicker_start = True
    
    
# define draw handler
def draw(canvas):
    canvas.draw_text(str(format(time)), (138,174), 45, "Maroon", "sans-serif")
    canvas.draw_text(str(format(time)), (134,170), 46, col3, "sans-serif")
    canvas.draw_text(":", (167, 171), 46, color1, "sans-serif")
    canvas.draw_text(":", (163, 167), 46, color2, "sans-serif")
    canvas.draw_text(str(success), (274, 54), 41, "Navy", "serif")
    canvas.draw_text(str(success), (270, 50), 41, col4, "serif")
    canvas.draw_text("/", (304, 54), 44, "Navy", "monospace")
    canvas.draw_text("/", (300, 50), 44, col4, "monospace")
    canvas.draw_text(str(tries), (334, 54), 41, "Navy", "serif")
    canvas.draw_text(str(tries), (330, 50), 41, col4, "serif")
    
# create frame
frame = simplegui.create_frame("Timer", 400, 300)
frame.add_button("Start", timer_start, 150)
frame.add_button("Stop", timer_stop, 150)
frame.add_button("Reset", timer_reset, 150)
frame.add_button("Flicker on/off", flicker_toggle, 150) 


# register event handlers
timer = simplegui.create_timer(100, timer1_handler)
timer2 = simplegui.create_timer(100, timer2_handler)
frame.set_draw_handler(draw)
flicker = simplegui.create_timer(33, flicker_handler)


# start frame
frame.start()

