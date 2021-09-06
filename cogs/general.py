import discord  # For Discord API
from discord.ext import commands
import os  # For OS related works

'''
1. Connecting to Discord Via GUILD
'''
# Variable name from .env file
GUILD = os.getenv('DISCORD_GUILD')
class General(commands.Cog):
    def __init__(self, client):
        self.client = client

    #When Bot becomes ready
    @commands.Cog.listener()
    async def on_ready(self):

    #Checking GUILD/Server name
        for guild in self.client.guilds:
            if guild.name == GUILD:
                break

        #Printing in console just to check everything is currect
        print(f'{self.client.user} is connected to the following Discord guild:\n'
            f'{guild.name}(id: {guild.id})\n')
    #Command for Pinging the bot for checking latency
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Ping > {round(self.client.latency * 1000)} ms')
    
    # Command to clear last n messages including the command given
    @commands.command()
    async def clear(self,ctx, num=5):
        await ctx.channel.purge(limit=num)
    
    # Command to kick any member of the server
    @commands.command()
    async def kick(self, ctx, member : discord.member, *, reason=None):
        await member.kick(reason=reason)

    # Message shown when in terminal when a member joins the server
    @commands.command()
    async def on_member_join(self, member : discord.member):
        print(f'{member} has joined the server')
    
    # Message shown when a member leaves server
    @commands.command()
    async def on_member_remove(self, member : discord.member):
        print(f'{member} has left the server')

    # Command to ban any member of the server
    @commands.command()
    async def ban(self, ctx, member : discord.member, *, reason=None):
        await member.ban(reason=reason)

    # Command to unban any member of the server
    @commands.command()
    async def unban(ctx, *, member):
        banned_members = await ctx.guild.bans()
        member_name, member_discriminator = member.split("#")

        for banned in banned_members:
            user = banned.user
            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f"Unbanned {user.mention}")
                return


# Setting up the General Cogs for connecting with CasperBot.py
def setup(client):
    client.add_cog(General(client))