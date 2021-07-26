#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 25 18:58:55 2021

@author: franek
"""

import pyautogui, random, time

# pozycja pisania x=594 y= 976

def position():
    pyautogui.moveTo(594, 976)
    pyautogui.click()
    

figury = ["","k","N","R","B","Q",]
kolumny = ["a","b","c","d","e","f","g","h"]
rzędy = ["1","2","3","4","5","6","7","8"]


def ruch():
    position()
    a = random.choice(figury)
    a = str(a)
    b = random.choice(kolumny)
    b = str(b)
    c = random.choice(rzędy)
    c = str(c)
    pyautogui.typewrite(a)
    pyautogui.typewrite(b)
    pyautogui.typewrite(c)
    pyautogui.press("enter")
    for i in range(3):
        pyautogui.press("delete")
    
for i in range (1000):
    1
    ke7
    