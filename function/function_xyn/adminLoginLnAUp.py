# -*- codeing = utf-8 -*-
# @Time : 2023/5/30 19:46
# @Author : Murphy_42
# @File : adminLoginLnAUp.py
# @Software : PyCharm

import pymssql
import shortuuid
from config import conn,cursor

#判断为空
def manager_null(id,password):
	if(id==''or password==''):
		return True
	else:
		return False

# 增
def manager_insert(password, sex, name):
    # 用于生成唯一标识符
    id = "m" + shortuuid.ShortUUID(alphabet='0123456789').random(length=7)
    # # 连接数据库
    # conn = pymssql.connect(server='LAPTOP-D2INVD39', user='sa', password='123', database='flower_shop_6')
    # # 创建游标对象
    # cursor = conn.cursor()
    # 插入数据的SQL语句
    insert_query = "INSERT INTO manager (manager_id,manager_name,manager_sex,manager_password) VALUES (?, ?, ?, ?)"
    # 插入数据的参数
    data = (id, password, sex, name)
    # 执行插入操作
    cursor.execute(insert_query, data)
    # 提交事务
    conn.commit()
    # 关闭连接
    conn.close()
    #返回id
    return id

#查
def manager_select(column_value1, column_value2):
    # 连接数据库
    # conn = pymssql.connect(server='LAPTOP-D2INVD39', user='sa', password='123', database='flower_shop_6')
    # if conn:
    #     str="连接成功1"
    # print(str)
    # # 创建游标对象
    # cursor = conn.cursor()
    # 查找数据的SQL语句
    select_query = "SELECT * FROM manageer WHERE manager_id = ? AND manager_password = ?"
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
    cursor.close()
    # 关闭连接
    conn.close()