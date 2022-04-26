from datetime import datetime, timedelta
from config import url
from ics import Calendar
import requests

c = Calendar(requests.get(url).text)


def day_events(days):
    today_lst = []

    date = (datetime.now() + timedelta(days))
    datefor = "%s" % date.strftime('%Y-%m-%d')

    today_msg = "**__"+str(date.strftime('%A %d %B'))+"__**\n"

    for event in c.events:
        if event.begin.strftime('%Y-%m-%d') == datefor:
            event.begin.hour = event.begin.hour + 2
            event.end.hour = event.end.hour + 2
            if event.begin.hour < 10:
                event.begin.hour = "0"+str(event.begin.hour)
            if event.begin.minute == 0:
                event.begin.minute = "00"
            if event.end.minute == 0:
                event.end.minute = "00"
            today_lst.append("```fix\n"+str(event.begin.hour)+":"+str(event.begin.minute) + " - "+str(
                event.end.hour)+":"+str(event.end.minute)+" - " + event.name.encode("latin-1").decode("utf-8")+"\n```")

    today_lst.sort()
    if today_lst == []:
        today_lst.append("```fix\nAucun événement pour aujourd'hui\n```")

    for cours in today_lst:
        today_msg += cours

    today_msg += "\n"

    return today_msg
