import discord
import random
from discord.ext import commands

intents = discord.Intents.all()
client = discord.Client(intents=intents)
client = commands.Bot(command_prefix='>', intents=discord.Intents.all())
client.remove_command("help")

@client.event
async def on_ready():
    print("Bot is online and ready to use!")
    await client.change_presence(status=discord.Status.dnd, activity=discord.Game('Subscribe'))

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason="Not specified"):
    if member == ctx.author:
        await ctx.send("You cannot kick yourself.")
    else:
        em = discord.Embed(title="**KICKED**", description=f"**{member.mention}** was kicked for {reason}")
        await ctx.send(embed=em)
        await ctx.guild.kick(discord.Object(id = member.id))

@client.command()
@commands.has_permissions(kick_members=True)
async def ban(ctx, member : discord.Member, *, reason="Not specified"):
    if member == ctx.author:
        await ctx.send("You cannot ban yourself.")
    else:
        em = discord.Embed(title="**BANNED**", description=f"**{member.mention}** was banned for {reason}")
        await ctx.send(embed=em)
        await ctx.guild.ban(discord.Object(id = member.id))

client.run('your token here')
