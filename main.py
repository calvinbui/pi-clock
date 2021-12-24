import datetime
import locale
import time
import os

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
    dtime = d.strftime("%I:%M %p")

    print(dday)
    print(ddate)
    print(dtime)

    time.sleep(1)
