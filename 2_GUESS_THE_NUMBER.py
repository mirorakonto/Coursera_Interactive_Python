GUESS THE NUMBER: 

http://www.codeskulptor.org/#user11_Gg2WnlLmR8Gqc0M.py

http://www.codeskulptor.org/#examples-guess_the_number_template.py

http://www.codeskulptor.org/#examples-gtn_testing_template.py


# "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console


import simplegui
import random
import math

# initialize global variables used in your code
low = 0
high = 100

# helper function to initial game 
def init():
    global low, high, guesses_left, secret_number
    guesses_left = math.ceil(math.log(high - low + 1, 2)) 
    secret_number = random.randrange(low, high)
    print "New game. Range is from " + str(low) + " to " + str(high)
    print "Number of remaining guesses is " + str(guesses_left) + "\n"
            
# define event handlers for control panel  
def range100():
    # button that changes range to range [0,100) and restarts
    global high
    high = 100
    init()
    
def range1000():
    # button that changes range to range [0,1000) and restarts
    global high
    high = 1000
    init()    
    
def input_guess(guess):
    # main game logic goes here
    global guesses_left
                     
    print "Guess was", guess
    player_number = int(guess)
    guesses_left = guesses_left - 1
    print "Number of remaining guesses is " + str(guesses_left)
        
    if guesses_left > 0:
        if player_number == secret_number:
            print "Correct! \n"
            init()
        elif player_number < secret_number:
            print "Higher! \n"      
        else: 
            print "Lower! \n"
    elif guesses_left == 0:
        if player_number == secret_number:
            print "Correct! \n"
            init()
        else: 
            print "You ran out of guesses. The number was " + str(secret_number) + "\n"
            init()    
   
# create frame
f = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements
f.add_button("Range is [0, 100)", range100, 200)
f.add_button("Range is [0, 1000)", range1000, 200)
f.add_input("Enter a guess", input_guess, 200)

init()

# start frame
f.start()
# always remember to check your completed program against the grading rubric
