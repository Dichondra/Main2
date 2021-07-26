#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 18:38:53 2021

@author: franek
"""

### Program dogry w adventure time
###
x = """
Zmiany które zrobiłem, dałem w innit playera zmienną bot i zmieniłem wszędzie bot na self. bot zamiast po prostu mieć zmienną bot == false


"""

### imports
import random


class Player():
    global END
    
    END = True
    
    
    
    
    def __init__(self,NAME, bot = False):
        self.name = NAME
        self.hand = []
        self.immune = False
        self.END = True
        self.name = input("Jak się nazywasz: ")
        self.bot = bot
    def play(self,Gracz,Przeciwnik,Talia, bot = False):
        global END
        if self.bot == False:
            print("Dostępne karty (człowiekowi) to : ",self.hand)
        if self.bot == False:
            self.choice = int(input("Którą kartę wybierasz?:"))
       
        if self.bot == True:
            if self.hand[0] != 8:
                self.choice = self.hand[0]
            else:
                self.choice = self.hand[1]
            if (5 and 7) in self.hand or (6 and 7)in self.hand:
                self.choice = 7
        self.hand.remove(self.choice)
        if self.hand != []:
            if self.choice == 1:
                if self.bot == False and Przeciwnik.immune == False or self.bot and Gracz.immune == False:
                    if self.bot == False:
                        strzał = int(input("Podaj numer jaki myślisz że ma przeciwnik: "))
                    if self.bot:
                        strzał = random.randint(2,8)
                        print("Strzelam w numer ",strzał)
                    if strzał == Przeciwnik.hand[0]:
                        print("Trafiłeś i wygrałeś")
                        END = False
                    if strzał != Przeciwnik.hand[0]:
                        print("Pudło")
            elif self.choice == 2:
                if self.bot == False and Przeciwnik.immune == False:
                    print("Karta przeciwnika to :",Przeciwnik.hand)
                else:
                    pass
            elif self.choice == 3:
                if self.bot == False and Przeciwnik.immune == False or self.bot and Gracz.immune == False:
                    print ("ręka człowieka to ",Gracz.hand[0],"Ręka bota to :",Przeciwnik.hand[0])
                    if Gracz.hand[0] > Przeciwnik.hand[0]:
                        print("Wygrał gracz, imię wygranego to :",Gracz.name)
                        END = False
                    if Gracz.hand[0] < Przeciwnik.hand[0]:
                        print("Wygrał bot, imię wygranego to :",Przeciwnik.name)
                        END = False

                    if Gracz.hand[0] == Przeciwnik.hand[0]:
                        print("remis, macie te same karty")
                        END = False
                else:
                    pass

            elif self.choice == 4:
                
                self.immune = True
            
            elif self.choice == 5:
                if self.bot == False and Przeciwnik.immune == False or self.bot and Gracz.immune == False:
                    if self.bot == True:
                        wybór = random.randint(1,2)
                        if wybór == 1:
                            print("Wybieram siebie")
                        else:
                            print("Wybieram byś ty odrzucił kartę")
                    else:
                        wybór = int(input("Wybierz czy zagrać na siebie czy na gracza (1- na siebie / 2- na przeciwnika)"))
                    if wybór == 1:
                        if self.hand[0] == 8:
                            print("Odrzucono 8, przegrano")
                            END = False
                    
                    
                        self.hand.remove(self.hand[0])
                       
                        if self.bot == False:
                           Talia.give_card(Talia.deck, Gracz)
                        else:
                           Talia.give_card(Talia.deck,Przeciwnik)
                    else:
                        if self.bot == False:
                            if Przeciwnik.hand[0] == 8:
                                print("Przeciwnik miał księżniczkę i przegrywa")
                                END = False
                            else:
                                Przeciwnik.hand = []
                          
                                Talia.give_card(Talia,Przeciwnik)
                        else:
                            if Gracz.hand[0] == 8:
                                print("Gracz miał księżniczkę i przegrywa")
                                END = False
                            else:  
                                Gracz.hand = []
                                Talia.give_card(Talia,Gracz)
            elif self.choice == 6:
                if self.bot == False and Przeciwnik.immune == False or self.bot and Gracz.immune == False:
                    copy = Przeciwnik.hand
                    Przeciwnik.hand = self.hand
                    self.hand = copy
                
                
            elif self.choice == 7:
                pass
            elif self.choice == 8:
                print("Przegrałeś, czemu ją grasz?")
                END = False

            
        
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
    
    def give_card(self,deck, gracz ):
        if self.deck:
            karta = self.deck.pop(0)
            
            gracz.hand.append(karta)
        else:
            pass
        
        
        
def Main():
    print("Witaj w adventure Time grze napisanej przeze mnie ")
    Gracz = Player("Gracz")
    Przeciwnik = Player("Przeciwnik", bot = True)
    Talia = Deck()
    Talia.shuffle()
    for i in range(2):
        Talia.give_card(Talia.deck, Gracz)
    Talia.give_card(Talia.deck, Przeciwnik)
    while END:
        Gracz.immune = False
        if (5 and 7) in Gracz.hand or (6 and 7) in Gracz.hand:
            print("Którą kartę wybierasz?:[7]")
            Gracz.hand.remove(7)
        else:    
            Gracz.play(Gracz,Przeciwnik,Talia)
        Talia.give_card(Talia.deck,Przeciwnik)
        Przeciwnik.immune = False
        if END:
            if Przeciwnik.hand[0] != 8:
                print("Ja bot gram kartę: " ,Przeciwnik.hand[0])
            else:
               print("Ja bot gram kartę: " ,Przeciwnik.hand[1])
        if END:
            if (5 and 7) in Gracz.hand or (6 and 7) in Gracz.hand:
                print("ja bot gram kartę:[7]")
                Gracz.hand.remove(7)
            else:
                Przeciwnik.play(Gracz,Przeciwnik, Talia, bot = True)
        Talia.give_card(Talia.deck, Gracz)
    
Main()