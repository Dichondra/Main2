#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 14:14:26 2021

@author: franek
"""

import pygame
from .constants import BLACK,ROWS,SQUARE_SIZE,WHITE

class Board:
    def __init__(self):
        self.board = []
        self.selected_square = None
        
    def draw_squares(self,win):
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(row % 2,ROWS,2):
                pygame.draw.rect(win,WHITE,(row * SQUARE_SIZE,col* SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))