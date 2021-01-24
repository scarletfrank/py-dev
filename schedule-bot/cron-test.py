from datetime import datetime
from apscheduler.schedulers.background import BlockingScheduler
import subprocess as sub

x = 512

# 输出时间


def job():
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


def botjob():
    global x
    # 避免403，提前触发，录稍微久一点，之后才trim
    sub.run(["ffmpeg", "-i", "https://fms2.uniqueradio.jp/agqr10/aandg1.m3u8",
             "-t", "60", f"output/{x}.mp4"])
    x += 1


# scheduler = BackgroundScheduler()
scheduler = BlockingScheduler()
scheduler.add_job(job, 'cron', second='*/30')
# scheduler.add_job(botjob, 'cron', day_of_week='6', hour=19, minute=10)

scheduler.start()  # 输出时间
