import interactions
from datetime import datetime

from dotenv import load_dotenv
from os import environ as env

from stylized_day_events import day_events

load_dotenv()

bot = interactions.Client(token=env["TOKEN"],
                          intents=interactions.Intents.ALL)


@interactions.slash_command(name="calendar", description="Get help with the calendar bot")
async def _help(ctx: interactions.SlashContext):
    await ctx.send("The commands are: \n```\n\t/calendar : to get help msg\n\t/today <1A|2ASDIA|2ARIO|3ASDIA|3ARIO> : to get the day's events\n\t/tomorrow <1A|2ASDIA|2ARIO|3ASDIA|3ARIO> : to get the day's events\n\t/week <1A|2ASDIA|2ARIO|3ASDIA|3ARIO> : to get the week's events.```")


@interactions.slash_command(name='today', description='Print today\'s events')
@interactions.slash_option(
    name="classe",
    description="The class you want to see (1A or 2ARIO or 2ASDIA or 3ARIO or 3ASDIA)",
    opt_type=interactions.OptionType.STRING,
    choices=[
        interactions.SlashCommandChoice(name="1A", value="1A"),
        interactions.SlashCommandChoice(name="2ARIO", value="2ARIO"),
        interactions.SlashCommandChoice(name="2ASDIA", value="2ASDIA"),
        interactions.SlashCommandChoice(name="3ARIO", value="3ARIO"),
        interactions.SlashCommandChoice(name="3ASDIA", value="3ASDIA")
    ],
    required=True
)
async def _today(ctx: interactions.SlashContext, classe: str):
    if classe not in ["1A", "2ARIO", "2ASDIA", "3ARIO", "3ASDIA"]:
        await ctx.send(content="The class you entered is not valid")
        return
    embed = interactions.Embed(title="Today lessons",
                               description=day_events(0, classe), color=0x00ff00)
    embed.set_footer(text="By Thomas DUMOND",
                     icon_url="https://avatars.githubusercontent.com/u/28956167?s=400&u=195ab629066c0d1f29d6917d6479e59861349b2d&v=4")
    await ctx.send(embeds=embed)


@interactions.slash_command(name='tomorrow', description='Print tomorrow\'s events')
@interactions.slash_option(
    name="classe",
    description="The class you want to see (1A or 2ARIO or 2ASDIA or 3ARIO or 3ASDIA)",
    opt_type=interactions.OptionType.STRING,
    choices=[
        interactions.SlashCommandChoice(name="1A", value="1A"),
        interactions.SlashCommandChoice(name="2ARIO", value="2ARIO"),
        interactions.SlashCommandChoice(name="2ASDIA", value="2ASDIA"),
        interactions.SlashCommandChoice(name="3ARIO", value="3ARIO"),
        interactions.SlashCommandChoice(name="3ASDIA", value="3ASDIA")
    ],
    required=True
)
async def _tomorrow(ctx: interactions.SlashContext, classe: str):
    if classe not in ["1A", "2ARIO", "2ASDIA", "3ARIO", "3ASDIA"]:
        await ctx.send(content="The class you entered is not valid")
        return

    embed = interactions.Embed(title="Tomorrow lessons",
                               description=day_events(1, classe), color=0x00ff00)
    embed.set_footer(text="By Thomas DUMOND",
                     icon_url="https://avatars.githubusercontent.com/u/28956167?s=400&u=195ab629066c0d1f29d6917d6479e59861349b2d&v=4")
    await ctx.send(embeds=embed)


@interactions.slash_command(name='week', description='Print the week\'s events')
@interactions.slash_option(
    name="classe",
    description="The class you want to see (1A or 2ARIO or 2ASDIA or 3ARIO or 3ASDIA)",
    opt_type=interactions.OptionType.STRING,
    choices=[
        interactions.SlashCommandChoice(name="1A", value="1A"),
        interactions.SlashCommandChoice(name="2ARIO", value="2ARIO"),
        interactions.SlashCommandChoice(name="2ASDIA", value="2ASDIA"),
        interactions.SlashCommandChoice(name="3ARIO", value="3ARIO"),
        interactions.SlashCommandChoice(name="3ASDIA", value="3ASDIA")
    ],
    required=True
)
async def _week(ctx: interactions.SlashContext, classe: str):
    if classe not in ["1A", "2ARIO", "2ASDIA", "3ARIO", "3ASDIA"]:
        await ctx.send(content="The class you entered is not valid")
        return
    buff = day_events(0, classe)+day_events(1, classe)+day_events(
        2, classe)+day_events(3, classe)+day_events(4, classe)+day_events(5, classe)+day_events(6, classe)+day_events(7, classe)
    embed = interactions.Embed(
        title="Week lessons", description=buff, color=0x00ff00)
    embed.set_footer(text="By Thomas DUMOND",
                     icon_url="https://avatars.githubusercontent.com/u/28956167?s=400&u=195ab629066c0d1f29d6917d6479e59861349b2d&v=4")
    await ctx.send(embeds=embed)


