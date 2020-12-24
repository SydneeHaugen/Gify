import discord
import asyncio
import os

from discord.ext import commands
from dotenv import load_dotenv

#this is access able on the .env (on computer running jarvis program)
load_dotenv()

token = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='#')

# bot info runs on start
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.event
async def on_message(message):

    #Gify says a random quotes if you speak its name (lowercase only)
    if 'gify' in message.content.lower():

        await message.channel.send("Hi :)")


    await bot.process_commands(message)


# Post Noice gif.
@bot.command(name='noice', help='Brooklyn 99 Noice.')
async def noice(context):

    noiceGIF = 'https://tenor.com/view/brooklyn99-noice-jake-peralta-andy-samberg-nice-gif-14234819'
    await context.channel.send(noiceGIF)

# Post boop gif.
@bot.command(name='boop', help='Schitts Creek (Alexis boop).')
async def boop(context):

    boopGIF = 'https://tenor.com/view/boop-alexis-rose-gif-18002318'
    await context.channel.send(boopGIF)

# Post F@uk u gif.
@bot.command(name='fu', help='F@uk u.')
async def fu(context):

    fuGIF = 'https://tenor.com/view/fuck-you-gif-4335985'
    await context.channel.send(fuGIF)


#runs bot
bot.run(token)