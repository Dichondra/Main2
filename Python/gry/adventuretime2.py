#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 15:25:48 2021

@author: franek
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 18:38:53 2021

@author: franek
"""

### Program dogry w adventure time


### imports
import random




class Player():
    def __init__(self):
        self.hand = []
        self.name = input("Jak się nazywasz: ")
    def play(self,Przeciwnik,Talia):
        print("Dostępne karty to : ",self.hand)
        self.choice = int(input("Którą kartę wybierasz?:"))
        self.hand.remove(self.choice)
        if self.hand != []:
            if self.choice == 1:
                strzał = int(input("Podaj numer jaki myślisz że ma przeciwnik"))
                if strzał == Przeciwnik.hand[0]:
                    print("Trafiłeś i wygrałeś")
                if strzał != Przeciwnik.hand[0]:
                    print("Pudło")
            elif self.choice == 2:
                print("Karta przeciwnika to :",Przeciwnik.hand)
            elif self.choice == 3:
                
                
                
                
                if self.hand[0] > Przeciwnik.hand[0]:
                    print("Wygrałeś, przeciwnik miał mniejszą karte równą :",Przeciwnik.hand)
                if self.hand[0] < Przeciwnik.hand[0]:
                    print("Przegrałeś, przeciwnik miał większą kartę równą :",Przeciwnik.hand)
                if self.hand[0] == Przeciwnik.hand[0]:
                    print("remis, macie te same karty, jego to też",Przeciwnik.hand)
            elif self.choice == 4:
                pass
            elif self.choice == 5:
                wybór = int(input("Wybierz czy zagrać na siebie czy na gracza (1- na siebie / 2- na przeciwnika)"))
                if wybór == 1:
                    self.hand.remove(self.hand[0])
                    Talia.give_card(Talia.deck, Gracz)
                else:
                    pass
            elif self.choice == 6:
                copy = Przeciwnik.hand
                Przeciwnik.hand = self.hand
                self.hand = copy
                
                
            elif self.choice == 7:
                pass
            elif self.choice == 8:
                print("Przegrałeś, czemu ją grasz?")
            
        
        else:
            print("try again, wrong card not in hand")
        
    def __str__(self,name):
        return self.name
    
    
class Deck():
   ## deck = ["1","1","1","1","1","2","2","3","3","4","4","5","5","6","7","8"]
    
    def __init__(self):
        self.deck = [1,1,1,1,1, 2,2, 3,3, 4,4, 5,5, 6, 7, 8]
        
    
    def shuffle(self):
        random.shuffle(self.deck)
    
    def give_card(self,deck, gracz, N ):
        if self.deck:
            for i in range(N):
                karta = self.deck.pop(0)
                gracz.hand.append(karta)
        else:
            pass
        
        
        
def Main():
    print("Witaj w adventure Time grze napisanej przeze mnie ")
    Gracz = Player()
    Przeciwnik = Player()
    Talia = Deck()
    Talia.shuffle()
    for i in range(2):
        Talia.give_card(Talia.deck, Gracz)
    Talia.give_card(Talia.deck, Przeciwnik)
    print(Przeciwnik.hand)
    while Talia.deck:
        Gracz.play(Przeciwnik,Talia)
    
Main()