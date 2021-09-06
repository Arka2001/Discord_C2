import discord  # For Discord API
from discord.ext import commands
import requests
import json

class Games(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    #Getting motivational quotes using api
    async def get_motivation():
        #Capturing request
        response = requests.get("https://zenquotes.io/api/random")
        #Storing json data
        json_data = json.loads(response.text)

        #Getting motivation
        motivate = json_data[0]['q'] + " -" + json_data[0]['a']
        return(motivate)

# Setting up the Games Cogs
def setup(client):
    client.add_cog(Games(client))