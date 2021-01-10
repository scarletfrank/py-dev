# 保证Linux下和Win10下的兼容性

import os
import subprocess


with open('.env.dev', 'r', encoding='utf-8') as f:
    lines = f.readlines()

m = {}
for line in lines:
    a, b, c = line.split(" ")
    if a == "SECRET_KEY":
        c = c.replace("'", "")
    m[a] = c
    os.environ[a] = c

# os.environ["SECRET_KEY"] = c
# print(os.environ["SECRET_KEY"])

cmd = "python manage.py runserver"
subprocess.run(cmd.split(" "))
