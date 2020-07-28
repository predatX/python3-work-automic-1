#coding=utf-8

import csv
import pymysql
import re
import time
import os

#连接数据库
db = pymysql.connect(host='10.1.2.1', port=3304, user='uname', passwd='passwd', database='sonar')
cursor=db.cursor()
print(">>>>>>>>>>>>>>>>Connected>>>>>>>>>>>>>>>>: ", db)

#查询sonar所有项目：
sql1 = "SELECT NAME FROM projects WHERE scope='PRJ' ORDER BY created_at DESC limit 140;"
data11 = cursor.execute(sql1)
data12 = cursor.fetchall()
print(">>>>>1. Begin sleep 100>>>>>>>>>>")
time.sleep(100)
#将项目名称写入文件
with open('project-name.csv','w') as f:
    f.write( '\n'.join(' '.join(str(x) for x in tu) for tu in data12) )
f.close
print(">>>>>2. Begin sleep 100>>>>>>>>>>")
time.sleep(100)
#统计并存储uuid，按时间顺序，limit 140：
sql2 = "SELECT project_uuid FROM projects WHERE scope='PRJ' ORDER BY created_at DESC limit 140;"
data26 = cursor.execute(sql2)
data27 = cursor.fetchall()
print(">>>>>3. Begin sleep 100>>>>>>>>>>")
time.sleep(100)
with open('uuid.csv','w') as f:
    f.write( '\n'.join(' '.join(str(x) for x in tu) for tu in data27) )
f.close()

#查询sonar所有项目的日期，limit 140：
sql1 = "SELECT created_at FROM projects WHERE scope='PRJ' ORDER BY created_at DESC limit 140;"
data11 = cursor.execute(sql1)
data12 = cursor.fetchall()
print(">>>>>4. Begin sleep 100>>>>>>>>>>")
time.sleep(100)
#将项目名称写入文件
with open('date.csv','w') as f:
    f.write( '\n'.join(' '.join(str(x) for x in tu) for tu in data12) )

