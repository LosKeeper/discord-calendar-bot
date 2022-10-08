import interactions
from datetime import datetime

from config import *
from stylized_day_events import day_events

bot = interactions.Client(token=token,
                          intents=interactions.Intents.ALL)


@bot.command(name='today', description='Print today\'s events',
             options=[interactions.Option(
                 name="classe",
                 description="The class you want to see (1A or 2ARIO or 2ASDIA)",
                 type=interactions.OptionType.STRING,
                 choice=["1A", "2ARIO", "2ASDIA"],
                 required=True,
             )])
async def _today(ctx: interactions.CommandContext, classe: str):
    if classe not in ["1A", "2ARIO", "2ASDIA"]:
        await ctx.send(content="The class you entered is not valid")
        return
    embed = interactions.Embed(title="Today lessons",
                               description=day_events(0, classe), color=0x00ff00)
    embed.set_footer(text="By Thomas DUMOND",
                     icon_url="https://avatars.githubusercontent.com/u/28956167?s=400&u=195ab629066c0d1f29d6917d6479e59861349b2d&v=4")
    await ctx.send(embeds=embed)


@bot.command(name='tomorrow', description='Print tomorrow\'s events',
             options=[interactions.Option(
                 name="classe",
                 description="The class you want to see (1A or 2ARIO or 2ASDIA)",
                 type=interactions.OptionType.STRING,
                 choice=["1A", "2ARIO", "2ASDIA"],
                 required=True,
             )])
async def _tomorrow(ctx: interactions.CommandContext, classe: str):
    if classe not in ["1A", "2ARIO", "2ASDIA"]:
        await ctx.send(content="The class you entered is not valid")
        return

    embed = interactions.Embed(title="Tomorrow lessons",
                               description=day_events(1, classe), color=0x00ff00)
    embed.set_footer(text="By Thomas DUMOND",
                     icon_url="https://avatars.githubusercontent.com/u/28956167?s=400&u=195ab629066c0d1f29d6917d6479e59861349b2d&v=4")
    await ctx.send(embeds=embed)


@ bot.command(name='week', description='Print the week\'s events',
              options=[
                  interactions.Option(
                      name="classe",
                      description="The class you want to see (1A or 2ARIO or 2ASDIA)",
                      type=interactions.OptionType.STRING,
                      choice=["1A", "2ARIO", "2ASDIA"],
                      required=True,
                  )])
async def _week(ctx: interactions.CommandContext, classe: str):
    if classe not in ["1A", "2ARIO", "2ASDIA"]:
        await ctx.send(content="The class you entered is not valid")
        return
    buff = day_events(0, classe)+day_events(1, classe)+day_events(
        2, classe)+day_events(3, classe)+day_events(4, classe)+day_events(5, classe)+day_events(6, classe)+day_events(7, classe)
    embed = interactions.Embed(
        title="Week lessons", description=buff, color=0x00ff00)
    embed.set_footer(text="By Thomas DUMOND",
                     icon_url="https://avatars.githubusercontent.com/u/28956167?s=400&u=195ab629066c0d1f29d6917d6479e59861349b2d&v=4")
    await ctx.send(embeds=embed)


@bot.command(name='day', description='Print the day\'s events',
             options=[
                  interactions.Option(
                      name="date",
                      description="The date of the day you want to see (YYYY-MM-DD)",
                      type=interactions.OptionType.STRING,
                      required=True,
                  ), interactions.Option(
                      name="classe",
                      description="The class you want to see (1A or 2ARIO or 2ASDIA)",
                      type=interactions.OptionType.STRING,
                      required=True,
                  )
             ],)
async def _day(ctx: interactions.CommandContext, date: str, classe: str):
    if classe not in ["1A", "2ARIO", "2ASDIA"]:
        await ctx.send(content="The class you entered is not valid")
        return
    try:
        date = datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        await ctx.send("Invalide date")
        return

    delta = date - datetime.now()
    embed = interactions.Embed(title="Day lessons",
                               description=day_events(delta.days + 1, classe),
                               color=0x00ff00)
    embed.set_footer(text="By Thomas DUMOND",
                     icon_url="https://avatars.githubusercontent.com/u/28956167?s=400&u=195ab629066c0d1f29d6917d6479e59861349b2d&v=4")
    await ctx.send(embeds=embed)


@ bot.event
async def on_start():
    # When bot is ready send time schedule in each 3 channels
    # 2ARIO
    channel = await bot._http.get_channel(CHANNEL_ID_2A_RIO)
    channel = interactions.Channel(**channel, _client=bot._http)
    await channel.purge(amount=10)
    embed = interactions.Embed(title="Next lessons",
                               description=day_events(1, "2ARIO"),
                               color=0x00ff00)
    embed.set_footer(text="By Thomas DUMOND",
                     icon_url="https://avatars.githubusercontent.com/u/28956167?s=400&u=195ab629066c0d1f29d6917d6479e59861349b2d&v=4")
    await channel.send(embeds=embed)

    # 2ASDIA
    channel = await bot._http.get_channel(CHANNEL_ID_2A_SDIA)
    channel = interactions.Channel(**channel, _client=bot._http)
    await channel.purge(amount=10)
    embed = interactions.Embed(title="Next lessons",
                               description=day_events(1, "2ASDIA"),
                               color=0x00ff00)
    embed.set_footer(text="By Thomas DUMOND",
                     icon_url="https://avatars.githubusercontent.com/u/28956167?s=400&u=195ab629066c0d1f29d6917d6479e59861349b2d&v=4")
    await channel.send(embeds=embed)

    # 1A
    channel = await bot._http.get_channel(CHANNEL_ID_1A)
    channel = interactions.Channel(**channel, _client=bot._http)
    await channel.purge(amount=10)
    embed = interactions.Embed(title="Next lessons",
                               description=day_events(1, "1A"),
                               color=0x00ff00)
    embed.set_footer(text="By Thomas DUMOND",
                     icon_url="https://avatars.githubusercontent.com/u/28956167?s=400&u=195ab629066c0d1f29d6917d6479e59861349b2d&v=4")
    await channel.send(embeds=embed)


bot.start()
