import discord


import asyncio
import requests
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

    #jarvis says a random quotes if you speak its name (lowercase only)
    if 'gify' in message.content.lower():

        await message.channel.send("Hi :)")


    await bot.process_commands(message)


# simple example that prints out hello
@bot.command(name='hello', help='Jarvis says hello.')
async def hello(context):

    msg = 'Hello ' + context.author.mention

    await context.send(msg)

# simple example that prints out hello
@bot.command(name='noice', help='Jarvis says hello.')
async def noice(context):

    noiceGIF = 'https://tenor.com/view/brooklyn99-noice-jake-peralta-andy-samberg-nice-gif-14234819'
    await message.channel.send(noiceGIF)




#runs bot
bot.run(token)