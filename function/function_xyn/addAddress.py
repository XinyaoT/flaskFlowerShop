# -*- codeing = utf-8 -*-
# @Time : 2023/5/31 20:53
# @Author : Murphy_42
# @File : addAddress.py
# @Software : PyCharm

import pymssql
import pyodbc
import shortuuid
import random
from config import cursor,conn

def generate_random_number():
    return random.randint(0, 1)

#增
# 功能1：添加时还要添加到has_c_s表中（有条件的）
def address_insert(c_id,addr):
    # 用于生成唯一标识符
    a_id = "a" + shortuuid.ShortUUID(alphabet='0123456789').random(length=7)
    is_default=generate_random_number()

    #在address表中查询插入的数据是否已经存在
    select_query = "SELECT COUNT(*) FROM address WHERE consignee_addr = ?"
    data = (addr,)
    cursor.execute(select_query, data)
    count = cursor.fetchone()[0]

    # 查找用户添加的地址是否已经address表中了（直接返回地址）
    select_query = "SELECT * FROM address WHERE consignee_addr = ?"
    data = (addr,)
    cursor.execute(select_query,data)
    result = cursor.fetchone()
    if result is not None:
        result = result[0]

    #通过判断的条件，用事务transaction功能对两张表进行插入操作
    try:
        # 使用with语句处理事务
        with conn:
            if count<=0:
                # 执行address表插入操作
                insert_query1 = "INSERT INTO address (address_id, consignee_addr) VALUES (?, ?)"
                data1 = (a_id,addr)
                cursor.execute(insert_query1, data1)

                # 执行has_c_s表插入操作
                insert_query2 = "INSERT INTO has_c_a (address_id, client_id, is_default) VALUES (?, ?, ?)"
                data2 = (a_id, c_id,is_default)
                cursor.execute(insert_query2, data2)
            else:
                # 执行has_c_s表插入操作
                insert_query3 = "INSERT INTO has_c_a (address_id, client_id, is_default) VALUES (?, ?, ?)"
                data3 = (result,c_id,is_default)
                cursor.execute(insert_query3, data3)
            # 提交事务
            conn.commit()

    except Exception as e:
        print("插入出现异常！")
        # 出现异常时回滚事务
        conn.rollback()

