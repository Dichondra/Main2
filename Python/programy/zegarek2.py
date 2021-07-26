

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 23 10:55:50 2021

@author: franek
"""

#stopwatch.py program do mierzenia czasu
#! python3
# stopwatch.py - A simple stopwatch program.

import time

# Display the program's instructions.
print('Press ENTER to begin. Afterward, press ENTER to "click" the stopwatch. Press Ctrl-C to quit.')
input()                    # press Enter to begin
print('Started.')
startTime = time.time()    # get the first lap's start time
lastTime = startTime
lapNum = 1

try:
    while True:
        input()
        lapTime = round(time.time()-lastTime,2)
        totalTime = round(time.time()-startTime,2)
        print('Lap #%s: %s (%s)' % (lapNum, totalTime, lapTime), end='')
        lapNum += 1
        lastTime = time.time()
except KeyboardInterrupt:
    print("\nDone")

# TODO: Start tracking the lap times.