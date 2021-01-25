# 非https的nginx 80 生产模拟

FROM nginx:1.19-alpine

RUN rm /etc/nginx/conf.d/default.conf
# 去除80端口 避免冲突
COPY upload.conf /etc/nginx/conf.d/upload.conf