
import json
import os
from dotenv import load_dotenv

import discord
from discord import channel
from discord.ext import commands, tasks

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

dir_path = os.path.dirname(os.path.realpath(__file__))

bot = commands.Bot(command_prefix='~', case_insensitive=True)
print('Running...')

@bot.event
async def on_ready():
    print('Bot is ready.')
    await bot.change_presence(activity=discord.Game(name='MapleRoyals'))

@bot.command(name = 'whatdrops', help = 'Displays what monster drops a certain item')
async def whatdrops(ctx, *args):
    f = open(dir_path+"/mobs.json","r", encoding = "utf-8")
    data = json.load(f)
    f.close()
    msg = ""
    item = ""
    for arg in args:
        item = item + arg + ' '
    item = item[:-1].lower()

    for detail in data:
        drops = detail["drops"]
        for drop in drops:
            if item == drop['name'].lower():
                msg = msg + detail["name"] + ", "
    if msg == '':
        await ctx.send(f'Nothing drops {item}')
    else:
        msg = msg[:-2]
        await ctx.send(msg)

bot.run(TOKEN)