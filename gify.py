import discord
import asyncio
import os

from discord.ext import commands
from dotenv import load_dotenv

#this is access able on the .env (on computer running gify program)
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

# Post wink gif.
@bot.command(name='wink', help='Schitts Creek (Alexis Wink).')
async def wink(context):

    winkGIF = 'https://tenor.com/view/schitts-creek-alexis-wink-flirting-gif-11803901'
    await context.channel.send(winkGIF)

# Post don't be a little B! gif.
@bot.command(name='b', help='Schitts Creek (Davild dont be a little B!).')
async def b(context):

    bGIF = 'https://tenor.com/view/dontbeab-bitch-dont-schitt-gif-5532877'
    await context.channel.send(bGIF)


# Post Indeed gif.
@bot.command(name='indeed', help='Birdgerton (simom indeed).')
async def indeed(context):

    indeedGIF = 'https://tenor.com/view/bridgerton-rege-jean-page-simon-basset-duke-of-hastings-period-drama-gif-19734062'
    await context.channel.send(indeedGIF)

# Post Is that so? gif.
@bot.command(name='ITS', help='Birdgerton (simom Is that so?).')
async def its(context):

    itsGIF = 'https://tenor.com/view/bridgerton-rege-jean-page-simon-basset-duke-of-hastings-period-drama-gif-19733860'
    await context.channel.send(itsGIF)

# Post unlikely gif.
@bot.command(name='unlikely', help='Schitts Creek (Davild unlikely).')
async def unlikely(context):

    unlikelyGIF = 'https://tenor.com/view/schitts-creek-david-rose-unlikely-probably-not-yeah-no-gif-19728909'
    await context.channel.send(unlikelyGIF)


# Post You got a Problem? gif.
@bot.command(name='u', help='SNL (simom You got a Problem?).')
async def u(context):

    uGIF = 'https://tenor.com/view/you-got-a-problem-rege-jean-page-saturday-night-live-excuse-me-whats-wrong-gif-20503002'
    await context.channel.send(uGIF)

#runs bot
bot.run(token)