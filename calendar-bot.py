import interactions
from datetime import datetime

from config import token, CHANNEL_ID
from stylized_day_events import day_events

bot = interactions.Client(token=token,
                          intents=interactions.Intents.ALL)


@bot.command(name='today', description='Print today\'s events')
async def _today(ctx: interactions.CommandContext):
    embed = interactions.Embed(title="Today lessons",
                               description=day_events(0), color=0x00ff00)
    await ctx.send(embeds=embed)


@bot.command(name='tomorrow', description='Print tomorrow\'s events')
async def _tomorrow(ctx: interactions.CommandContext):
    embed = interactions.Embed(title="Tomorrow lessons",
                               description=day_events(1), color=0x00ff00)
    await ctx.send(embeds=embed)


@bot.command(name='week', description='Print the week\'s events')
async def _week(ctx: interactions.CommandContext):
    embed = interactions.Embed(title="Week lessons", description=day_events(0)+day_events(1)+day_events(
        2)+day_events(3)+day_events(4)+day_events(5)+day_events(6)+day_events(7), color=0x00ff00)
    await ctx.send(embeds=embed)


@bot.command(name='day', description='Print the day\'s events',
             options=[
                 interactions.Option(
                     name="date",
                     description="The date of the day you want to see (YYYY-MM-DD)",
                     type=interactions.OptionType.STRING,
                     required=True,
                 ),
             ],)
async def _day(ctx: interactions.CommandContext, date: str):
    try:
        date = datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        await ctx.send("Invalide date")
        return

    delta = date - datetime.now()
    embed = interactions.Embed(title="Day lessons",
                               description=day_events(delta.days + 1), color=0x00ff00)
    await ctx.send(embeds=embed)


@bot.event
async def on_ready():
    channel = await bot._http.get_channel(CHANNEL_ID)
    channel = interactions.Channel(**channel, _client=bot._http)
    await channel.send("I'm ready !")

bot.start()
