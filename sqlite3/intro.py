import sqlite3
conn = sqlite3.connect('/home/scarlet/py/py-dev/sqlite3/master_10081200.db')
c = conn.cursor()

c.execute('select * from sqlite_master')
print(c.fetchall())