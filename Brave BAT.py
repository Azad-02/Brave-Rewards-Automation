from datetime import datetime
import pyautogui as pe
import time
import os


def add_hour():
    now = datetime.now()
    only_second = now.strftime('%S')
    only_minute = now.strftime('%M')
    only_hour = now.strftime('%H')
    plus_hour = int(only_hour) + 1
    os.system(f'time {plus_hour}:{only_minute}:{only_second}')


def hour_rst():
    now = datetime.now()
    only_second = now.strftime('%S')
    only_minute = now.strftime('%M')
    only_hour = now.strftime('%H')
    rset_hour = int(only_hour) - 6
    os.system(f'time {rset_hour}:{only_minute}:{only_second}')


def add_date():
    import datetime
    today = datetime.date.today()
    only_date = today.strftime('%d')
    only_month = today.strftime('%m')
    only_year = today.strftime('%y')
    plus_date = int(only_date) + 1
    os.system(f'date {plus_date}-{only_month}-{only_year}')


for z in range(4):
    for x in range(1):
        for i in range(7):
            os.startfile("C:\Program Files\BraveSoftware\Brave-Browser\Application\Brave.exe")
            time.sleep(5)
            for i in range(20):
                pe.press('F5', interval=1.0)
#               pe.click(85, 45, interval=3.0)
            pe.click(1345, 10)
            time.sleep(3)
            add_hour()
    time.sleep(3)
    hour_rst()
    time.sleep(3)
    add_date()
    time.sleep(3)
