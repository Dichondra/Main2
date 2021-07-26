#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 26 11:25:33 2021

@author: franek
"""
### wysajzuj czerwony statek !!!


import pygame
import os
pygame.font.init()
pygame.mixer.init()


WIDTH, HEIGHT, = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Franek is great!")


WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)


BORDER = pygame.Rect(WIDTH//2 - 5, 0,10, HEIGHT)

HEALTH_FONT = pygame.font.SysFont('comicsans',40)
WINNER_FONT = pygame.font.SysFont("comicsans",100)

FPS = 60
VEL = 5
BULLET_SPEED = 10
MAX_BULLETS = 3


SPACESHIP_WIDTH, SPACESHIP_HIGHT = 55, 40


YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2

BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join("PygameForBeginners-main","Assets","orgasm.wav"))
BULLET_FIRE_SOUND = pygame.mixer.Sound(os.path.join("PygameForBeginners-main","Assets","cat.wav"))


YELLOW_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join("PygameForBeginners-main","Assets","spaceship_yellow.png"))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE,(SPACESHIP_WIDTH, SPACESHIP_HIGHT)), 90)
RED_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join("PygameForBeginners-main","Assets","spaceship_red.png"))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE,(SPACESHIP_WIDTH, SPACESHIP_HIGHT)), 270)

SPACE =pygame.transform.scale(pygame.image.load(os.path.join("PygameForBeginners-main","Assets","space.png")),(WIDTH, HEIGHT))


def draw_window(red, yellow, red_bullets, yellow_bullets, RED_HP, YELLOW_HP):
    WIN.blit(SPACE,(0,0))
    pygame.draw.rect(WIN,BLACK, BORDER )
    
    
    
    
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y ))
    WIN.blit(RED_SPACESHIP,(red.x,red.y))
    
    
    red_health_font = HEALTH_FONT.render("Health: "+ str(RED_HP), 1, WHITE)
    yellow_health_font = HEALTH_FONT.render("Health: "+ str(YELLOW_HP), 1, WHITE)
    WIN.blit(red_health_font, (WIDTH - red_health_font.get_width() - 10, 10))
    WIN.blit(yellow_health_font,(10,10))

        
    for bullet in red_bullets:
        pygame.draw.rect(WIN, RED, bullet)
    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet)
    
        
    pygame.display.update()
    

def yellow_movement(keys_pressed,yellow):
    if keys_pressed[pygame.K_a] and yellow.x - VEL > 0: # left
            yellow.x -= VEL
    if keys_pressed[pygame.K_w] and yellow.y - VEL > 0: # up
            yellow.y -= VEL
    if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < BORDER.x: # right
            yellow.x += VEL
    if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height < HEIGHT - 10: # down
            yellow.y += VEL
            
def red_movement(keys_pressed,red):
    if keys_pressed[pygame.K_LEFT] and red.x - VEL > BORDER.x + BORDER.width: # left
            red.x -= VEL
    if keys_pressed[pygame.K_UP] and red.y - VEL > 0: # up
            red.y -= VEL
    if keys_pressed[pygame.K_RIGHT] and red.x + VEL + red.width < WIDTH: # right
            red.x += VEL
    if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height < HEIGHT - 10: # down
            red.y += VEL
 

def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width() /
                         2, HEIGHT/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)

             
def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    for bullet in yellow_bullets:
        bullet.x += BULLET_SPEED
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            yellow_bullets.remove(bullet)
    for bullet in red_bullets:
        bullet.x -= BULLET_SPEED
        if yellow.colliderect(bullet):
             pygame.event.post(pygame.event.Event(YELLOW_HIT))
             red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet)
             
    
    
def main():
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH,SPACESHIP_HIGHT)
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH,SPACESHIP_HIGHT)
    red_bullets = []
    yellow_bullets = []
    YELLOW_HP = 10
    RED_HP = 10
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
               
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height/2 -2, 10, 5)
                    yellow_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()
                
                if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:  
                    bullet = pygame.Rect(red.x, red.y + red.height//2 -2, 10, 5)
                    red_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()
                    
            if event.type == RED_HIT:  
                RED_HP -= 1
                BULLET_HIT_SOUND.play()
            if event.type == YELLOW_HIT:
                YELLOW_HP -= 1
                BULLET_HIT_SOUND.play()
        winner_text = ""
        
        if RED_HP <= 0:
            winner_text = "Yellow wins!!!"
            
        if YELLOW_HP <= 0:
            winner_text = "Red wins!!!"
        
        if winner_text != "":
            draw_winner(winner_text)
            break
        
        
        keys_pressed = pygame.key.get_pressed()
        yellow_movement(keys_pressed,yellow)
        red_movement(keys_pressed, red)
        
        handle_bullets(yellow_bullets, red_bullets, yellow, red)
        
        
        draw_window(red, yellow, red_bullets,yellow_bullets,RED_HP, YELLOW_HP)
        
    main()
    
    
    
if __name__ == "__main.py_":
    main() 
