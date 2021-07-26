#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 16:01:33 2021

@author: franek
"""

import discord, os,nest_asyncio,random, datetime, asyncio

def randnum(fname):
	lines=open(fname).read().splitlines()
	return random.choice(lines)


client = discord.Client()


@client.event
async def on_ready():
    print("we have logged in as {0.user}"
          .format(client))


    
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith("$hello"):
        await message.channel.send("Witaj człeku, co sprowadza cię na moje bagna?")
    
    if message.content.startswith("$recap"):
        f = open("recap.txt","r")
        await message.channel.send(f.read())
    if message.content.startswith("$fname"):
        x = randnum("names.txt")
        await message.channel.send(x)
    
    if message.author.id ==  343188073435365377:
        i = random.randint(1,5)
        if i == 1:
            await message.channel.send("Tęsknie za tobą, Amity")
        elif i == 2:
             await message.channel.send("Wychudłaś Amity, jedz więcej mięsa")
        elif i == 3:
                 await message.channel.send("Crocodile  screech")
        elif i == 4:
             await message.channel.send("Dobra robota, Ami")
        elif i == 5:
             await message.channel.send("Dobry człowiek")
    if message.content.startswith("$helo"):
        await message.channel.send("SyntaxError: unexpected EOF while parsing")
    if message.content.startswith("$pajac"):
        await message.channel.send("Spadaj")
    if message.content.startswith("$roll20"):
        
        await message.channel.send("Wylosowałam : 20")
    if message.content.startswith("$roll21"):
        
        await message.channel.send("Wylosowałam : 21")
    if message.content.startswith("$help"):
        await message.channel.send("""
                                   $hello
                                   $recap
                                   $pajac
                                   $roll20
                                   $roll21
                                   $fname
                                   $newrecap
                                   $newrecapshow
                                   $SetSession
                                   """)
    if message.content.startswith("$newrecap"):
        
        f = open("recap.txt","r+")
        f.truncate(0)
        f.write(message.content[9:])
        f.close
        z = open ("allrecap.txt","a")
        z.write("    ")
        z.write(message.content[9:])
    if message.content.startswith("$newrecapshow"):
        l = open("allrecap.txt","r")
        await message.channel.send(l.read())
    if message.content.startswith("$SetSession"):
        date = message.content[12:]
        date = datetime.strptime(date, '%d/%m/%y')
        now = datetime.datetime.now()
        await message.channel.send("Ustawiłam datę przypomnienia na :")
        await message.channel.send(date)
        await asyncio.sleep((date-now).total_seconds()+43200)
        await message.channel.send("Eh miałam przypomnieć o sesji. Dziś będzie sesja")
    if "zrób" in message.content:
        await message.channel.send("Nie.")
client.run("ODY3MzEwNDUxODE2Mzk4ODU4.YPfPzQ.cZWVDhT9-1vFGUsGasTf_40w_dQ")