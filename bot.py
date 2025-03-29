
import discord
from discord.ext import commands

# Enable bot intents (required for message events)
intents = discord.Intents.default()
intents.message_content = True  # Allows reading messages
intents.presences = True  # Allows detecting user presence (optional)
intents.members = True  # Allows fetching member lists (optional)

# Create the bot
bot = commands.Bot(command_prefix="!", intents=intents)

from datetime import datetime

# Get current date
current_date = datetime.now().date()

TARGET_USER_ID = 1339241886447046758
IVAN = 1216378821679513691 #ivan
MAXIMO = 1233735689950990388 #me
MIGUEL = 897507146210631701 #miguel

Salutations = ["hi","hii","hiii","sup","whatsup","heys","helo","hello", "going on", "happening"]

print(type(current_date))

# Event: When bot is ready
@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

    channel = bot.get_channel(1304486961469456497)

    if channel:
        await channel.send("Hiii UWU hoiwz evwyone dowing >v<")


@bot.command()
async def hurray(ctx):
    await ctx.send("Huwway!!>v<")

@bot.command()
async def agree(ctx):
    await ctx.send("o-oh, i agwe wit that!! 7w7")

@bot.command()
async def sry(ctx):
    await ctx.send("Aww:[ wat did I dwo wongg??")

@bot.command()
async def horny(ctx):
    await ctx.send(f"sending orbital strike to {ctx.author}'s house")

@bot.command()
async def news(ctx):
    await ctx.send("https://tenor.com/view/breaking-news-news-news-alert-sml-supermariologan-gif-20828801")

@bot.command()
async def cool_vid(ctx):
    await ctx.send("https://www.youtube.com/watch?v=xvFZjo5PgG0")

@bot.command()
async def bday(ctx):
    if str(current_date) == "2025-02-16":
        await ctx.send("Happwy Bwirthdway Autism Creature")
    elif str(current_date) == "2025-09-01":
        await ctx.send("Happwy Bwirthdway Dad")
    elif str(current_date) == "2025-09-12":
        await ctx.send("Happwy Bwirthdway daddy")
    else:
        await ctx.send("today isnt any1s birthday dumass")

@bot.command()
async def silksong_news(ctx):
    await ctx.send(f"""Totay is-s {current_date}.
    

    
This is youw chan MommyChomperUwU333, youwu chan for todawy, bringing you youw dailyw Silksong newuuys>_<

Thewe had been nuw newys to repowt for silksong todawy.

This has been your daily news for silksong for today, And MommyChomperUwU333 as your host for today""")

@bot.command()
async def server(ctx, member: discord.Member):

    while True:
        await ctx.send(f"{member.mention} server")

@bot.event
async def on_message(message):
    # Prevent the bot from replying to itself
    if message.author == bot.user:
        return

    if any(word in message.content.lower() for word in Salutations):
        if message.author.id == IVAN:
            await message.channel.send(f"luv you daddy")
        elif message.author.id == MIGUEL:
            await message.channel.send(f"Hiii awtism cweature")
        elif message.author.id == MAXIMO:
            await message.channel.send(f"OH, Hwi Dad :3")

    if any(word in message.content.lower() for word in ["smash"]):
        await message.channel.send("No yuw uglwy ):")
        

    if message.content.lower() == "stfu" or message.content.lower() == "shut the fuck up":
        await message.channel.send(f"Yea! shut up you Mother Fucking niga no bitches no cock so black the night looks like day.")
        await message.channel.send(f"Oopsie ;D")

    if any(word in message.content.lower() for word in ["kys","kill yourself"]):
        await message.channel.send("W-w-wayt!! Dun't do it); giwey youw amongus dead body tuo me fiwst>_<")

    if bot.user in message.mentions:
        # Ignore if the message is a reply to the bot
        if message.reference and message.reference.resolved:
            if message.reference.resolved.author == bot.user:
                return  # Do nothing
        if message.author.id == IVAN:
            await message.channel.send(f"luv you daddy")
        elif message.author.id == MIGUEL:
            await message.channel.send(f"Hiii awtism cweature")
        elif message.author.id == MAXIMO:
            await message.channel.send(f"OH, Hwi Dad :3")
        else:
            await message.channel.send(f"Did someowne pingwed me? •v•")

    # Process commands (if you want to use commands alongside this)
    await bot.process_commands(message)

# Run the bot (Replace YOUR_TOKEN_HERE with your actual bot token)
bot.run("MTMzOTI2MzE0MDQ3MDMyNTM2MQ.Gy2m0v.7rV_88i4ANlkAUbXlarXldnTlw5h3TPTNr736U")
