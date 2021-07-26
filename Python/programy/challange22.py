#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 13:07:09 2021

@author: franek
"""


def nonogram(array):
    count = 0
    lista = []
    for i in array:
        if i == 1:
            count +=1
        if count != 0 and i == 0:
            lista.append(count)
            count = 0
    if array[-1] == 1:
        lista.append(count)
    print(lista)




            