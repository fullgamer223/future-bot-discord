import discord
import time
from discord.ext import commands

bot = commands.Bot(command_prefix="f.", description="")

@bot.event
async def on_ready():
    game = discord.Activity(type=discord.ActivityType.listening, name="something")
    await bot.change_presence(status=discord.Status.dnd, activity=game)

@bot.command(pass_context = True)
async def ping(ctx):
    t = await ctx.send('Ping? :thinking:')
    ms = (t.timestamp-ctx.message.timestamp).total_seconds() * 1000
    await ctx.edit_message(t, new_content='Pong! Took: {}ms'.format(int(ms)))

bot.run("NDQ5NjMxNTE3NTUyMTQ4NDgx.Dgv9qQ.NWwrfY3Y39jyWpqxxxVKGanAKY4")
