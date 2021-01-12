# 读取本地env
with open('./env/.env.pg') as f:
    data = f.readlines()

m = {}
for line in data:
    pair = line.strip().split(" ")
    m[pair[0]] = pair[-1]

print(m)
# 

from sqlalchemy import create_engine
db = create_engine(f"postgresql+psycopg2://{m['pguser']}:{m['pgpwd']}@127.0.0.1:5432/{m['pgdb']}")

result_set = db.execute("SELECT * FROM customers")
for r in result_set:  
    print(r)


# 写程序的时候遇到一个问题
# Docker 在WSL2 网络下...
# 如何让Win10网络的应用去访问WSL2上的数据库
# 不对啊，仔细一想，我Dbeaver是直接访问localhost的...
# 哦我想起来了，是Clojure的应用在WSL2访问Docker...
# 那不也是本地吗
