#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 23:23:48 2021

@author: franek
"""

import random

x = random.randrange(1,100)
y = 101

while y != x:
    y = int(input("o jakiej liczbie myślę"))
    if y > x:
        print("lower")
    elif y < x:
        print("higher")
    else:
        print("you win")
        break