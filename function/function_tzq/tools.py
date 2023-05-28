# -*- coding: utf-8 -*-

import pymssql
import shortuuid

import datetime

from flask import session

# server    数据库服务器名称或IP
# user      用户名
# password  密码
# database  数据库名称

server = "127.0.0.1"
user = "sa"
password = "tzqsgdmn"
database = "FlowerShop1"

# 连接数据库
conn = pymssql.connect(server, user, password, database, autocommit=True, charset='utf8')
cursor = conn.cursor()
if conn:
    print("数据库已连接成功")


# 新建表
def CreateTable(table_create, table_content):
    sql = "IF OBJECT_ID('" + table_create + "') IS NOT NULL DROP TABLE " + table_create + " CREATE TABLE " \
          + table_create + table_content
    cursor.execute(sql)
    # 提交当前事务,设置autocommit=True之后不用
    conn.commit()


# 批量插入数据
def InsertData(table_insert, value_insert, data_insert):
    sql = "INSERT INTO " + table_insert + " VALUES " + value_insert
    cursor.executemany(sql, data_insert)
    # 如果没有指定autocommit属性为True的话就需要调用commit()方法
    conn.commit()


# def messageRecord(nickname, key, message):
#     message_id = "m" + shortuuid.ShortUUID(alphabet='0123456789').random(length=7)
#     c_id = 'c1111111'
#     m_time = datetime.datetime.now().strftime("%Y-%m-%d")
#     return (message_id, c_id, message, m_time, key, nickname)


# def InsertMessageData(data_mes_insert1):
#     sql = "INSERT INTO message VALUES (%s, %s, %s, %s, %s, %s)"
#     cursor.executemany(sql, data_mes_insert1)
#     # 如果没有指定autocommit属性为True的话就需要调用commit()方法
#     conn.commit()


# 删除操作
def DeleteData(table_del, condition_del):
    sql = "delete " + table_del + " where " + condition_del
    cursor.execute(sql)
    conn.commit()


def DeleteMessageData(condition_mes_del):
    sql = "delete from message where client_id = " + condition_mes_del
    cursor.execute(sql)
    conn.commit()


# 修改操作
def UpdateData(table_up, result_up, condition_up):
    sql = "update [" + table_up + "] set " + result_up + " where " + condition_up
    cursor.execute(sql)
    conn.commit()


# 查询操作
def SelectTable(table_sel):
    sql = "SELECT * FROM " + table_sel
    # 执行查询语句
    cursor.execute(sql)
    # 获取所有的列名
    columns = [column[0] for column in cursor.description]
    row = cursor.fetchone()
    while row:
        print(f"{columns[0]}={row[0]}, {columns[1]}={row[1]}, {columns[2]}={row[2]}")
        row = cursor.fetchone()
    conn.commit()


# 补充与扩展
# 条件选择——可用于数据分析
def DataAnalyse(col_name, table_ana, condition_ana):
    sql = "SELECT " + col_name + " FROM " + table_ana + " WHERE " + condition_ana
    cursor.execute(sql)
    row = cursor.fetchone()
    # 获取所有的列名
    columns = [column[0] for column in cursor.description]
    while row:
        print(f"{columns[0]}={row[0]}, {columns[1]}={row[1]}, {columns[2]}={row[2]}")
        row = cursor.fetchone()
    conn.commit()


# 近一周热评
def DataMessageAnalyse():
    sql = "SELECT message_key, count(*) FROM message GROUP BY message_key"
    cursor.execute(sql)
    conn.commit()
    results = cursor.fetchall()
    columns = [column[0] for column in cursor.description]
    for row in results:
        print(f"{columns[0]}={row[0].encode('latin-1').decode('gbk')}, {columns[1]}={row[1]}")


# 近一周热卖
def DataOrderAnalyse():
    last_week = datetime.datetime.now().date() - datetime.timedelta(days=7)
    sql = f"SELECT orderInfo_flower_name, SUM(orderInfo_flowerNum) FROM orderInfo WHERE order_time >= '{last_week}' GROUP BY orderInfo_flower_name"
    # sql = "SELECT orderInfo_flower_name, SUM(orderInfo_flowerNum) FROM orderInfo GROUP BY orderInfo_flower_id"
    cursor.execute(sql)
    conn.commit()
    results = cursor.fetchall()
    columns = [column[0] for column in cursor.description]
    for row in results:
        print(f"{columns[0]}={row[0].encode('latin-1').decode('gbk')}, {columns[1]}={row[1]}")


# 排序
# 销量冠军/亟待降价销售
def OrderFlower(case):
    if case:
        sql = "SELECT flower_name,flower_sale FROM flower ORDER BY flower_sale DESC"
    else:
        sql = "SELECT flower_name,flower_num FROM flower ORDER BY flower_num DESC"
    cursor.execute(sql)
    row = cursor.fetchone()
    # 获取所有的列名
    columns = [column[0] for column in cursor.description]
    while row:
        print(f"{columns[0]}={row[0].encode('latin-1').decode('gbk')}, {columns[1]}={row[1]}")
        row = cursor.fetchone()
    conn.commit()


