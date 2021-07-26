#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 09:59:47 2021

@author: franek
"""

# bot.py
import nest_asyncio
nest_asyncio.apply()
import os

import discord
from dotenv import load_dotenv


load_dotenv("DISCORD_TOKEN.env")
TOKEN = os.getenv('DISCORD_TOKEN.env')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} dołączył/a do naszej drużyny')

print(os.getenv('DISCORD_TOKEN'))
client.run(TOKEN)
