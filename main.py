#!/usr/bin/env python3

import datetime
import locale
import time
import os

from art import *

locale.setlocale(locale.LC_TIME, 'vi_VN.UTF-8')


def replace_vn_chars(day):
    day = day.replace("ủ", "u")
    day = day.replace("ậ", "a")
    day = day.replace("ú", "u")
    day = day.replace("ậ", "a")
    day = day.replace("ứ", "u")
    day = day.replace("ứ", "u")
    day = day.replace("ư", "u")
    day = day.replace("ă", "a")
    day = day.replace("á", "a")
    day = day.replace("ả", "a")
    return day


while True:
    os.system('cls' if os.name == 'nt' else "printf '\033c'")

    d = datetime.datetime.now()
    dday = replace_vn_chars(d.strftime("%A"))
    ddate = d.strftime("%x")
    dtime = d.strftime("%I:%M:%S %p")

    tprint(dday.upper(), font="tarty1")
    tprint(ddate, font="tarty1")
    tprint(dtime, font="tarty1")

    time.sleep(1)
