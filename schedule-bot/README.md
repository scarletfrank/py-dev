# README

## 环境

- Docker虚拟化 （WSL Or Ubuntu 18.04)
- python:3.8-alpine
- Node.js LTS
- Minyami 4.2.2

## 页面录制逻辑

### m3u8 地址

1. `https://fms2.uniqueradio.jp/agqr10/aandg1.m3u8`
2. `https://www.uniqueradio.jp/agplayerf/hls/HLS_Layer1-cdn.m3u8` 

关于`2`，参考在Minyami提的一个[issue](https://github.com/Last-Order/Minyami/issues/73)


`ffmpeg`对`m3u8`定点录制，录制三十分钟，读取文件内容。

除了`403`，我印象中确实出现过IO类的报错。

```log
[tcp @ 0x55bce8d530c0] Connection to tcp://fms2.uniqueradio.jp:443 failed: Connection timed out
```

### 


## Docker容器运行

> 还没写完。upload的部分感觉没写对，8001端口没监听到，原来是我忘记添加了...

```bash
docker-compose up -d --build
docker-commpose down
docker-compose down -v #会把volumes删掉

```

## 查看容器日志

> VS Code 只显示最近1000条，更细致的查询得自己加参数

```bash
docker logs --tail 1000 -f 35e3c6458c2310b28fbb5dfd2d5098a5aca9c1ac3796d7c9ac7274257c0edcca 
docker logs --since "2021-02-20" --tail 1000 -f 35e3c6458c2310b28fbb5dfd2d5098a5aca9c1ac3796d7c9ac7274257c0edcca 
docker inspect --format='{{.LogPath}}' 35e3c6458c2310b28fbb5dfd2d5098a5aca9c1ac3796d7c9ac7274257c0edcca 
```

### alpine 时区设置

- [wiki](https://wiki.alpinelinux.org/wiki/Setting_the_timezone)
- [issue](https://github.com/gliderlabs/docker-alpine/issues/136)