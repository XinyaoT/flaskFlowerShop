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

server = "127.0.0.1,1433"  # 请确保服务器名称和端口号的正确性
user = "sa"
password = "tzqsgdmn"
database = "FlowerShopFinal"

# pyodbc连接数据库
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + user + ';PWD=' + password)
cursor = conn.cursor()

if conn:
    print("数据库已连接成功")

