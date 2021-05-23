import os
from discord.ext import commands
from pkg.utils import plus, minus, multi

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user} | Ready!')

@bot.command(name='plus')
async def cmd_plus(ctx, a: int, b: int):
    await ctx.send(plus(a, b))

bot.run(os.getenv('TOKEN'))
