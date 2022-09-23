import discord
from discord.ext import commands

client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print("Bot is online!")
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('With Mods'))

client.run('your token here')
