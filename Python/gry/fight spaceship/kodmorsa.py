#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 30 12:40:47 2021

@author: franek
"""
import time



słownik_znaków = {
                    "a":".-","b":"-...","c":"-.-.","d":"-..","e":".","f":"..-.","g":"--.","h":"....","i":"..","j":".---","k":"-.-","l":".-..","m":"--","n":"-.","o":"---","p":".--.","q":"--.-",
                  "r":".-.","s":"...","t":"-","u":"..-","w":".--","v":"...-","x":"-..-","z":"--..","y":"-.--"
                 }



def dot():
    print("\a")
    
def dash ():
    time.sleep(1)
    print("\a")
    




def main():
    word = input("Jakie słowo zamienić na morsa ? : ")
    znak = ""
    for i in word:
        if i ==" ":
            znak += i
        else :
            znak += słownik_znaków[i]
        
        
        
    print(znak)
    #for k in znak:
    #    if k == ".":
    #        dot()
    #    if k =="-":
    #        dash()


main()