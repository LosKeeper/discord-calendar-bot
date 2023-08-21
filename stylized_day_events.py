
from datetime import datetime, timedelta
from dateutil import tz

from dotenv import load_dotenv
from os import environ as env

from ics import Calendar
import requests

load_dotenv()

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


def day_events(days, classe):
    """
    Return the events of the day in a list
    """
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
