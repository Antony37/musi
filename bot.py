# Egroid made with ❤️ by Wallvon

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

@bot.event
async def on_member_join(member):
    print("Recogniced that a member called " + member.name + " joined")
    await bot.send_message(member, "Welcome to the server! I hope you have a great time!")
    print("Sent message to " + member.name)


class Main_Commands():
    def __init__(self, bot):
     self.bot = bot

#ping

@bot.event
async def on_message(message):
    if message.content.startswith('gimmecookie'):
        await bot.say('Here is ya Cookie :cookie:')
    await bot.process_commands(message)

@bot.command(pass_context=True)
async def ping(ctx):
    """Pings the bot."""
    t = await bot.say('Pong!')
    ms = (t.timestamp-ctx.message.timestamp).total_seconds() * 1000
    await bot.edit_message(t, new_content='Pong! Took: {}ms'.format(int(ms)))

#ping

#clear

@bot.command(pass_context=True)
@commands.has_role("Staff")
async def clearmessage(ctx, amount=100):
    """Clears the amount of messages that you filled in -1."""
    channel = ctx.message.channel
    messages = []
    async for message in bot.logs_from(channel, limit=int(amount)):
        messages.append(message)
    await bot.delete_messages(messages)
    await bot.say("Messages Deleted.")

#clear

#drink

@bot.command(pass_context=True)
async def drink(ctx):
    """Gives you a virtual drink."""
    await bot.say("Here Ya Go! :tropical_drink:")
    print ("user has Drinked")

#drink

#food

@bot.command(pass_context=True)
async def food(ctx):
    """Gives you virtual food."""
    await bot.say("Here Is Ya Food! :cookie:")
    print ("user has Eaten")

#food

#hi

@bot.command(pass_context=True)
async def hi(ctx):
    """Says hi to the bot."""
    await bot.say("Hey! :wave:")

#hi

#info

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    """Gives info about the user. Usage: %info [Username]."""
    embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I could find.", color=0x00ff00)
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Highest role", value=user.top_role)
    embed.add_field(name="Joined", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.say(embed=embed)

#info

#message emoji reaction

@bot.event
async def on_reaction_add(reaction, user):
    channel = reaction.message.channel
    await bot.send_message(channel, '{} has added {} to the message: {}'.format(user.name, reaction.emoji, reaction.message.content))

@bot.event
async def on_reaction_remove(reaction, user):
    channel = reaction.message.channel
    await bot.send_message(channel, '{} has removed {} from the message: {}'.format(user.name, reaction.emoji, reaction.message.content))

@bot.command(pass_context=True)
async def clear(ctx, amount=100):
    channel = ctx.message.channel
    messages = []
    async for message in bot.logs_from(channel, limit=int(amount)):
        messages.append(message)
    await bot.delete_messages(messages)

#message emoji reaction

#botinfo

@bot.command(pass_context=True)
async def botinfo(ctx):
    """Gives info about the bot."""
    embed = discord.Embed(title="Version", description="I'm now on version 1.0", color=0x00ff00)
    embed.set_footer(text="Made with ❤️ by Lenaa")
    embed.set_author(name="Wave")
    embed.add_field(name="Prefix", value="%", inline=True)
    await bot.say(embed=embed)

#botinfo

#serverinfo

@bot.command(pass_context=True)
async def serverinfo(ctx):
    """Gives info about the server where the command was executed."""
    embed = discord.Embed(name="{}'s info".format(ctx.message.server.name), description="Here's what I could find.", color=0x00ff00)
    embed.set_author(name="Wave")
    embed.add_field(name="Name", value=ctx.message.server.name, inline=True)
    embed.add_field(name="ID", value=ctx.message.server.id, inline=True)
    embed.add_field(name="Roles", value=len(ctx.message.server.roles), inline=True)
    embed.add_field(name="Members", value=len(ctx.message.server.members))
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await bot.say(embed=embed)

#serverinfo

#support

@bot.command(pass_context=True)
async def support(ctx):
    """Gives you a link to the support server."""
    embed = discord.Embed(title="Need help? Click on the link below to join our support server!", description="https://discord.gg/DRhcT4P", color=0x00ff00)
    embed.set_footer(text="Made with ❤️ by Lenaa")
    embed.set_author(name="Wave")
    embed.add_field(name="Need more help?", value="Ask a Developer.", inline=True)
    await bot.say(embed=embed)

#support

#invite

@bot.command(pass_context=True)
async def invite(ctx):
    """Gives you a link to invite the bot."""
    embed = discord.Embed(title="Want to invite Wave? Click on the link below!", description="https://discordapp.com/oauth2/authorize?client_id=548784332291178496&scope=bot&permissions=8", color=0x00ff00)
    embed.set_footer(text="Made with ❤️ by Lenaa")
    embed.set_author(name="Wave")
    embed.add_field(name="Make Sure To Share Wave With Friends.", value="Thanks For Using Wave.", inline=True)
    await bot.say(embed=embed)

#invite

#murder

@bot.command(pass_context=True)
async def murder(ctx, user: discord.Member):
    """Murders someone. Usage: %murder [Username]."""
    await bot.say("Wave: You're gonna die! :gun:")
    await bot.say("A person murderd, {}. Ya Dead Now!".format(user.name))

#murder

#heal

@bot.command(pass_context=True)
async def heal(ctx, user: discord.Member):
    """Heals someone. Usage: %heal [Username]."""
    await bot.say("Wave: Here get a bandage")
    await bot.say("A person healed, {}. Ya Alive Now!".format(user.name))

#heal

#ban

@bot.command(pass_context=True)
@commands.has_role("Staff")
async def ban(ctx, user: discord.Member):
    """Bans someone (needs the role Staff). Usage: %ban [Username]."""
    await bot.say("Cya, {}. Ya never gonna be seen again! :b: :a: :regional_indicator_n: :regional_indicator_n: :regional_indicator_e: :regional_indicator_d:  :b: :a: :b: :regional_indicator_y: ".format(user.name))
    await bot.ban(user)

#ban

#kick

@bot.command(pass_context=True)
@commands.has_role("Staff")
async def kick(ctx, user: discord.Member):
    """Kicks someone (needs the role Staff). Usage: %kick [Username]."""
    await bot.say(":boot: Cya, {}. Ya loser!".format(user.name))
    await bot.kick(user)

#kick

#music

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('failed to load extention {}\n{}'.format(extension, exc))

#music

#servers

@bot.command(pass_context=True)
async def servers(ctx):
    """List of the Servers the Bot is on"""
    await bot.say("Bot runs on these Servers:\n")
    for s in bot.servers:
        await bot.say(f"```{s.name}```")

#server

#say

@bot.command(pass_context=True)
async def say(ctx, *, saymsg):
    """Say Command"""
    output = saymsg
    message = ctx.message
    await bot.delete_message(message)
    await bot.say(output)

bot.run('NTQ4Nzg0MzMyMjkxMTc4NDk2.D1KW2A.RSoFooLaN7Jfek3D0hrnmjrgjt0')
