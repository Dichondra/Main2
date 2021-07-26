#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 20:52:13 2021

@author: franek
"""

def change(number):
    reszta = 0
    while number - 500 > 0 or  number - 500 == 0:
        number -= 500
        reszta += 1
    while number - 100 > 0 or  number - 100 == 0:
        number -= 100
        reszta += 1
    while number - 25 > 0 or  number - 25 == 0:
        number -= 25
        reszta += 1
    while number - 10 > 0 or  number - 10 == 0:
        number -= 10
        reszta += 1
    while number - 5 > 0 or number - 5 == 0:
        number -= 5
        reszta += 1
    while number - 1 > 0 or number - 1 == 0:
        number -= 1
        reszta += 1
    print(reszta)



testy = [0,12,468,123456,999999992]

for test in testy:
    
    change(test)
    