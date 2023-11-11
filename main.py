import interactions
from datetime import datetime, timedelta
from dateutil import tz

import time

from dotenv import load_dotenv
from os import environ as env

from ics import Calendar
import requests

import threading

# Load the .env file
load_dotenv()


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


def day_events(days, classe):
    """
    Return the events of the day in a list
    """

    global c1, c2, c3, c4, c5

    if classe == "1A":
        c = c1
    elif classe == "2ARIO":
        c = c2
    elif classe == "2ASDIA":
        c = c3
    elif classe == "3ARIO":
        c = c4
    elif classe == "3ASDIA":
        c = c5
    else:
        return

    # If no calendar is set for this class
    if c is None:
        return "```fix\nPas d'emploi du temps configuré pour cette classe\n```"

    today_lst = []

    date = datetime.now()

    date = date + timedelta(days=days)
    datefor = "%s" % date.strftime('%Y-%m-%d')

    today_msg = "**__"+str(date.strftime('%A %d %B'))+"("+classe+")"+"__**\n"

    for event in c.events:
        if event.begin.strftime('%Y-%m-%d') == datefor:
            event.begin = event.begin.astimezone(tz.tzlocal())
            event.end = event.end.astimezone(tz.tzlocal())

            tmp_begin_hour = (int(event.begin.hour))
            tmp_end_hour = (int(event.end.hour))
            if tmp_begin_hour < 10:
                tmp_begin_hour = "0"+str(tmp_begin_hour)
            if event.begin.minute == 0:
                event.begin.minute = "00"
            if event.end.minute == 0:
                event.end.minute = "00"
            if event.location == None:
                today_lst.append("```fix\n"+str(tmp_begin_hour)+":"+str(event.begin.minute) + " - "+str(
                    tmp_end_hour)+":"+str(event.end.minute)+" - " + event.name.encode("latin-1").decode("utf-8")+"\n```")
            else:
                today_lst.append("```fix\n"+str(tmp_begin_hour)+":"+str(event.begin.minute) + " - "+str(
                    tmp_end_hour)+":"+str(event.end.minute)+" - " + event.name.encode("latin-1").decode("utf-8")+" -> "+event.location.encode("latin-1").decode("utf-8").split("(")[0]+"\n```")

    today_lst.sort()
    if today_lst == []:
        today_lst.append("```fix\nAucun événement pour aujourd'hui\n```")

    for cours in today_lst:
        today_msg += cours

    today_msg += "\n"

    return today_msg


def fill_calendar():
    global c1, c2, c3, c4, c5

    while True:
        # Check if env vars are set one by one and if not, set them to None
        if env["URL_1A"] == "":
            c1 = None
        else:
            c1 = Calendar(requests.get(env["URL_1A"]).text)

        if env["URL_2A_RIO"] == "":
            c2 = None
        else:
            c2 = Calendar(requests.get(env["URL_2A_RIO"]).text)

        if env["URL_2A_SDIA"] == "":
            c3 = None
        else:
            c3 = Calendar(requests.get(env["URL_2A_SDIA"]).text)

        if env["URL_3A_RIO"] == "":
            c4 = None
        else:
            c4 = Calendar(requests.get(env["URL_3A_RIO"]).text)

        if env["URL_3A_SDIA"] == "":
            c5 = None
        else:
            c5 = Calendar(requests.get(env["URL_3A_SDIA"]).text)

        print("Calendars updated")

        # Wait 10 minutes before checking again
        time.sleep(600)
        c1 = None
        c2 = None
        c3 = None
        c4 = None
        c5 = None


if __name__ == "__main__":

    # Load the .env file
    load_dotenv()

    # Global variables to store the calendars
    c1 = None
    c2 = None
    c3 = None
    c4 = None
    c5 = None

    # Create the bot
    bot = interactions.Client(token=env["TOKEN"],
                              intents=interactions.Intents.ALL)

    # Start the calendar filling in a new thread
    threading.Thread(target=fill_calendar).start()

    # Start the bot
    bot.start()
