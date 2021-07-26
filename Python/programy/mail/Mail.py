#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 23 10:09:57 2021

@author: franek
"""


import smtplib
conn = smtplib.SMTP('smtp.gmail.com', 587)

conn.ehlo()
conn.starttls()
conn.login('spamorshluck@gmail.com', 'qjjcjfszugrnykqf')
conn.sendmail('spamorshluck@gmail.com','spamorshluck@gnp.pl',"Subject: Mail napisany przez pythona\n\nWitaj, ten mail zostal napisany w programie python, przez Franciszka Orszulaka")
 
conn.quit()