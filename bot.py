# Egroid (First Herman) by Wallvon

import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import find
import asyncio
import time
import os

Client = discord.Client ()
bot = commands.Bot(command_prefix='%')

@bot.command(pass_context=True)

@bot.event
async def on_ready():
    await bot.change_presence(game=discord.Game(name='%bothelp, %invite'))
    print ("I'm Ready, Fresh and Started!")
    print ("I am running on " + bot.user.name)
    print ("With the ID: " + bot.user.id)

@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say(":ping_pong: Pong!")
    print ("user has pinged")

@bot.command(pass_context=True)
async def clear(ctx, amount=100):
    channel = ctx.message.channel
    messages = []
    async for message in bot.logs_from(channel, limit=int(amount)):
        messages.append(message)
    await bot.delete_messages(messages)
    await bot.say("Messages Deleted.")

@bot.command(pass_context=True)
async def pong(ctx):
    await bot.say(":ping_pong: Ping!")
    print ("user has ponged")

@bot.command(pass_context=True)
async def drink(ctx):
    await bot.say("Here Ya Go! :tropical_drink:")
    print ("user has Drinked")

@bot.command(pass_context=True)
async def food(ctx):
    await bot.say("Here Is Ya Food! :cookie:")
    print ("user has Eaten")

@bot.command(pass_context=True)
async def hi(ctx):
    await bot.say("Hey! :wave:")

@bot.command(pass_context=True)
async def story(ctx):
    await bot.say("Title: The Little Girl Who Wasn't")
    await bot.say("I lived in a house from hell for four years, from age eleven to almost sixteen. There was constantly something happening. Doors flying open and shut, voices, footsteps. Nothing ever stayed where you put it. I was alone there a lot because both my parents worked and I was constantly terrified. One of the most gut-level disturbing things though was the little girl in my bathroom. Every time I walked past my bathroom door (which was constantly since it was right outside my bedroom) I saw a little girl with blond curled hair and a rose-colored dress. She just stood there, staring, looking like a photograph from 1905. I started keeping the door closed so I could walk by without seeing her, but she was always there when I opened it. Once I stepped in past her, I couldn't see her anymore but I could feel her there. She scared me, but I felt really sorry for her because she was trapped there, just like me, but probably forever. As the years went by and things in the house continued to get worse, she started seeming... darker. I started feeling like she wasn't really a little girl. I knew there was something ugly in the house and I felt like it was presenting this sympathetic image to me. Then I started thinking I was completely losing my mind.")
    await bot.say("One day, when I was 14, I had a friend from out of town come stay with me for a week. I hadn't told her anything whatsoever about the house because I didn't think she would come if I did. Right after she got there we were sitting in my room and she left to go to the bathroom. About a minute later she walked back in with a puzzled look on her face and said So, there's a little girl in your bathroom. Um, I, yeah she hangs out in there. Blond hair?" "Curls? Pink dress? Yeah. You know that's not really a little girl, don't you? I almost threw up. I was so relieved and terrified and excited and ready to run out of the house screaming. She wouldn't use my bathroom the rest of the week and I started using it as little as possible without pissing off my parents (who did not want to believe). Eventually we moved out and I could not have been happier. I distanced myself from it mentally as much as I could. Then, when I was 18, I took another friend on a road trip to pack up a few things I'd left in the house (my parents hadn't managed to sell it, and wouldn't for 5 more years). The minute we got on the property, my friend seemed uncomfortable. When we came around the bend in the long, steep driveway, he went completely white. I could tell something was wrong, but he insisted he was OK, so we got to work. After a while he asked to use the bathroom and I directed him to mine. Not 20 seconds after he left, he came running back in, gasping for breath, andand slammed the bedroom door behind him. He started babbling about a little blond girl who isn't really a little girl. All of a sudden he went dead still, looked me in the eye, and very solemnly said She's not happy. With you. You left, and you weren't supposed to. We threw whatever we could grab in two trips in my car (after I walked him to another bathroom and waited outside the door) and got the fuck out at top speed.")

