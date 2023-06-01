# -*- coding: utf-8 -*-
# 配置文件，用于实现数据库连接
# 发送邮箱，邮箱配置
# cookie、session加密

import pymssql
import pyodbc

# server    数据库服务器名称或IP
# user      用户名
# password  密码
# database  数据库名称
conn = pyodbc.connect('DRIVER={SQL Server};SERVER=LAPTOP-D2INVD39;DATABASE=flower_shop_6;UID=sa;PWD=123')
str = "连接失败！"
if conn:
    str='连接成功！'
    # db.close() # 关闭连接，释放内存
print(str) # 如果结果为连接成功即表示已经成功连接。
cursor = conn.cursor()

