#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:28:19 2021

@author: franek
"""
# cjvtsybxdatgcdhc
import urllib.request, smtplib
#page = urllib.request.urlopen("https://www.theowlclub.net/").read()
from urllib.request import Request, urlopen

encode = "utf-8"


new_episodes = ["Season 5 Episode 17","Season 5 Episode 18","Season 5 Episode 19","Season 5 Episode 20","Season 5 Episode 21"]


x = """    
if found == True:
    conn = smtplib.SMTP('smtp.gmail.com', 587) # smtp address and port
    conn.ehlo() # call this to start the connection
    conn.starttls() # starts tls encryption. When we send our password it will be encrypted.
    conn.login('pythonorszulak@gmail.com', 'cjvtsybxdatgcdhc')
    conn.sendmail('pythonorszulak@gmail.com', "franekorszulak@gmail.com", 'Subject: Owl house episode!\n\nAttention!\n\nYour favourite show is available today!\n\n')
    conn.quit()
    
else:
    print("Did not found episode")
"""  

def Main():
   
    page = urllib.request.urlopen("https://www.thewatchcartoononline.tv/anime/boku-no-hero-academia-english-subbed").read()
    
    encode = "utf-8"
    

    page_string = str(page, encode)
    
    found = False
    for episode in new_episodes:
        if episode in page_string:
            found = True
            new_episodes.remove(episode)
    if found == True:
        print("hello")
        conn = smtplib.SMTP('smtp.gmail.com', 587) # smtp address and port
        conn.ehlo() # call this to start the connection
        conn.starttls() # starts tls encryption. When we send our password it will be encrypted.
        conn.login('pythonorszulak@gmail.com', 'cjvtsybxdatgcdhc')
        conn.sendmail('pythonorszulak@gmail.com', "franekorszulak@gmail.com", 'Subject: Boku no hero academia episode!\n\nAttention!\n\nYour favourite show is available today!\n\n')
        conn.sendmail('pythonorszulak@gmail.com', "asia.widla@gmail.com", 'Subject: Boku no hero academia episode!\n\nAttention!\n\nYour favourite show is available today!\n\n')

        conn.quit()
    else:
        print("hello",found, new_episodes)
    
Main()