@bot.command(pass_context=True)
async def kill(ctx):
    await bot.say("Egroid: You're gonna die! :gun:")
    await bot.say("You: AHHHHHHHHH!")
    await bot.say("Egroid Points the gun at you")
    await bot.say("Gun: *click*")
    await bot.say("Egroid: Wait, Why did nothing happen??")
    await bot.say("You: I'm gonna call the Police! :iphone:")
    await bot.say("Egroid: Where is my ammo?")
    await bot.say("You: Picks up phone and calls **911**")
    await bot.say("Police: Police how can i help you?")
    await bot.say("You: There is a man pointing a gun at me!!")
    await bot.say("Police: We are coming to your exact location!")
    await bot.say("Egroid: Ahhhh Here is my ammo!")
    await bot.say("Egroid hears the sirens from the Police car :police_car: :oncoming_police_car:")
    await bot.say("Gun: *Click* Egroid: Reloaded!")
    await bot.say("FBI: **FBI** DROP THE GUN NOW!")
    await bot.say("Gun: **Pow!**")
    await bot.say("*You fell dead* :gravestone:")
    await bot.say("FBI'S Gun: **Pow!**")
    await bot.say("Egroid fell dead :gravestone:")
    print ("The Kill command is used")

@bot.command(pass_context=True)
async def changelanguage(ctx):
    await bot.say(":flag_nl: :flag_us: You want to change the language? :flag_gb: :flag_jp:")
    await bot.say("I'm sorry to say that you can't do that in this version of the bot")
    await bot.say("Maybe in some next version but idk")

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I could find.", color=0x00ff00)
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Highest role", value=user.top_role)
    embed.add_field(name="Joined", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def meme(ctx, user: discord.Member):
    embed = discord.Embed(title="Here is a meme:", color=0x00ff00)
    embed.set_image(url=https://i.imgflip.com/2ckpnn.jpg)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def botinfo(ctx):
    embed = discord.Embed(title="Version", description="I'm now on version 1.46", color=0x00ff00)
    embed.set_footer(text="Made By Wallvon")
    embed.set_author(name="Egroid")
    embed.add_field(name="Why am i made", value="I am made to do some simple tasks and to be sort of funny.", inline=True)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def serverinfo(ctx):
    embed = discord.Embed(name="{}'s info".format(ctx.message.server.name), description="Here's what I could find.", color=0x00ff00)
    embed.set_author(name="Egroid")
    embed.add_field(name="Name", value=ctx.message.server.name, inline=True)
    embed.add_field(name="ID", value=ctx.message.server.id, inline=True)
    embed.add_field(name="Roles", value=len(ctx.message.server.roles), inline=True)
    embed.add_field(name="Members", value=len(ctx.message.server.members))
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def bothelp(ctx):
    embed = discord.Embed(title="Need help? Click on the link below to join our support server!", description="https://discord.gg/MKgxBU9", color=0x00ff00)
    embed.set_footer(text="Made By Wallvon")
    embed.set_author(name="Egroid")
    embed.add_field(name="Need more help?", value="Ask a Developer.", inline=True)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def invite(ctx):
    embed = discord.Embed(title="Want to invite Egroid? Click on the link below!", description="https://discordapp.com/oauth2/authorize?client_id=475685785040060437&permissions=2080898167&scope=bot", color=0x00ff00)
    embed.set_footer(text="Made By Wallvon")
    embed.set_author(name="Egroid")
    embed.add_field(name="Make Sure To Share Egroid With Friends.", value="Thanks For Using Egroid.", inline=True)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def murder(ctx, user: discord.Member):
    await bot.say("Egroid: You're gonna die! :gun:")
    await bot.say("A person murderd, {}. Ya Dead Now!".format(user.name))

@bot.command(pass_context=True)
@commands.has_role("Staff")
async def ban(ctx, user: discord.Member):
    await bot.say("Cya, {}. Ya never gonna be seen again! :b: :a: :regional_indicator_n: :regional_indicator_n: :regional_indicator_e: :regional_indicator_d:  :b: :a: :b: :regional_indicator_y: ".format(user.name))
    await bot.ban(user)

@bot.command(pass_context=True)
@commands.has_role("Staff")
async def kick(ctx, user: discord.Member):
    await bot.say(":boot: Cya, {}. Ya loser!".format(user.name))
    await bot.kick(user)

bot.run(os.getenv('TOKEN'))
