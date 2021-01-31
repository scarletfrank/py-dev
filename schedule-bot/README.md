# 

## Windows & Linux

二者通用的脚本，不过配置方式不太一样。都要保证`ffmpeg`在路径上。


## 页面录制逻辑

`ffmpeg`对`m3u8`定点录制，录制三十分钟。感觉要提前一点触发任务，测试的时候出现了`403`问题

```bash
# [tcp @ 0x55bce8d530c0] Connection to tcp://fms2.uniqueradio.jp:443 failed: Connection timed out
# https://fms2.uniqueradio.jp/agqr10/aandg1.m3u8: Connection timed out
python3 cron-test.py > output.log
# 单步执行
```

单步执行


## 用Docker持久化容器运行

> 还没写完。upload的部分感觉没写对，8001端口没监听到，原来是我忘记添加了...

```bash
docker-compose up -d --build
docker-compose down -v
```

### alpine 时区设置

- [wiki](https://wiki.alpinelinux.org/wiki/Setting_the_timezone)
- [issue](https://github.com/gliderlabs/docker-alpine/issues/136)