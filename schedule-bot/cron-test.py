from datetime import datetime
from apscheduler.schedulers.background import BlockingScheduler
import subprocess as sub

x = 513

# 输出时间


def job():
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


# 每日测试一下地址
def daily():
    sub.run(["ffmpeg", "-y", "-i", "https://fms2.uniqueradio.jp/agqr10/aandg1.m3u8",
             "-t", "60", f"daily.mp4"], check=True)

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
scheduler.add_job(job, 'cron', second='*/59')
scheduler.add_job(daily, 'cron', minute=20)
scheduler.add_job(backup, 'cron', day_of_week='6', hour=11, minute=38)
scheduler.add_job(botjob, 'cron', day_of_week='6', hour=11, minute=38)

scheduler.start()  # 输出时间
