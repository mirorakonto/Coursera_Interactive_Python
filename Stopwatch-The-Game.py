Mini-project description - "Stopwatch: The Game"

My code: http://www.codeskulptor.org/#user12_zmUQiKHky9I8F6K.py

http://www.codeskulptor.org/#examples-format_template.py

Junilu Lacar:

https://class.coursera.org/interactivepython-002/forum/thread?thread_id=3307

http://www.codeskulptor.org/#user12_lS4l5Lu47RVOqcP.py

http://www.youtube.com/watch?v=oUB2GTwVAqg&feature=youtube_gdata


##########################################################
#The Stopwatch Game

import simplegui

##########################################################
###########      SET OR INITIALIZE GLOBALS     ###########
##########################################################

width = 600
height = width
control_width = 250
interval = 100
BUTTON_SIZE = 150

timer_int = 0
success_stop = 0
total_stop = 0
last_stop = 0

##########################################################
###########          HELPER FUNCTIONS          ###########
##########################################################

def format(timer_int):
    # helper function format that converts time
    # in tenths of seconds into formatted string A:BC.D   
    A = timer_int // 600
    B = timer_int % 600 // 100
    C = timer_int % 100 // 10 
    D = timer_int % 10
    return str(A) + ":" + str(B) + str(C) + "." + str(D) 

##########################################################
##########      EVENT HANDLERS FOR BUTTONS      ##########
##########################################################

#DEFINE BUTTON HANDLERS - Handlers for mouse click
def startButton():
    timer.start()
    
def stopButton():
    # stops timer and increments success and attempt counters
    global timer_int, total_stop, success_stop, last_stop
    timer.stop()
    if last_stop != timer_int:
        total_stop = total_stop + 1
        if timer_int % 10 == 0:
            success_stop = success_stop + 1
    last_stop = timer_int    

def resetButton():
    # stops timer, resets timer and counters to zero
    global timer_int, total_stop, success_stop
    timer.stop()
    timer_int = 0
    total_stop = 0
    success_stop = 0   

def quit_gameButton():
    frame.stop()  

##########################################################
##########        EVENT HANDLER FOR TIMER       ##########
##########################################################    
#DEFINE TIMER HANDLER

def timer_handler():
    # define event handler for timer with 0.1 sec interval
    global timer_int
    timer_int = timer_int + 1
      
##########################################################
###########            DRAW HANDLERS           ###########
##########################################################
  
#DEFINE DRAW HANDLERS 
# Handler to draw on canvas
def draw_stopwatch(canvas):
    canvas.draw_text(format(timer_int), [width/4, height/2.5], width/6, "Red")
    canvas.draw_text(str(success_stop) + "/" + str(total_stop), (width/1.70, height/5), width/15, "Blue")
    
##########################################################
###########   initialize frame and handlers  #############
##########################################################     

#CREATE FRAME
frame = simplegui.create_frame("Stopwatch", width, height, control_width)

#REGISTER CANVAS BACKGROUND HANDLER 
# by default is black
frame.set_canvas_background("Black")

#REGISTER DRAW HANDLER
frame.set_draw_handler(draw_stopwatch)

#REGISTER BUTTON, LABEL AND INPUT HANDLERS
# The order of registration is key
# assign callbacks to event handlers
label = frame.add_label("THE STOPWATCH GAME")
frame.add_button("Start", startButton, BUTTON_SIZE)
frame.add_button("Stop", stopButton, BUTTON_SIZE)
frame.add_button("Reset", resetButton, BUTTON_SIZE)
label = frame.add_label("")
label = frame.add_label("")
label = frame.add_label("")
frame.add_button("Quit program", quit_gameButton, BUTTON_SIZE)

# Register timers
timer = simplegui.create_timer(interval, timer_handler)

# Start the frame
frame.start()

# Please remember to review the grading rubric

##########################################################
###########                TESTS             #############
##########################################################
# JUnit-style test harness for the format function
# You don't need to change anything in this section

def test(expected, timer_int, skip_test=0):
    global test_count, test_skip
    
    test_count += 1
    
    if skip_test:
        test_skip += 1
        return
    
    print "format(%3d) ==>" % timer_int,
    is_equal(expected, format(timer_int))

def is_equal(expected, actual):
    global test_pass, test_fail
    if expected == actual:
        test_pass += 1
        print actual, "(Pass)"
    else:
        test_fail += 1
        print "Fail>>> expected [%s] but got [%s]" % (str(expected), str(actual))

def test_stats():
    print
    print "Totals tests:", test_count,
    print "  Passed:", test_pass,
    print "  Failed:", test_fail,
    print "  Skipped:", test_skip
    print

    if test_count == 0:
        print "No tests were executed"
    elif  test_count == test_skip:
        print "All tests were skipped"
    else:
        print "RED" if test_fail else "GREEN", "BAR!"
        

# Output from test
test_count = 0
test_pass = 0
test_fail = 0
test_skip = 0

# pass as third parameter to test() to disable it
SKIP = True     

###################################################
# Test cases for the format() function.
#
# Note that format() should always return a string 
# with six characters. Add as many more test cases
# as you'd like...

test("0:00.0", 0)
test("0:00.1", 1) # Remove SKIP to activate test
test("0:00.7", 7)
test("0:01.7", 17)
test("0:06.0", 60)
test("0:06.3", 63)
test("0:21.4", 214)
test("0:59.9", 599)
test("1:00.0", 600)
test("1:00.2", 602)
test("1:06.7", 667)
test("2:12.5", 1325)
test("7:36.7", 4567)
test("9:59.9", 5999)
test("10:00.0", 6000)

###################################################
# Show summary

test_stats()
