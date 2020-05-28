#  _________             .__        
# /   _____/____    ____ |__| ____  
# \_____  \\__  \  /    \|  |/ ___\ 
# /        \/ __ \|   |  \  \  \___ 
#/_______  (____  /___|  /__|\___  >
#        \/     \/     \/        \/
#   _____                          _________        .__            _____          __          
#  /     \   ____   _____   ____   \_   ___ \  ____ |__| ____     /  _  \  __ ___/  |_  ____  
# /  \ /  \_/ __ \ /     \_/ __ \  /    \  \/ /  _ \|  |/    \   /  /_\  \|  |  \   __\/  _ \ 
#/    Y    \  ___/|  Y Y  \  ___/  \     \___(  <_> )  |   |  \ /    |    \  |  /|  | (  <_> )
#\____|__  /\___  >__|_|  /\___  >  \______  /\____/|__|___|  / \____|__  /____/ |__|  \____/ 
#        \/     \/      \/     \/          \/               \/          \/                    

try:
    import shelve
    import os

    if os.path.isfile('config/config.dat') == True and os.path.getsize('config/config.dat') > 0:
        with shelve.open('config/config') as config:
            token = config['token']
            channel = config['channel']
            botid = config['botid']
            balhigh = config['balhigh']
            userid = config['userid']
    else:
        with shelve.open('config/config') as config:
            config['token'] = input('Please input your user token.\n')
            config['channel'] = input('Please input your designated channel.\n')
            config['botid'] = input('Please input the ID of the bot.\n')
            config['userid'] = input('Please input your ID.\n')
            config['balhigh'] = 0
            print('Please restart')
            exit()
except Exception as e:
    print(e)
    exit()

import discord
import asyncio
import random
import datetime
import time
from datetime import datetime

client = discord.Client()

# Creation of Global Variables #
bot = None
botchan = None

name = None
user = None

balance = 0

@client.event
async def on_message(message):
    global balance
    global balhigh
    global bot
    global botchan
    global user
    global name

    if message.author == bot:
        if message.channel == botchan:
            if str(name) and 'Prestige Level' in message.content:
                s = message.content
                
                balance = s.split('total balance is: ', 1)[1].split('total memes per minute', 1)[0]
                if ',' in balance:
                    balance = balance.replace(',', '')
                    balance = int(balance)
                    print(balance)

async def mine():
    await asyncio.sleep(12)
    global botchan
    try:
        while True:
            await botchan.send('!mine')
            await asyncio.sleep(61)
    except Exception as e:
        print(e)

async def startup():
    # Global Variables #
    global channel
    global botid
    global botchan
    global bot
    global userid
    global user
    global name
    
    # Saved Variables Conversion #
    channel = int(channel)
    botid = int(botid)
    userid = int(userid)
    
    # Startup Processes #
    await asyncio.sleep(10)
    botchan = client.get_channel(channel)
    bot = client.get_user(botid)
    user = client.get_user(userid)
    s = str(user)
    name = s.split('#', 1)[0]

async def buyprocess():
    await asyncio.sleep(12)
    global balance
    global bot
    global botchan
    try:
        while True:
            await botchan.send('!memes')
            await asyncio.sleep(3)
    except:
        return

client.loop.create_task(buyprocess())
client.loop.create_task(startup())
client.loop.create_task(mine())
# Login to Discord #
try:
    print("Logging in...\n")
    client.run(token, bot=False)
except Exception as e:
    print('Token is invalid, wiping config')
    os.remove('config.dat')
    os.remove('config.bak')
    os.remove('config.dir')
