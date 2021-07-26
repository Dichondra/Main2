#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 23:33:01 2021

@author: franek
"""

import random


print("pomyśl o liczbie a ja spróbuję ją zgadnąć")
print("1 - niżej / 2 wyżej / 3 zgadłeś")

choice = int(input("choice = "))
low = 0
high = 100

while choice != 3:

    if choice == 1:
        pass
    elif choice == 2:
        pass
    elif choice == 3:
        print("wygrałem")
        break
    else:
        print("invalid")
        
    choice = int(input("1 - niżej / 2 wyżej / 3 zgadłeś : "))

