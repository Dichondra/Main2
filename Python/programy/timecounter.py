#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 25 18:45:16 2021

@author: franek
"""

# program bierze dwie daty i wylicza ile czasu mija pomiędzy nimi (sekund,minut,godzin dni, miesięcy, lat)

import datetime, time

def powitanie():
    print("Ten program wylicza ile czasu minęło pomiędzy dwoma datami")

def zapytajdata():
    global day, month, year
    day = int(input("dzień miesiąca: "))
    month = int(input("miesiąc: "))
    year = int(input("Rok: "))
    return day, month, year


def main():
    day = 1
    month = 1
    year = 1
    powitanie()
    print("pierwsza data to ?")
    zapytajdata()
    firstdate = datetime.datetime(years = year, months = month, days = day)
    print(firstdate)
    
main()