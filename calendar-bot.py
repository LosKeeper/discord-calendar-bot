import discord
from discord_slash import SlashCommand, SlashContext
from discord.ext import commands
from datetime import datetime

from config import token
from stylized_day_events import day_events

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())
slash = SlashCommand(bot, sync_commands=True)


@bot.event
async def on_ready():
    print('Logged in as {0.user}'.format(bot))


@slash.slash(name='jour', description='Affiche les événements du jour')
async def _jour(ctx: SlashContext):
    embed = discord.Embed(title="Cours du jour",
                          description=day_events(0), color=0x00ff00)
    await ctx.send(embed=embed)


@slash.slash(name='demain', description='Affiche les événements de demain')
async def _demain(ctx: SlashContext):
    embed = discord.Embed(title="Cours de demain",
                          description=day_events(1), color=0x00ff00)
    await ctx.send(embed=embed)


@slash.slash(name='semaine', description='Affiche les événements de la semaine')
async def _semaine(ctx: SlashContext):
    embed = discord.Embed(title="Cours de la semaine", description=day_events(
        0)+day_events(1)+day_events(2)+day_events(3)+day_events(4)+day_events(5)+day_events(6)+day_events(7), color=0x00ff00)
    await ctx.send(embed=embed)


@slash.slash(name='date', description='Affiche les événements de la date')
async def _date(ctx: SlashContext, user_input: str = ""):
    try:
        str = datetime.strptime(str, '%Y-%m-%d')
    except ValueError:
        await ctx.send("Date invalide")
        return

    embed = discord.Embed(title="Cours de la date",
                          description=day_events(str), color=0x00ff00)
    await ctx.send(embed=embed)

bot.run(token)
