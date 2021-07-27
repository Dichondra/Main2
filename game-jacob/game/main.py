#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 13:46:42 2021

@author: franek
"""

import pygame
from sub_things.constants import HEIGHT, WIDTH, FPS
from sub_things.board import Board
WIN = pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption("Saper weird")



def Main():
    run = True
    clock = pygame.time.Clock()
    board = Board()
    
    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
            
        
        board.draw_squares(WIN)
        pygame.display.update()
    pygame.quit()





Main()