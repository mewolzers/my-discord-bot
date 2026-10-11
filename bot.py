import os
import discord
from discord.ext import commands

# CHANGE THESE TWO LINES:
CHANNEL_ID = "1543509825755811884"  # Put your channel's ID inside the quotes
ALLOWED_WORD = "morms"             # Put your exact allowed word here

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name} and monitoring channel...")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if str(message.channel.id) == CHANNEL_ID:
        if message.content != ALLOWED_WORD:
            try:
                await message.delete()
            except discord.Forbidden:
                print("Error: The bot needs 'Manage Messages' permission.")

    await bot.process_commands(message)

# This reads your token safely from Render
bot.run(os.environ.get('DISCORD_TOKEN'))
