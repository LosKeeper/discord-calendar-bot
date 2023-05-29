import pytz
from datetime import datetime, timedelta

from config import url_1a, url_2a_rio, url_2a_sdia
from ics import Calendar
import requests

c1 = Calendar(requests.get(url_1a).text)
c2 = Calendar(requests.get(url_2a_rio).text)
c3 = Calendar(requests.get(url_2a_sdia).text)


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

    today_lst = []

    # USE FOR TIMEZONE IN WINTER
    deltatime = 2

    date = datetime.now(pytz.timezone('Europe/Paris'))
    date = date + timedelta(days=days)
    datefor = "%s" % date.strftime('%Y-%m-%d')

    today_msg = "**__"+str(date.strftime('%A %d %B'))+"("+classe+")"+"__**\n"

    for event in c.events:
        if event.begin.strftime('%Y-%m-%d') == datefor:
            tmp_begin_hour = (int(event.begin.hour) + deltatime)
            tmp_end_hour = (int(event.end.hour) + deltatime)
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
