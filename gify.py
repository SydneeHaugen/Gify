import discord


import asyncio
import requests
import os
import json
import random
import time
import datetime
import math


from discord.ext import commands
from dotenv import load_dotenv

#this is access able on the .env (on computer running jarvis program)
load_dotenv()

token = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')



# bot info runs on start
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.event
async def on_message(message):

    #jarvis says a random quotes if you speak its name (lowercase only)
    if 'jarvis' in message.content.lower():

        with open('quotes.json', 'r') as quotes:
            jarvisQuotes = json.load(quotes)

        await message.channel.send(random.choice(jarvisQuotes))

    # gifs outputed depending on prompt word 
    elif 'noice' in message.content.lower() and not message.author.bot:
        noiceGIF = 'https://tenor.com/view/brooklyn99-noice-jake-peralta-andy-samberg-nice-gif-14234819'
        await message.channel.send(noiceGIF)

    elif 'what' in message.content.lower() and not message.author.bot:
        whaaatGIF = 'https://gph.is/g/a9Y71PB'
        await message.channel.send(whaaatGIF)

    await bot.process_commands(message)


# simple example that prints out hello
@bot.command(name='hello', help='Jarvis says hello.')
async def hello(context):

    msg = 'Hello ' + context.author.mention

    await context.send(msg)




#runs bot
bot.run(token)