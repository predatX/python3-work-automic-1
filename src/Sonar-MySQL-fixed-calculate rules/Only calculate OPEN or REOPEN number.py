# coding=utf-8

import csv
import pymysql
import re
import time
import os

# 连接数据库
db = pymysql.connect(host='10.240.7.140', port=3306, user='root', passwd='123456', database='sonar')
cursor = db.cursor()
print("Result: ", db)

# 查询sonar所有项目：
sql1 = "SELECT NAME FROM projects WHERE scope='PRJ' ORDER BY created_at DESC limit 140;"
data11 = cursor.execute(sql1)
data12 = cursor.fetchall()
# print(">>>>>1. Begin sleep 100>>>>>>>>>>")
time.sleep(0.01)
# 将项目名称写入文件
with open('project-name.csv', 'w') as f:
    f.write('\n'.join(' '.join(str(x) for x in tu) for tu in data12))
f.close
# print(">>>>>2. Begin sleep 100>>>>>>>>>>")
time.sleep(0.01)
# 统计并存储uuid，按时间顺序，limit 140：
sql2 = "SELECT project_uuid FROM projects WHERE scope='PRJ' ORDER BY created_at DESC limit 140;"
data26 = cursor.execute(sql2)
data27 = cursor.fetchall()
# print(">>>>>3. Begin sleep 100>>>>>>>>>>")
time.sleep(0.01)
with open('uuid.csv', 'w') as f:
    f.write('\n'.join(' '.join(str(x) for x in tu) for tu in data27))
f.close()

# 查询sonar所有项目的日期，limit 140：
sql1 = "SELECT created_at FROM projects WHERE scope='PRJ' ORDER BY created_at DESC limit 140;"
data11 = cursor.execute(sql1)
data12 = cursor.fetchall()
# 将项目名称写入文件
with open('date.csv', 'w') as f:
    f.write('\n'.join(' '.join(str(x) for x in tu) for tu in data12))

# print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
# 如果存在同名的ruleid.csv文件，则先删掉
if os.path.exists("ruleid.csv"):
    os.remove("ruleid.csv")
# 按行取uuid，通过每次取到的uuid来查询并存储rule-id，rule-id就是sonar的rules在MySQL存储的id
p0 = p1 = p2 = p3 = 0  # p0,p1,p2,p3为不同的漏洞等级
null = ''
file21 = open('uuid.csv')
for cache in file21:
    sql2 = "SELECT rule_id FROM issues WHERE project_uuid='" + cache.replace("\n",
                                                                             "") + "' and (status='OPEN' or status='REOPENED') and issue_type IN(2) AND severity IN('BLOCKER','CRITICAL','MAJOR','MINOR');"
    data21 = cursor.execute(sql2)
    data22 = cursor.fetchall()
    # print(">>>>>4. Begin sleep 7>>>>>>>>>>")
    # time.sleep(7)
    # data23=str(data22)
    if data22 != ():
        for d22 in data22:
            print(d22)
            # if (d22 == (5151,) or d22 == (5143,)):
            if d22==(5151,):
                p0 = p0 + 1
            elif (d22 == (5274,) or d22 == (5285,) or d22 == (5371,) or d22 == (5544,) or d22 == (5122,) or d22 == (
            5368,) or d22 == (5430,) or d22 == (5112,) or d22 == (5317,) or d22 == (5296,) or d22 == (5382,) or d22 == (
                  5282,) or d22 == (5363,) or d22 == (5121,) or d22 == (5234,) or d22 == (5213,) or d22 == (
                  5446,) or d22 == (5072,) or d22 == (5356,) or d22 == (5216,) or d22 == (5448,) or d22 == (
                  5221,) or d22 == (5372,)):
                p1 = p1 + 1
            elif d22 != null:
                p2 = p2 + 1

# 统计p0-p2数量
print("Summary:")
print('Final P0: ')
print(p0)
print('Final P1: ')
print(p1)
print('Final P2: ')
print(p2)