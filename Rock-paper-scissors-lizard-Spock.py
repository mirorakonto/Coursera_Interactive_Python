# Rock-paper-scissors-lizard-Spock

# http://www.codeskulptor.org/#user10_D3FlPcXz81gdEBI.py

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

import random

# Two helper functions

# 1st helper function
def number_to_name(num):
    # a helper function number_to_name(num) that converts 
    # a number in the range 0 to 4 into its corresponding 
    # name as a string using if/elif/else. 
    if num == 0:
        return "rock"
    elif num == 1:
        return "Spock"
    elif num == 2:
        return "paper"
    elif num == 3:
        return "lizard"
    elif num == 4:
        return "scissors"
    else:
        return "Please enter a positive integer \
        in the range from 1 to 4."
    
# 2nd helper function    
def name_to_number(name):    
    # a helper function name_to_number(name) that converts
    # the string name into a number between 0 and 4 
    # as described above.    
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        return "A written name does not match \
        any of the five correct input strings."

# The main function 
def rpsls(name): 
    # converts name to player_number using name_to_number
    player_number = name_to_number(name) 

    # computes random guess for comp_number using random.randrange()
    comp_number = random.randrange(0,5)

    # computes difference of player_number and comp_number modulo five
    diff = (player_number - comp_number) % 5
    # If clauses - determining winner:
    # if diff 1 or 2 player wins
    # if diff 3 or 4 computer wins
    # if diff 0 no one wins, it's a draw or it's a tie.

    # uses if/elif/else to determine winner
    if diff == 1 or diff == 2:
        winner = 'Player'
    elif diff == 3 or diff == 4:
        winner = 'Computer'
    elif diff == 0:
        winner = 'No one wins.'
    else:
        winner = 'Error'
        
    # converts player_number to name using number_to_name
    # player_chooses_name = number_to_name(player_number)
      
    # converts comp_number to name using number_to_name
    computer_chooses_name = number_to_name(comp_number) 
       
    # prints results
    print ""
    print "Player chooses",number_to_name(player_number)
    print "Computer chooses",computer_chooses_name 
    if diff > 0:   
        print winner, "wins!"
    elif diff == 0:
        print "Player and computer tie!"
    else:
        print "Error."

# tests my code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
