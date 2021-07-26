#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 25 18:58:55 2021

@author: franek
"""

import pyautogui, random
# pozycja pisania x=594 y= 976

def position():
    pyautogui.moveTo(656, 973)
    pyautogui.click()
    

#figury = ["","k","N","R","B","Q",]
kolumny = ["a","b","c","d","e","f","g","h"]
rzędy = ["1","2","3","4","5","6","7","8"]

#figury =[""]
#kolumny = ["e"]
#rzędy =  ["4"]
def ruch():
    position()
    #a = str(random.choice(figury))
    b = str(random.choice(kolumny))
    c = str(random.choice(rzędy))
    for i in range(10):
        pyautogui.press("delete")
    #pyautogui.typewrite(a)
    pyautogui.typewrite(b)
    pyautogui.typewrite(c)
    pyautogui.typewrite(b)
    pyautogui.typewrite(c)
    pyautogui.press("enter")
    
def main(): 
    for i in range (100):
            ruch()
  

try:        
    main()
except KeyboardInterrupt:
        print("\nDone")