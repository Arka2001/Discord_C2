#!/usr/bin/python3

import os         # For OS related works
import discord    # For discord api
import requests   # For doing http request and get data from the api: "https://apisecurity.io/"
import json       # For handling JSON data returned by api
import random     # For making data random

from dotenv import load_dotenv      # Take environment variable from .env file
from discord.ext import commands    # Extended featured version of discord.Client
import logging                      # Logging module to log events


#########################################################################################

'''
1. Accessing env. var. from .env file
2. Connecting to discord server via TOKEN and GUILD name
3. Command regitration
4. Removing default help command to make our very own
5. Creating custom functions
6. Creating events
'''

#Search for variables by the given name in the host environment
load_dotenv()

#Variable name from .env file
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

#Registering a command
client = commands.Bot(command_prefix = '$')

#Removing default help command to create our own
client.remove_command('help')


#Getting motivational quotes using api
def get_motivation():
    #Capturing request
    response = requests.get("https://zenquotes.io/api/random")
    #Storing json data
    json_data = json.loads(response.text)

    #Getting motivation
    motivate = json_data[0]['q'] + " -" + json_data[0]['a']
    return(motivate)

#When Bot becomes ready
@client.event
async def on_ready():

    #Checking GUILD/Server name
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    #Printing in console just to check everything is currect
    print(f'{client.user} is connected to the following Discord guild:\n'
          f'{guild.name}(id: {guild.id})\n')


##########################################################################################

'''
All Discord Commands
'''

#1. help cmd
@client.command()
async def help(ctx):
    await ctx.send('''

1. **$help**     -> _To list available commands_
2. **$hello**    -> _For building a rapport with me,_ the ***CasperBot***
3. **$motivate** -> _Motivate members via random quotes_
4. **$ping**     -> _Checks latency_
''')

#2. hello cmd
@client.command()
async def hello(ctx):
    await ctx.send("Hey! I'm CasperBot.\nType: **$help** to see my _serving menu_")

#3. motivate cmd
@client.command()
async def motivate(ctx):
    motivate = get_motivation()
    await ctx.send(motivate)

#4. ping cmd
@client.command()
async def ping(ctx):
    await ctx.send(f'**latency**: _{round(client.latency * 1000)}ms_')


#logging

client.run(TOKEN)
