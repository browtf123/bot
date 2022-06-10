    ### HEADER ###
print('   ______                                   __            __     ____     ___')
print('  / ____/_____ ____ _ __  __ ____   ____   / /_   ____   / /_   / __ \   <  /')
print(' / /    / ___// __ `// / / // __ \ / __ \ / __ \ / __ \ / __/  / / / /   / / ')
print('/ /___ / /   / /_/ // /_/ // /_/ // / / // /_/ // /_/ // /_   / /_/ /_  / /  ')
print('\____//_/    \__,_/ \__, / \____//_/ /_//_.___/ \____/ \__/   \____/(_)/_/   ')
print('                   /____/                                                    ')
    ### DESCRIPTION ###
print('')
print('| Code by Crayonboi19                          | ')
print('| Project started on 06/10/2022                | ')
print('| A general purpose discord bot                | ')
print('| Title was made at patorjk.com/software/taag/ | ')
print('')

    ### IMPORT LIBRARIES ###
import discord
import os, json
from discord.utils import get
from dotenv import load_dotenv
import time

client = discord.Client()

    ### LAUNCHER ###
print('Launching...')
time.sleep(1.5)

@client.event
async def on_ready():
  print('{0.user} is now online.'.format(client))

    ### STATUS ###
discord.Activity(name="Chilling", type=3)

    ### BOT TOKEN ###
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client.run(TOKEN)
