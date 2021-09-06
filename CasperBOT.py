#!/usr/bin/python3

import discord      # For discord api
import requests     # For doing http request and get data from the api: "https://apisecurity.io/"
import json         # For handling JSON data returned by api
import random       # For making data random
import os           # For OS related works
import subprocess   # Allows us to execute os cmds in an easier and controllable manner


from dotenv import load_dotenv      # Take environment variable from .env file
from discord.ext import commands    # Extended featured version of discord.Client
import logging                      # Logging module to log events


#########################################################################################

'''
1. Accessing env. var. from .env file
2. Connecting to discord server via TOKEN and GUILD name
3. Command regitration
4. Removing default help command to make our very own
5. Logging
6. Creating custom functions
7. Creating events
'''

#Search for variables by the given name in the host environment
load_dotenv()

#Variable name from .env file
TOKEN = os.getenv('DISCORD_TOKEN')


#Registering a command
bot = commands.Bot(command_prefix = '$')

#Removing default help command to create our own
bot.remove_command('help')

'''
#Logging commands
logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='a')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

class logthis :
    def __init__(self):
        logging.basicConfig(level=logging.DEBUG,filename="socio-terminal.log",format="%(asctime)s [%(levelname)s] - [%(filename)s > %(funcName)s() > %(lineno)s] - %(message)s",datefmt="%H:%M:%S")
    def debug(self,msg):
        logging.debug(msg)
    def info(self,msg):
           logging.info(msg)
    def warning(self,msg):
           logging.warning(msg)
    def error(self,msg):
           logging.error(msg)
    def critical(self,msg):
           logging.critical(msg)
'''





#logging

# Loading and Unloading commands for the Cogs
@bot.command()
async def load(ctx,extension):
    bot.load_extension(f'cogs.{extension}')

@bot.command()
async def unload(ctx,extension):
    bot.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')


bot.run(TOKEN)
