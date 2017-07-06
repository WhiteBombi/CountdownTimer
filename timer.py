# Script Name        :  timer.py
# Author             :  WhiteBombo
# Created            :  July 6th 2017
# Last modified      :
# Version            :  1.0
# Description        :  Timer that writes remaining time in a file in same directory.

from datetime import datetime, timedelta
from time import sleep
import os, sys

## String dictionaries
formats = {
        'singleSeconds': '{}',
        'fullSeconds': '{}:{}',
        'paddedSeconds': '{}:0{}',
        }

dots = {
        0: '.    ',
        1: '..   ',
        2: '...  ',
        3: '.... ',
        4: '.....'
        }

## String processing functions
def spit(minutes, seconds):
    if minutes == 0:
        output = formats['singleSeconds'].format(seconds)
    elif minutes > 0 and seconds < 10:
        output = formats['paddedSeconds'].format(minutes, seconds)
    else:
        output = formats['fullSeconds'].format(minutes, seconds)
    file.write(output)
    return output

def cmdPrint(i, printClearEnable):
    if printClearEnable == True:
        os.system('cls')
    print('Script running{} [{}]'.format(dots[i], output))

def kill():
    file = open("timer.txt", "w")
    file.write(' ')
    file.close()

## Settings
# Initial countdown time calculation
defaultCountdown = 10
now = datetime.now
cdTime = int(float(raw_input('How many minutes? (Default: {}) '.format(defaultCountdown)) or 10) * 60)

# Amount of seconds reduced from countdown per tick
reduction = 1
#reduction = raw_input('Reduction per second? (Default: 1 s) ') or 1
# Amount of time between each tick
tick = 1
#tick = 1 / (raw_input('Tickrate? (Default: 1 tick/sec) ') or 1)
# Cmd line output counter needs an integer
i = 0
printClearEnable = True
#printClearEnable = raw_input('Show only one line in command line? (Default: True) ') or True

## Actual process
try:
    while True:
        # Divide countdown time into minutes and seconds
        minutes = int(cdTime / 60)
        seconds = cdTime % 60

        # Formats, writes and outputs strings
        file = open("timer.txt", "w")
        if minutes <= 0 and seconds < reduction: # Exit condition
            file.write('0')
            file.close()
            sleep(tick)
            break
        output = spit(minutes, seconds)
        file.close()

        # Print stuff to command line
        if printClearEnable == True:
            cmdPrint(i, True)
        else:
            cmdPrint(i, False)
        i = (i + 1) % len(dots)

        cdTime -= reduction
        sleep(tick)
except KeyboardInterrupt:
    kill()
    print('buh bye')
    sleep(tick)
    sys.exit()

kill()
print('Program terminated. Until we meet again. ~')
sleep(5)
