from datetime import datetime
from apscheduler.schedulers.background import BlockingScheduler
import subprocess as sub
import logging


x = 513
# logging.basicConfig(level=logging.INFO)
# 输出时间


def job():
    s = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(s)
    logging.info(f"Time: {s}")


# 每日测试一下地址
def daily():
    try:
        sub.run(["ffmpeg", "-y", "-i", "https://fms2.uniqueradio.jp/agqr10/aandg1.m3u8",
                 "-t", "60", f"output/daily.mp4"], check=True, timeout=80)
    except sub.TimeoutExpired:
        print("into timeout exception")
        logging.info("Daily Timeout, proc should be terminated")
        # 周日 晚上七点半（日本时间）


def botjob():
    global x
    # 避免403，提前触发，录稍微久一点，之后才trim
    sub.run(["ffmpeg", "-y", "-i", "https://fms2.uniqueradio.jp/agqr10/aandg1.m3u8",
             "-t", "60", f"output/{x}.mp4"], check=True)
    x += 1

# 周六早上十点半（日本时间）


def backup():
    global x
    sub.run(["ffmpeg", "-y", "-i", "https://fms2.uniqueradio.jp/agqr10/aandg1.m3u8",
             "-t", "60", f"output/{x}.mp4"], check=True)


# scheduler = BackgroundScheduler()
scheduler = BlockingScheduler()
scheduler.add_job(job, 'cron', second='*/5')
scheduler.add_job(daily, 'cron', minute='*/3')
# scheduler.add_job(backup, 'cron', day_of_week='6', hour=11, minute=38)
# scheduler.add_job(botjob, 'cron', day_of_week='6', hour=11, minute=38)

scheduler.start()  # 输出时间
