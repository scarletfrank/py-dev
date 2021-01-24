from datetime import datetime
from apscheduler.schedulers.background import BlockingScheduler

x = 512

# 输出时间


def job():
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


# scheduler = BackgroundScheduler()
scheduler = BlockingScheduler()
scheduler.add_job(job, 'cron', second='*/10')

scheduler.start()  # 输出时间
