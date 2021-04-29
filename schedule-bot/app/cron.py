from datetime import datetime
from apscheduler.schedulers.background import BlockingScheduler
import subprocess as sub
import logging
import os


x = 515

# 输出时间

def job():
    print("[Time]" + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# 每日测试一下地址

def daily():
    try:
        sub.run(["minyami -d https://fms2.uniqueradio.jp/agqr10/aandg1.m3u8 --live", 
        f"--output mediafiles/daily.ts"], check=True, timeout=60)
    except sub.TimeoutExpired:
        logging.warning("[daily] 录制时间已到，关闭程序")

# 周日 晚上七点半（日本时间）


def botjob():
    global x
    try:
        sub.run(["minyami -d https://fms2.uniqueradio.jp/agqr10/aandg1.m3u8 --live",
                 f" --output mediafiles/{x}_fresh.ts"], check=True, timeout=1860)
        x += 1
    except sub.TimeoutExpired:
        logging.warning("[fresh] 录制时间已到，关闭程序")


# 周六早上十点半（日本时间）
def backup():
    global x
    try:
        sub.run(["minyami -d https://fms2.uniqueradio.jp/agqr10/aandg1.m3u8 --live",
                  f"--output mediafiles/{x-1}_bk.mp4"], check=True, timeout=1860)
    except sub.TimeoutExpired:
        logging.warning("[backup] 录制时间已到，关闭程序")


# scheduler = BackgroundScheduler()
scheduler = BlockingScheduler()
scheduler.add_job(job, 'cron', minute='*/20')
scheduler.add_job(daily, 'cron', hour='*/1')
scheduler.add_job(backup, 'cron', day_of_week='5', hour=9, minute=29)
scheduler.add_job(botjob, 'cron', day_of_week='6', hour=18, minute=29)


scheduler.start()  # 输出时间
