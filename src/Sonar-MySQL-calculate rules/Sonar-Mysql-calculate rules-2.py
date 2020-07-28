#coding=utf-8

import csv
import pymysql
import re
import time
import os

#连接数据库
db = pymysql.connect(host='10.1.2.1', port=3304, user='uname', passwd='passwd', database='sonar')
cursor=db.cursor()
print("Result: ", db)

# print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
#如果存在同名的ruleid.csv文件，则先删掉
if os.path.exists("ruleid.csv"):
	os.remove("ruleid.csv")
#按行取uuid，通过每次取到的uuid来查询并存储rule-id，rule-id就是sonar的rules在MySQL存储的id
p0=p1=p2=p3=0 #p0,p1,p2,p3为不同的漏洞等级
null=''
file21=open('uuid.csv')
for cache in file21:
    sql2="SELECT rule_id FROM issues WHERE project_uuid='" + cache.replace("\n","")+ "' and issue_type IN(3) AND severity IN('BLOCKER','CRITICAL');"
    data21 = cursor.execute(sql2)
    data22 = cursor.fetchall()
    # print("                 ~Begin sleep 7~  Zzzz")
    data23=str(data22)
    print("after getted the str(p0-p1) from each rule_id "+data23)
    time.sleep(0.004)
    if data23!='()':
    	data24=data23
    	# print("~~~~~~~~~~~~~~~~~~~~~~~~IF- ONE TIME~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    	i25=re.findall(r'\b\d+\b',data24)
    	open('ruleid.csv','+a').write( '\n'.join(i25))
    open('ruleid.csv','+a').write( ''.join('\n'))
    open('ruleid.csv','+a').write( ''.join('\n'))
#统计p0-p2数量
file=open('ruleid.csv','r')
stus=csv.reader(file)
for stu3 in stus:
    if len(stu3):
    # if int(stu3[0]) != null:
        stu2=int(stu3[0])
        if (stu2==5151):
            p0=p0+1
        elif (stu2==5274 or stu2==5285 or stu2==5371 or stu2==5544 or stu2==5122 or stu2==5368 or stu2==5430 or stu2==5112 or stu2==5317 or stu2==5296 or stu2==5382 or stu2==5282 or stu2==5363 or stu2==5121 or stu2==5234 or stu2==5213 or stu2==5446 or stu2==5072 or stu2==5356 or stu2==5216 or stu2==5448 or stu2==5221 or stu2==5372):
            p1=p1+1
        elif stu2 != null:
            p2=p2+1

#统计p0-p2数量
print("Summary:")
print('Final P0: ')
print(int(p0))
print('Final P1: ')
print(int(p1))
print('Final P2: ')
print(int(p2))