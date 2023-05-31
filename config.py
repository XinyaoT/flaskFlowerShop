#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2023/5/27 21:44
# @Author  : Smalltown
# @FileName: config.py
# @Software: PyCharm


# import pymssql
#
# conn = pymssql.connect(host="LAPTOP-D2INVD39", database='flower_shop_6', user='sa', password='123',charset='utf8')
# str = "连接失败！"
# if conn:
#     str = '连接成功！'
#     # db.close() # 关闭连接，释放内存
# print(str)  # 如果结果为连接成功即表示已经成功连接。
# cursor = conn.cursor()
# ###############################连接###########################################
import pyodbc as pyodbc
conn = pyodbc.connect('DRIVER={SQL Server};SERVER=LAPTOP-D2INVD39;DATABASE=flower_shop_6;UID=sa;PWD=123')
str = "连接失败！"
if conn:
    str='连接成功！'
    # db.close() # 关闭连接，释放内存
print(str) # 如果结果为连接成功即表示已经成功连接。
# host 为服务器名称
# database 表示你需要连接的数据库
# user及password 表示你SQL Server身份验证的登录名和密码
cursor = conn.cursor()