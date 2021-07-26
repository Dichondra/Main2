#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 24 15:47:55 2021

@author: franek
"""


litery = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

zdanie = ""
ciąg = ""
x = ""
for i in litery[:20]:
    ciąg = i
    x = zdanie + i + zdanie
    zdanie = x


print(x)