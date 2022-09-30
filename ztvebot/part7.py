import discord
from discord.ext import commands
from discord import app_commands

client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
  print('Bot is online')
  try:
      synced = await client.tree.sync()
      print(f'synced {len(synced)} command')
  except Exception as e:
    print(e)

@client.tree.command(name="ping")
async def ping(interaction: discord.Interaction):
  await interaction.response.send_message(f"yo")

client.run('your token here')
