#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 30 12:26:53 2021

@author: franek
"""

import random

def ułatwienie():
    x = random.randrange(1,20)
    y = random.randrange(1,20)
    if x > y :
        return x
    else:
        return y
    

def chaos():
    x= random.randrange(1,20)
    if x <= 10:
        x = random.randrange(1,20)
    return x



Ułatwienie_suma = 0
chaos_suma = 0
n = 1000000

for i in range(n):
    Ułatwienie_suma += ułatwienie()
    chaos_suma += chaos()
    
Ułatwienie_suma /= n
chaos_suma /= n

print(Ułatwienie_suma)
print(chaos_suma)

