# Script Name        :  settings.py
# Author             :  WhiteBombo
# Created            :  July 26th 2017
# Last modified      :
# Version            :  1.0
# Description        :  Settings file for timer.py.

# Timer settings:
topOfHour = False         # Force timer to countdown to top of hour (True/False)
finishMessage = ' '       # What is displayed when the timer runs out
defaultCountdownTime = 10 # Default countdown time in minutes
reductionAmount = 1       # How many seconds are reduced at each tick
tick = 1                  # How long is one tick in seconds

# String dictionaries
    # Customize time format to your liking
formats = {
        'singleSeconds': '{}',
        'fullSeconds': '{}:{}',
        'paddedSeconds': '{}:0{}',
        }

    # Add some dots or take away or whatever, mhm..
dots = {
        0: '.    ',
        1: '..   ',
        2: '...  ',
        3: '.... ',
        4: '.....'
        }

# Developer settings:
printClearEnable = True  # Is terminal cleared every tick
clear = 'cls'            # Terminal clearing command. Use 'cls' for windows, 'clear' for linux systems.
    # Query variables:
#reductionAmount = raw_input('Reduction per second? (Default: 1 s) ') or 1
#tick = 1 / (raw_input('Tickrate? (Default: 1 tick/sec) ') or 1)
#printClearEnable = raw_input('Clear command line at tick? (Default: True) ') or True
