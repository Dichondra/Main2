#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 21:21:59 2021

@author: franek
"""

from collections import Counter
import random
import matplotlib.pyplot as plt

rzuty = []
liczba_wynik = []

def roll(number):
    for i in range(number):
        x = random.randrange(1,5)
        y = random.randrange(1,5)
        z = random.randrange(1,5)
        l = random.randrange(1,5)
        k = random.randrange(1,5)
        suma = x+y+z+l+k
        rzuty.append(suma)
    rzuty.sort()
    
def main():
    wybór = int(input("ile chcesz rzutów: "))
    x = roll(wybór)
    wyniki = dict(Counter(rzuty))
    for i in range(20):
        if i + 1 in wyniki:
            liczba_wynik.append(wyniki[i+1])
        else:
            liczba_wynik.append(0)
    procentowe = []
    
    for i in liczba_wynik:
        x = (i/wybór) * 100
        procentowe.append(x)
    
    left = range(1,21)
    height = procentowe
    tick_label = range(1,21)
    plt.bar(left,height, tick_label = tick_label, width = 0.5, color = ["pink"])
    plt.show()
    
main()