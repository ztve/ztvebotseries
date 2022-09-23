import discord
from discord.ext import commands

intents = discord.Intents.all()
client = discord.Client(intents=intents)
client = commands.Bot(command_prefix='>', intents=discord.Intents.all())
client.remove_command("help")

@client.event
async def on_ready():
    print("Bots Is Online!")
    await client.change_presence(status=discord.Status.dnd, activity=discord.Game('you'))

@client.group(invoke_without_commands=True)
async def help(ctx):
    em = discord.Embed(title = "Help Commands!", description="These are the commands.")
    
    em.add_field(name = "Moderation", value = "kick,ban,warn")
    em.add_field(name = "Fun", value = "ping,8ball")

    await ctx.send(embed=em)
client.run('your token here')
