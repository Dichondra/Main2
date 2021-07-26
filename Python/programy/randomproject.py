#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 25 12:07:17 2021

@author: franek
"""


import random
from words import words
word = random.choice(words)
print(word)

while word != "yoke":
    word = random.choice(words)
    
print(word)