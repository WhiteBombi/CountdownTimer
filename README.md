CountdownTimer
==============

## Simple timer written in Python 3.
#### Description:
CountdownTimer is a simple timer written in Python 3, that spits out a text string in a .txt file in the same directory.

#### Important for non-Windows users!
Command line/terminal clearing is only enabled to work on a Windows operating system. If you encounter errors on Linux or Mac, switch the line 40 in 'timer.py' from ```os.system('cls')``` to ```os.system('clear')``` Be careful not to change indentation in the line. (The line should have 8 spaces behind it.)

#### Use case
The script has been created to be used in OBS or similar video broadcast software in order to achieve a countdown timer using a text source. By doing this, user is left to easily make custom text formatting of their choice.

By design it will update the output time every second, but can be configured to update at a set interval by editing the code. Any broadcast software used may have their own internal processing delay for reading text inside a file, which may cause inaccurate performance.

#### Requirements
Made using Python 3.5.2 as a runtime environment. The script will not work with Python 2, so be sure you're using Python version 3 or further.

#### How to use
Once you have Python 3 installed, all you need to do is run the script with it. Once the script has been initialized, an initial countdown time may be inserted. (If the initial countdown time is left blank, timer will be set for 10 minutes.)

Once the program has been given a time (default or custom), it will begin to write to a 'timer.txt'-file in the same directory as the script is in. Custom time will be given in minutes, but also supports float values (e.g. 0.5 for 30 seconds).

#### Custom features
The script itself has commented out lines that can be used to provide further customizability. Current additional features are as follows.

| Feature          | Used for                | Line number  |
| ---------------- |:------------------------| :-----------:|
| reduction              | Amount of seconds reduced from the timer at each tick.                                        |      55      |
| tick             | Speed at which new time is processed within the script.                                      |      58      |
| printClearEnable | Whether or not the command line/terminal is cleared after each tick. Useful to turn off if the testing in an IDE.           |      62      |
