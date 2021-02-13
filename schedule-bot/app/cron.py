from datetime import datetime
from apscheduler.schedulers.background import BlockingScheduler
import subprocess as sub
import logging

x = 515

# 输出时间


def job():
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# 每日测试一下地址


def daily():
    try:
        sub.run(["ffmpeg", "-y", "-i", "https://fms2.uniqueradio.jp/agqr10/aandg1.m3u8",
                 "-t", "60", f"mediafiles/daily.mp4"], check=True, timeout=80)
    except sub.TimeoutExpired:
        print("into timeout exception")
        logging.info("Daily Timeout, proc should be terminated")

# 周日 晚上七点半（日本时间）


def botjob():
    global x
    # 避免403，提前触发，录稍微久一点，之后才trim
    try:
        sub.run(["ffmpeg", "-y", "-i", "https://fms2.uniqueradio.jp/agqr10/aandg1.m3u8",
                 "-t", "1860", f"mediafiles/{x}_fresh.mp4"], check=True, timeout=1900)
        x += 1
    except sub.TimeoutExpired:
        print("into timeout exception")
        logging.info("Daily Timeout, proc should be terminated")


# 周六早上十点半（日本时间）
def backup():
    global x
    try:
        sub.run(["ffmpeg", "-y", "-i", "https://fms2.uniqueradio.jp/agqr10/aandg1.m3u8",
                 "-t", "1860", f"mediafiles/{x-1}_bk.mp4"], check=True, timeout=1900)
    except sub.TimeoutExpired:
        print("into timeout exception")
        logging.info("Daily Timeout, proc should be terminated")


# scheduler = BackgroundScheduler()
scheduler = BlockingScheduler()
scheduler.add_job(job, 'cron', minute='*/20')
scheduler.add_job(daily, 'cron', hour='*/1')
scheduler.add_job(backup, 'cron', day_of_week='5', hour=9, minute=29)
scheduler.add_job(botjob, 'cron', day_of_week='6', hour=18, minute=29)


scheduler.start()  # 输出时间
