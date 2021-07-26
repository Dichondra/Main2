#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 17:17:12 2021

@author: franek
"""

file = open("Słowa","r")




def Main(string):
    number = 0
    for i in string:
       number += ord(i) - 96
    return number




lines = file.readlines()

for line in lines:
    x = Main(line)
    x += 86
    if x == 69:
        print(line)
  




# Odpowiedzi do zadania
#1 słowo to reinstitutionalizations
