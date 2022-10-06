from datetime import datetime, timedelta
from config import url_1a, url_2a_rio, url_2a_sdia
from ics import Calendar
import requests

c1 = Calendar(requests.get(url_1a).text)
c2 = Calendar(requests.get(url_2a_rio).text)
c3 = Calendar(requests.get(url_2a_sdia).text)


def day_events(days, classe):

    if classe == "1A":
        c = c1
    elif classe == "2ARIO":
        c = c2
    elif classe == "2ASDIA":
        c = c3

    today_lst = []

    date = (datetime.now() + timedelta(days))
    datefor = "%s" % date.strftime('%Y-%m-%d')

    today_msg = "**__"+str(date.strftime('%A %d %B'))+"("+classe+")"+"__**\n"

    # Delta for UTC time
    deltaHour = 2

    for event in c.events:
        if event.begin.strftime('%Y-%m-%d') == datefor:
            event.begin.hour = int(event.begin.hour) + deltaHour
            event.end.hour = int(event.end.hour) + deltaHour
            if event.begin.hour < 10:
                event.begin.hour = "0"+str(event.begin.hour)
            if event.begin.minute == 0:
                event.begin.minute = "00"
            if event.end.minute == 0:
                event.end.minute = "00"
            today_lst.append("```fix\n"+str(event.begin.hour)+":"+str(event.begin.minute) + " - "+str(
                event.end.hour)+":"+str(event.end.minute)+" - " + event.name.encode("latin-1").decode("utf-8")+" -> "+event.location.encode("latin-1").decode("utf-8").split("(")[0]+"\n```")

    today_lst.sort()
    if today_lst == []:
        today_lst.append("```fix\nAucun événement pour aujourd'hui\n```")

    for cours in today_lst:
        today_msg += cours

    today_msg += "\n"

    return today_msg
