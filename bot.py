import discord
from discord.ext import commands
import asyncio

bot = commands.Bot(command_prefix='/')

@bot.event
async def onready():
    print('The Bot Is Ready!')
    print(bot.user.name)
    print(bot.user.id)

@bot.command()
async def sword():
    await bot.say('DIE!')

@bot.command()
async def nub():
    await bot.say('u are nub -_-')

@bot.command()
async def list():
    await bot.say('All -Commands-')
    await bot.say('/sword')
    await bot.say('Kills You')
    await bot.say('/nub')
    await bot.say('Says Noob')
    await bot.say('/creeper')
    await bot.say('Sends Link Of A Creeper Pitcure')
    await bot.say('/diaset')
    await bot.say('Gives You Diamond Armor')
    await bot.say('/creator')
    await bot.say('Tells More About Creator')
    await bot.say('/gtfo')
    await bot.say('Says Something Special')

@bot.command()
async def creeper():    
    await bot.say('https://goo.gl/images/phsPwJ%27')

@bot.command()
async def diaset():
    await bot.say('You Weared Diamond Armor!')

@bot.command()
async def creator():
    await bot.say('My Creators Name Is ProTalha You Can Join His Server From Here https://discord.gg/YQQUD35%27)

@bot.command()
async def gtfo():
    await bot.say('GET THE F#$@ OUT OF MY ROOM IM PLAYING MINECRAFT')

bot.run('NTQwOTI3NzI4NDkzMjY0OTA4.DzYDTw.FS-L2OA_4iFnKs_JbBWpS-WwPzE')
