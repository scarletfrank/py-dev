from datetime import datetime
from apscheduler.schedulers.background import BlockingScheduler
import subprocess as sub
import sys
import logging
import os
import signal

logging.basicConfig(stream=sys.stdout, level=logging.INFO)


x = 526

# 输出时间


def job():
    logging.info("[Time]" + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


def daily():
    p1 = sub.Popen(['minyami', '-d', 'https://fms2.uniqueradio.jp/agqr10/aandg1.m3u8',
                '--live', '--output', 'mediafiles/daily.ts'])
    try:
        logging.info("执行minyami[daily]")
        out, errs = p1.communicate(timeout=30)
    except sub.TimeoutExpired as e:
        logging.warning("[daily] 录制时间已到，Ctrl+C 终止录制程序")
        p1.send_signal(signal.SIGINT)
        # p1.kill()


def botjob():
    """
    # 周日 晚上七点半（日本时间）
    """
    global x
    p1 = sub.Popen(['minyami', '-d', 'https://fms2.uniqueradio.jp/agqr10/aandg1.m3u8',
                '--live', '--output', f"mediafiles/{x}_fresh.ts"])
    try:
        logging.info("执行minyami[bot]")
        out, errs = p1.communicate(timeout=1860)
        x += 1
    except sub.TimeoutExpired as e:
        logging.warning("[bot] 录制时间已到，Ctrl+C 终止录制程序")
        p1.send_signal(signal.SIGINT)


def backup():
    """
    # 周六早上十点半（日本时间）
    """
    global x
    p1 = sub.Popen(['minyami', '-d', 'https://fms2.uniqueradio.jp/agqr10/aandg1.m3u8',
                '--live', '--output', f"mediafiles/{x-1}_backup.ts"])
    try:
        logging.info("执行minyami[backup]")
        out, errs = p1.communicate(timeout=1860)
    except sub.TimeoutExpired as e:
        logging.warning("[backup] 录制时间已到，Ctrl+C 终止录制程序")
        p1.send_signal(signal.SIGINT)

def ffmpegjob():
    """
    # 保留ffmpeg的方式，毕竟录Backup的时候很稳定。
    """
    global x
    try:
        logging.info("执行ffmpeg[backup]")
        sub.run(["ffmpeg", "-y", "-i", "https://fms2.uniqueradio.jp/agqr10/aandg1.m3u8",
                 "-t", "1860", f"mediafiles/{x}_backup.mp4"], check=True, timeout=1900)
        x += 1
    except sub.TimeoutExpired:
        logging.info("[ffmpeg-bot] 录制超时，killed掉程序")

# scheduler = BackgroundScheduler()
scheduler = BlockingScheduler()
scheduler.add_job(job, 'cron', minute='*/20')
scheduler.add_job(daily, 'cron', hour='*/2')
scheduler.add_job(backup, 'cron', day_of_week='5', hour=9, minute=29)
scheduler.add_job(botjob, 'cron', day_of_week='6', hour=18, minute=29)


scheduler.start()  # 输出时间
