#!/usr/bin/python3

'''
import os
import discord

TOKEN='ODc3NDk3MjI2MDYxMDIxMjE0.YRze-Q.tj1MUweW9730cPiPPxgF1PaVIrI'

#Connection to Discord
client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_mssg(message):
  #Checking if the author of the mssg is CasperBOT
  if message.author == client.user:
    return

  if message.content.startswith('$hello'):
    await message.channel.send("Hey! I'm CasperBOT. I will try to give anything you want")

  await bot.process_commands(message)


#Running the CasperBOT: run(<BOT token>)
client.run(TOKEN)

'''

import os
import discord

from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()


@client.event
async def on_ready():
  for guild in client.guilds:
    if guild.name == GUILD:
      break


  print(f'{client.user} is connected to the following Discord guild:\n'
        f'{guild.name}(id: {guild.id})\n')


  members = '\n - '.join([member.name for member in guild.members])
  print(f'Guild Members:\n - {members}')


@client.event
async def on_message(message):
  if '$hello' in message.content.lower():
    await message.channel.send("Hey! I'm CasperBOT. I will try to give anything you want 😉")


client.run(TOKEN)
