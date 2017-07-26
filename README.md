CountdownTimer
==============

## Simple timer written in Python 3.
#### Description:
CountdownTimer is a simple timer written in [Python 3](https://www.python.org), that spits out a text string in a .txt file in the same directory.

#### New in version 1.2:
* A new settings file was added to bundle all configurable variables in one place.
* Timer and topOfHour scripts have been combined into one. Switching between custom timer and top of the hour timer can be done in 'settings.py' -file.
* Added an option to change a custom finish message to 'settings.py' to display after the timer hits 0.

#### Important for non-Windows users!
Command line/terminal clearing is only enabled to work on a Windows operating system. If you encounter errors on Linux or Mac, see the end of 'settings.py' -file for a setting that fixes this.

#### Use case
The script has been created to be used in [OBS](https://obsproject.com) or similar video broadcast software to make a countdown timer using a text source. By doing this, user may easily make custom text formatting of their choice.

#### Requirements
Made using Python 3.6.2rc2 as a runtime environment. The script will not work with Python 2, so be sure you're using [Python version 3](https://www.python.org/downloads) or further.

#### How to use
Once you have [Python 3](https://www.python.org) installed, all you need to do is run the script with it. Once the script has been started, you may enter a countdown time in minutes. (If the initial countdown time is left blank, timer will be set for 10 minutes.)

If you wish to countdown to a top of the hour, you may change the setting ```True``` in 'settings.py'. When this is enabled, you cannot enter a custom time.

Once the program has been given a time (default or custom), it will begin to write to a 'timer.txt'-file in the same directory as the script is in. Custom time will be given in minutes, but also supports float values (e.g. 0.5 for 30 seconds).

Edit 'settings.py' -file for further configuration.
