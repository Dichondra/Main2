#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 25 11:13:07 2021

@author: franek
"""
### Papier kamień i nozyce gra
import sys
import random
Wybory = ["K","N","P"]
x = 0
wins = 0
def askYorN(pytanie):
    print("Odpowiedz na to pytanie Y lub N: ")
    anwser = input(pytanie)
    anwser = anwser.upper()
    while anwser != "Y" or anwser != "N":
        if anwser == "Y":
            return True
        if anwser == "N":
            return False
        print("To nie jest Y lub N")
        anwser = input(pytanie)
        anwser = anwser.upper()        
        

def powitanie():
    print("Witaj w grze papier kamień i nożyce")
    if  askYorN("are you ready to play?\n") == False:
        sys.exit()
    else:
        pass

def zasady():
    print("Co ty głupi jesteś wybieraj kamień nożyce lub papier i tyle")

def wybór():
    choice = input("K - Kamień; P- Papier; N-Nożyce\nWybierz mądrze - ")
    choice = choice.upper()
    return choice    
    
def walka():
    global wins
    bot = random.choice(Wybory)
    choice = wybór()
    while choice not in ["K","k","P","p","N","n"]:
        choice = wybór()
    if bot == "K" and choice == "K":
        print("ja wybrałem :",bot,"remis")
    if bot == "K" and choice == "P":
        print("ja wybrałem :",bot,"przegrałem")
        wins += 1
    if bot == "K" and choice == "N":
        print("ja wybrałem :",bot,"Wygrałem")
    if bot == "P" and choice == "K":
        print("ja wybrałem :",bot,"Wygrałem")
    if bot == "P" and choice == "N":
        print("ja wybrałem :",bot,"Przegrałem")
        wins += 1
    if bot == "P" and choice == "P":
        print("ja wybrałem :",bot,"remis")
    if bot == "N" and choice == "K":
        print("ja wybrałem :",bot,"Przegrałem")
        wins += 1
    if bot == "N" and choice == "P":
        print("ja wybrałem :",bot,"Wygrałem")
    if bot == "N" and choice == "N":
        print("ja wybrałem :",bot,"remis")
   

def Main():
    global x
    if x == 0:
        powitanie()
        zasady()
    walka()
    x = 1
    if askYorN("chcesz zagrać ponownie?") == True:
        Main()
    else:
        print("Oto ile gier wygrałeś/aś: ",wins)
        print("bye bye")
        
Main()