# 两表关联查询
def Order(col_select, ord_table, inner_table, condition_select):
    sql = "SELECT " + col_select + " FROM " + ord_table + " INNER JOIN " + inner_table + " ON " + condition_select
    cursor.execute(sql)
    row = cursor.fetchone()
    # 获取所有的列名
    columns = col_select
    while row:
        print(f"{columns[0]}={row[0]}, {columns[1]}={row[1]}, {columns[2]}={row[2]}")
        row = cursor.fetchone()
    conn.commit()


# 查询订单
def selectOrderInfo(order_id):
    sql = "SELECT * FROM orderInfo INNER JOIN [order] ON orderInfo.order_id = [order].order_id WHERE orderInfo.order_id=" + order_id
    cursor.execute(sql)
    row = cursor.fetchone()
    # 获取所有的列名
    columns = [column[0] for column in cursor.description]
    while row:
        row_dict = dict(zip(columns, row))
        for column in columns:
            if isinstance(row_dict[column], datetime.datetime):
                value = row_dict[column].strftime('%Y-%m-%d %H:%M:%S')  # 将日期时间转换为字符串
                encoded_value = value.encode('latin-1').decode('gbk')  # 进行编码转换
                print(f"{column}={encoded_value}")
            else:
                encoded_value = str(row_dict[column]).encode('latin-1').decode('gbk')  # 其他类型的列进行常规编码转换
                print(f"{column}={encoded_value}")
        row = cursor.fetchone()
    conn.commit()


#
# # 消息发布：对消息数据表进行数据插入
# # 应获取c_id, content, nickname, key
# def postMessage():
#     InsertMessageData(data_mes_insert)
#
#
# # 用户删除消息：对消息数据表进行删除
# def delMessage():
#     DeleteMessageData(condition_mes_del)
#
#
# def analyseFlower():
#     OrderFlower(case)
#     DataMessageAnalyse()
#     DataOrderAnalyse()
#
#
# def selOrder():
#     selectOrderInfo("'o1111111'")
#
#
# def postNotice():
#     InsertNoticeData(data_not_insert)
# 消息发布：对消息数据表进行数据插入
# 用户删除消息：对消息数据表进行删除
# 管理与删除消息：对消息数据表进行删除
# 管理员查询鲜花表的销量：对鲜花表进行查询
# 管理员词云生成：对消息表关键字进行查询


def InsertMessageData(nickname, key, message):
    message_id = "m" + shortuuid.ShortUUID(alphabet='0123456789').random(length=7)
    c_id = 'c1111111'
    m_time = datetime.datetime.now().strftime("%Y-%m-%d")
    sql = "INSERT INTO message VALUES (%s, %s, %s, %s, %s, %s)"
    data = (message_id, c_id, message, m_time, key, nickname)
    cursor.execute(sql, data)
    conn.commit()


def InsertNoticeData(title, content):
    sql = "INSERT INTO notice VALUES (%s, %s, %s, %s, %s)"
    notice_id = "n" + shortuuid.ShortUUID(alphabet='0123456789').random(length=7)
    manager_id = 'a1111111'
    n_time = datetime.datetime.now().strftime("%Y-%m-%d")
    data = (notice_id, manager_id, title, content, n_time)
    cursor.execute(sql, data)
    # 如果没有指定autocommit属性为True的话就需要调用commit()方法
    conn.commit()


def createMessageTuple():
    cursor.execute("SELECT * FROM message")
    rows = cursor.fetchall()
    unique_values = set()
    for row in rows:
        unique_values.add(row[4])
    unique_values = tuple(unique_values)
    encoded_tuple = tuple(
        item.encode('latin-1').decode('gbk') if isinstance(item, str) else item for item in unique_values)
    print(encoded_tuple)
    return encoded_tuple


def InsertFlowerData(flower_name, flower_mean, flower_imprice, flower_exprice, flower_num, flower_sale):
    flower_id = "f" + shortuuid.ShortUUID(alphabet='0123456789').random(length=7)
    session['flower_id'] = flower_id
    sql = "INSERT INTO flower VALUES (%s, %s, %s, %s, %s, %s, %s)"
    data = (flower_id, flower_name, flower_mean, flower_imprice, flower_exprice, flower_num, flower_sale)
    cursor.execute(sql, data)
    conn.commit()


def createFlowerTuple():
    cursor.execute("SELECT * FROM flower")
    rows = cursor.fetchall()
    unique_values = set()
    for row in rows:
        unique_values.add(row[1])
    unique_values = tuple(unique_values)
    encoded_tuple = tuple(
        item.encode('latin-1').decode('gbk') if isinstance(item, str) else item for item in unique_values)
    print(encoded_tuple)
    return encoded_tuple
