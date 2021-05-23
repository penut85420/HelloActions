import os
from discord.ext import commands
from pkg.utils import intdiv, plus, minus, multi, intdiv, moddiv

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user} | Ready!')

@bot.command(name='plus')
async def cmd_plus(ctx, a: int, b: int):
    await ctx.send(plus(a, b))

@bot.command(name='minus')
async def cmd_minus(ctx, a: int, b: int):
    await ctx.send(minus(a, b))

@bot.command(name='multi')
async def cmd_multi(ctx, a: int, b: int):
    await ctx.send(multi(a, b))

@bot.command(name='intdiv')
async def cmd_intdiv(ctx, a: int, b: int):
    await ctx.send(intdiv(a, b))

@bot.command(name='moddiv')
async def cmd_moddiv(ctx, a: int, b: int):
    await ctx.send(moddiv(a, b))

if __name__ == '__main__':
    bot.run(os.getenv('TOKEN'))
