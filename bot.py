# Wave made with ❤️ by Lenaa

import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import find
from discord.voice_client import VoiceClient
import asyncio
import time
import os
from discord import opus
OPUS_LIBS = ['libopus-0.x86.dll', 'libopus-0.x64.dll',
             'libopus-0.dll', 'libopus.so.0', 'libopus.0.dylib']


def load_opus_lib(opus_libs=OPUS_LIBS):
    if opus.is_loaded():
        return True

    for opus_lib in opus_libs:
            try:
                opus.load_opus(opus_lib)
                return
            except OSError:
                pass

    raise RuntimeError('Could not load an opus lib. Tried %s' %
                       (', '.join(opus_libs)))


opts = {
    'default_search': 'auto',
    'quiet': True,
}  # youtube_dl options


load_opus_lib()

startup_extensions = ["Music"]

Client = discord.Client ()
bot = commands.Bot(command_prefix=commands.when_mentioned_or('%'))

@bot.command(pass_context=True)

@bot.event
async def on_ready():
    await bot.change_presence(game=discord.Game(name='%help | %invite'))
    print ("I'm Ready, Fresh and Started!")
    print ("I am running on " + bot.user.name)
    print ("With the ID: " + bot.user.id)

class Main_Commands():
    def __init__(self, bot):
     self.bot = bot

#music

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('failed to load extention {}\n{}'.format(extension, exc))

#music

bot.run('token')