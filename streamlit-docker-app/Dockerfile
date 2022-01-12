
FROM python:3.8-alpine
# 设置镜像源，提高pip install 速度
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install --upgrade pip 
RUN pip install flake8
COPY . .
RUN flake8 --ignore=E501,F401 .
COPY ./requirements.txt .
RUN pip isntall -r requirements.txt

# streamlit hello创建一个演示页面，映射80端口以便网页访问
CMD ["streamlit","hello", "--server.port","80"] 