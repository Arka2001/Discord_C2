from chunk import Chunk
import subprocess
import discord
from discord.ext import commands
import os

# System cmd
def SystemCmd(cmd):
    proc=subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)

    result = proc.stdout.read() + proc.stderr.read()    # stdout and stderr
    result = result.decode('utf-8')                     # decoding result to utf-8
    return result

class CommandLine(commands.Cog):
    def __init__(self, client):
        self.client = client

    '''
    All Discord Command related stuffs
    '''

    #1. help cmd
    @commands.command()
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
    @commands.command()
    async def hello(self,ctx):
        await ctx.send("Hey! I'm CasperBot.\nType: **$help** to see my _serving menu_")
    
    #5.1. OS cmd 
    # Sending data chunk by chunk
    def chunks(self,lst, n):
        for i in range(0, len(lst), n):
            yield lst[i:i+n]

    #5.2. OS cmd
    

    #5. OS cmd
    @commands.command()
    async def os(self, ctx, *args):
        no_of_args = len(args)
        cmd=' '.join(args)      # Converting to string
        
        result = SystemCmd(cmd)

        await ctx.send('***OUTPUT***')
        for chunk in Chunk(result, 2000):
            await ctx.send(chunk)

    #6. OS bind/rev shell cmd

def setup(client):
    client.add_cog(CommandLine(client))
