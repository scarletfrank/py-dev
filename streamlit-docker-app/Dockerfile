FROM python:3.8-slim

# set work directory
WORKDIR /usr/src/app

RUN pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/
RUN pip install --upgrade pip 
RUN pip install flake8
COPY . .
RUN flake8 --ignore=E501,F401 ./src
# install dependencies
COPY ./requirements.txt .

RUN pip install -r requirements.txt 

# streamlit hello创建一个演示页面，映射80端口以便网页访问
CMD ["streamlit","run", "src/app.py", "--server.port","80"] 