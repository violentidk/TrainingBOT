import discord
from discord import app_commands
from discord.ext import commands

intents = discord.Intents.default()
client = commands.Bot(command_prefix='/', intents=intents)

tree = app_commands.CommandTree(client)

@tree.command(name="event1", description="Starts event 1")
async def event1(interaction: discord.Interaction):
    user = interaction.user.mention
    await interaction.response.send_message(f"📢 Event 1 started! Hosted by {user}.")

@tree.command(name="event2", description="Starts event 2")
async def event2(interaction: discord.Interaction):
    user = interaction.user.mention
    await interaction.response.send_message(f"🎉 Event 2 started! Hosted by {user}.")

@client.event
async def on_ready():
    await tree.sync()
    print(f"We have logged in as {client.user}")

client.run('MTI2NTMxOTM1NzIzNjM4Mzc3NA.GYjv9_.VhQqT0jUn92ApFQnTECubIh3-aaXkmDX5lVx04')
