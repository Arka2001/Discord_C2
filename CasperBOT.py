#!/usr/bin/python3

import os         # For OS related works
import discord    # For discord api
import requests   # For doing http request and get data from the api: "https://apisecurity.io/"
import json       # For handling JSON data returned by api

from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

#Getting infosec news
def get_news():
  #Capturing request
  response = requests.get("https://zenquotes.io/api/random")
  #Storing json data
  json_data = json.loads(response.text)

  news = json_data[0]['q'] + " -" + json_data[0]['a']
  return(news)


@client.event
async def on_ready():

  #Checking GUILD/Server name
  for guild in client.guilds:
    if guild.name == GUILD:
      break

  #Printing in console just to check everything is currect
  print(f'{client.user} is connected to the following Discord guild:\n'
        f'{guild.name}(id: {guild.id})\n')


  #Needs correction: This should print all the members 
  #members = '\n - '.join([member.name for member in guild.members])
  #print(f'Guild Members:\n - {members}')


@client.event
async def on_message(message):
  
  #if '$help' in message.content.lower():
  #  await message.channel.send("1. $hello - for building a rapport with CasperBOT")

  #if '$hello' in message.content.lower():
  #  await message.channel.send("Hey! I'm CasperBOT. I will try to give anything you want 😉")

  if '$news' in message.content.lower():
    news = get_news()
    await message.channel.send(news)
  
  #else:
  # await message.channel.send("Sorry 😔, I'm not configured to reply anything against this command")

client.run(TOKEN)