@interactions.slash_command(name='day', description='Print the day\'s events')
@interactions.slash_option(
    name="date",
    description="The date of the day you want to see (YYYY-MM-DD)",
    opt_type=interactions.OptionType.STRING,
    required=True
)
@interactions.slash_option(
    name="classe",
    description="The class you want to see (1A or 2ARIO or 2ASDIA or 3ARIO or 3ASDIA)",
    opt_type=interactions.OptionType.STRING,
    choices=[
        interactions.SlashCommandChoice(name="1A", value="1A"),
        interactions.SlashCommandChoice(name="2ARIO", value="2ARIO"),
        interactions.SlashCommandChoice(name="2ASDIA", value="2ASDIA"),
        interactions.SlashCommandChoice(name="3ARIO", value="3ARIO"),
        interactions.SlashCommandChoice(name="3ASDIA", value="3ASDIA")
    ],
    required=True
)
async def _day(ctx: interactions.SlashContext, date: str, classe: str):
    if classe not in ["1A", "2ARIO", "2ASDIA", "3ARIO", "3ASDIA"]:
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


@interactions.Task.create(interactions.TimeTrigger(hour=int(env["HOUR"]), minute=int(env["MINUTE"]), utc=False))
async def _daily_calendar():

    # Don't print calendar for the week-end so don't print it if it's friday or saturday
    if datetime.now().weekday() in [4, 5]:
        return

    # 1A
    channel = await bot.fetch_channel(env["CHANNEL_ID_1A"])
    await channel.purge(deletion_limit=10)
    embed = interactions.Embed(title="Next lessons",
                               description=day_events(1, "1A"),
                               color=0x00ff00)
    embed.set_footer(text="By Thomas DUMOND",
                     icon_url="https://avatars.githubusercontent.com/u/28956167?s=400&u=195ab629066c0d1f29d6917d6479e59861349b2d&v=4")
    await channel.send(embeds=embed)

    # 2ARIO
    channel = await bot.fetch_channel(env["CHANNEL_ID_2A_RIO"])
    await channel.purge(deletion_limit=10)
    embed = interactions.Embed(title="Next lessons",
                               description=day_events(1, "2ARIO"),
                               color=0x00ff00)
    embed.set_footer(text="By Thomas DUMOND",
                     icon_url="https://avatars.githubusercontent.com/u/28956167?s=400&u=195ab629066c0d1f29d6917d6479e59861349b2d&v=4")
    await channel.send(embeds=embed)

    # 2ASDIA
    channel = await bot.fetch_channel(env["CHANNEL_ID_2A_SDIA"])
    await channel.purge(deletion_limit=10)
    embed = interactions.Embed(title="Next lessons",
                               description=day_events(1, "2ASDIA"),
                               color=0x00ff00)
    embed.set_footer(text="By Thomas DUMOND",
                     icon_url="https://avatars.githubusercontent.com/u/28956167?s=400&u=195ab629066c0d1f29d6917d6479e59861349b2d&v=4")
    await channel.send(embeds=embed)

    # 3ARIO
    channel = await bot.fetch_channel(env["CHANNEL_ID_3A_RIO"])
    await channel.purge(deletion_limit=10)
    embed = interactions.Embed(title="Next lessons",
                               description=day_events(1, "3ARIO"),
                               color=0x00ff00)
    embed.set_footer(text="By Thomas DUMOND",
                     icon_url="https://avatars.githubusercontent.com/u/28956167?s=400&u=195ab629066c0d1f29d6917d6479e59861349b2d&v=4")
    await channel.send(embeds=embed)

    # 3ASDIA
    channel = await bot.fetch_channel(env["CHANNEL_ID_3A_SDIA"])
    await channel.purge(deletion_limit=10)
    embed = interactions.Embed(title="Next lessons",
                               description=day_events(1, "3ASDIA"),
                               color=0x00ff00)
    embed.set_footer(text="By Thomas DUMOND",
                     icon_url="https://avatars.githubusercontent.com/u/28956167?s=400&u=195ab629066c0d1f29d6917d6479e59861349b2d&v=4")
    await channel.send(embeds=embed)


@interactions.listen()
async def on_start(event: interactions.api.events.Startup):
    # Add status to the bot
    await bot.change_presence(
        activity=interactions.Activity(
            name="/calendar", type=interactions.ActivityType.PLAYING)
    )

    # Start the daily calendar task
    _daily_calendar.start()


bot.start()
