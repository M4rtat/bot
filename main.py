import discord
from discord.ext import commands
import random
import string

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)


@bot.command(description='For when you wanna settle the score some other way')
async def removehelpers(ctx, *choices: str):
    """Chooses between multiple choices."""
    finallword = ''
    for i in range(len(choices)):
        if choices[i] != 'или' and choices[i] != 'и' and choices[i] != 'но' and choices[i] != 'если' and choices[i] != 'то':
            #await ctx.send(choices[i])
            finallword += ''
            finallword += choices[i]
    await ctx.send(finallword)


@bot.command()
async def randomsum(ctx, times: int,):
    resulting = 0
    for i in range(times):
        num = random.choice([1,2,3,4,5,6,7,8,9,10])
        await ctx.send(num)
        resulting = num + resulting
    await ctx.send(resulting)


@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

bot.run('MTIwODc0OTU3MTc3MDAyNDAxNg.GWwQKl.Ib5LvnV1gBpcT0Ks5PngtbENacZmKTNluSjeGE')
