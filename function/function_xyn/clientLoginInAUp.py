#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2023/5/27 0:46
# @Author  : Smalltown
# @FileName: client.py
# @Software: PyCharm

import pymssql
import shortuuid
from config import conn,cursor

#判断为空
def client_null(id,password):
	if(id==''or password==''):
		return True
	else:
		return False

# 增
def client_insert(password, sex, phone, name):
    # 用于生成唯一标识符
    id = "u" + shortuuid.ShortUUID(alphabet='0123456789').random(length=7)
    # # 连接数据库
    # conn = pymssql.connect(server='LAPTOP-D2INVD39', user='sa', password='123', database='flower_shop_6')
    # # 创建游标对象
    # cursor = conn.cursor()
    # 插入数据的SQL语句
    insert_query = "INSERT INTO client (client_id,client_password,client_sex,client_phone,client_name) VALUES (?, ?, ?, ?, ?)"
    # 插入数据的参数
    data = (id, password, sex, phone, name)
    # 执行插入操作
    cursor.execute(insert_query, data)
    # 提交事务
    # conn.commit()
    # # 关闭连接
    # conn.close()
    #返回id
    return id

#查
def client_select(column_value1, column_value2):
    # 连接数据库
    # conn = pymssql.connect(server='LAPTOP-D2INVD39', user='sa', password='123', database='flower_shop_6')
    # if conn:
    #     str="连接成功1"
    # print(str)
    # # 创建游标对象
    # cursor = conn.cursor()
    # 查找数据的SQL语句
    select_query = "SELECT * FROM client WHERE client_id = ? AND client_password = ?"
    # 执行查找操作
    data = (column_value1, column_value2)
    cursor.execute(select_query, data)
    # 获取查找结果
    result = cursor.fetchall()
    if len(result) == 0:
        return False
    else:
        return True
    # 关闭游标
    # cursor.close()
    # # 关闭连接
    # conn.close()
