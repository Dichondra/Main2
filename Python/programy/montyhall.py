#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 12 19:00:12 2021

@author: franek
"""


### monty hall problem


###są 3 drzwi, prowadzący losowo wybiera jedne z nich i jest za nimi nagroda, za pozostałymi nie ma nic
### gracz wybiera drzwi 
### prowadzący odsłania drzwi za którymi nie ma nagrody i któ©ych nie wybrał gracz
### gracz decyduje się czy pozostać przy swoim wyborze czy zmienić na drzwi który pozostały
### gracz wygrywa jeśli wybrał drzwi z nagrodą

# strategie :
    #Alice - wybiera drzwi #1 i nie zmienia nigdy
    #Bob - wybiera drzwi #2 i zawsze zmienia

import random
door1 = " " 
door2 = " "
door3 = " "
count = 0


class door(object):
    pass

class nagroda(object):
    """ nagroda """
    PRIZE = ["koza","koza","ferrari"]
    
    def __init__(self, prize = ""):
        self.prize = prize
        
    def ustal(self):
        prize = random.choice(self.PRIZE)
        self.prize = prize
        self.PRIZE.remove(prize)
        return prize
        
    def __str__(self):
        nagroda = self.prize
        return nagroda
    
    def restart(self):
        self.PRIZE =["koza","koza","ferrari"]
        return self.PRIZE
    
door1 = nagroda()
door2 = nagroda()
door3 = nagroda()

drzwi = [door1,door2,door3]

#class gracz(object):
#    def __init__ (self,name,choice,stay = True):
#        self.name = name
#        self.choice = name
#        self.stay = stay
#    def __str__(self):
#        return (choice)
#    
#    def zmiana(self):
#        if self.stay:
#            return self.stay
        
        
def restart():
    nagroda.PRIZE =["koza","koza","ferrari"]
 
    

def ustal_drzwi():
    door1.ustal()
    door2.ustal()
    door3.ustal()

#asia = gracz("asia",1)
#print(asia)



def Alice():
    count = 0
    for i in range(100000):
        ustal_drzwi()
        if door1.prize == "ferrari":
            count += 1
        restart()
    count = count / 100000
    print(count)

def Bob():
    count = 0
    for i in range (100000):
        ustal_drzwi()
        if door1.prize != "ferrari":
            count += 1
        restart()
    count = count / 100000
    print(count)
        

Alice()
Bob()
