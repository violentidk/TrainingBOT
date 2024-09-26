import os
import discord
from discord import app_commands
from discord.ext import commands

intents = discord.Intents.default()
client = commands.Bot(command_prefix='/', intents=intents)

@client.tree.command(name="event1", description="Starts event 1")
async def event1(interaction: discord.Interaction):
    user = interaction.user.mention
    await interaction.response.send_message(f"📢 Event 1 started! Hosted by {user}.")

@client.tree.command(name="event2", description="Starts event 2")
async def event2(interaction: discord.Interaction):
    user = interaction.user.mention
    await interaction.response.send_message(f"🎉 Event 2 started! Hosted by {user}.")

@client.event
async def on_ready():
    await client.tree.sync()
    print(f"We have logged in as {client.user}")

# Fetch the token from environment variable
token = os.getenv('MTI2NTMxOTM1NzIzNjM4Mzc3NA.GYjv9_.VhQqT0jUn92ApFQnTECubIh3-aaXkmDX5lVx04')

# Raise error if the token is not set
if not token:
    raise ValueError("No Discord bot token found in environment variables!")

client.run(token)
