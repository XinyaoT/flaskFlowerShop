# -*- coding: utf-8 -*-

import pymssql
import shortuuid

import datetime

from flask import session

from config import cursor, conn


# server    数据库服务器名称或IP
# user      用户名
# password  密码
# database  数据库名称

# server = "127.0.0.1"
# user = "sa"
# password = "tzqsgdmn"
# database = "FlowerShop1"
#
# # 连接数据库
# conn = pymssql.connect(server, user, password, database, autocommit=True, charset='utf8')
# cursor = conn.cursor()
# if conn:
#     print("数据库已连接成功")


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
    results = cursor.fetchall()
    print(results)
    if len(results) > 0:
        first_row_first_column = results[0][0]
        return first_row_first_column
    else:
        return None  # 或返回默认值或进行适当的错误处理


# 近一周热卖
def DataOrderAnalyse():
    last_week = datetime.datetime.now().date() - datetime.timedelta(days=7)
    sql = f"SELECT orderInfo_flower_name, SUM(orderInfo_flowerNum) FROM orderInfo WHERE orderInfo_time >= '{last_week}' GROUP BY orderInfo_flower_name"
    cursor.execute(sql)
    results = cursor.fetchall()
    print(results)
    if len(results) > 0:
        first_row_first_column = results[0][0]
        return first_row_first_column
    else:
        return None  # 或返回默认值或进行适当的错误处理


# 排序
# 销量冠军/亟待降价销售
def OrderFlower(case):
    if case:
        sql = "SELECT flower_name,flower_sale FROM flower ORDER BY flower_sale DESC"
    else:
        sql = "SELECT flower_name,flower_num FROM flower ORDER BY flower_num DESC"
    cursor.execute(sql)
    row = cursor.fetchone()
    print(row[0])
    return row[0]
    # print("here")
    # # 获取所有的列名
    # columns = [column[0] for column in cursor.description]
    # while row:
    #     print(f"{columns[0]}={row[0].encode('gbk').decode('gbk')}, {columns[1]}={row[1]}")
    #     row = cursor.fetchone()
    # conn.commit()
    # print(columns[0])


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
                encoded_value = value.encode('gbk').decode('gbk')  # 进行编码转换
                print(f"{column}={encoded_value}")
            else:
                encoded_value = str(row_dict[column]).encode('gbk').decode('gbk')  # 其他类型的列进行常规编码转换
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


def InsertMessageData(nickname, key, message,c_id):
    message_id = "m" + shortuuid.ShortUUID(alphabet='0123456789').random(length=7)

    m_time = datetime.datetime.now().strftime("%Y-%m-%d")
    sql = "INSERT INTO message VALUES (?, ?, ?, ?, ?, ?)"
    data = (message_id, c_id, message, m_time, key, nickname)
    cursor.execute(sql, data)
    conn.commit()


def InsertNoticeData(title, content):
    sql = "INSERT INTO notice VALUES (?, ?, ?, ?, ?)"
    notice_id = "n" + shortuuid.ShortUUID(alphabet='0123456789').random(length=7)
    manager_id = 'a1111111'
    n_time = datetime.datetime.now().strftime("%Y-%m-%d")
    data = (notice_id, manager_id, title, content, n_time)
    print(data)
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
        item.encode('gbk').decode('gbk') if isinstance(item, str) else item for item in unique_values)
    print(encoded_tuple)
    return encoded_tuple


def InsertFlowerData(flower_name, flower_mean, flower_imprice, flower_exprice, flower_num, flower_sale):
    flower_id = "f" + shortuuid.ShortUUID(alphabet='0123456789').random(length=7)
    # session['flower_id'] = flower_id
    sql = "INSERT INTO flower VALUES (?, ?, ?, ?, ?, ?, ?)"
    data = (flower_id, flower_name, flower_mean, flower_imprice, flower_exprice, flower_num, flower_sale)
    cursor.execute(sql, data)
    conn.commit()
    return flower_id


def createFlowerTuple():
    cursor.execute("SELECT * FROM flower")
    rows = cursor.fetchall()
    unique_values = set()
    for row in rows:
        unique_values.add(row[1])
    unique_values = tuple(unique_values)
    encoded_tuple = tuple(
        item.encode('gbk').decode('gbk') if isinstance(item, str) else item for item in unique_values)
    print(encoded_tuple)
    return encoded_tuple


def createFlowerIDTuple():
    cursor.execute("SELECT * FROM flower")
    rows = cursor.fetchall()
    unique_values = set()
    for row in rows:
        unique_values.add(row[0])
    unique_values = tuple(unique_values)
    encoded_tuple = tuple(
        item.encode('gbk').decode('gbk') if isinstance(item, str) else item for item in unique_values)
    print(encoded_tuple)
    return encoded_tuple


def createClientTuple():
    cursor.execute("SELECT * FROM client")
    rows = cursor.fetchall()
    unique_values = set()
    for row in rows:
        unique_values.add(row[0])
    unique_values = tuple(unique_values)
    encoded_tuple = tuple(
        item.encode('gbk').decode('gbk') if isinstance(item, str) else item for item in unique_values)
    print(encoded_tuple)
    return encoded_tuple


def getFlowerBySort(flower_id):
    sql = "SELECT sort.sort_name FROM sort " \
          "JOIN belong ON sort.sort_id = belong.sort_id " \
          "JOIN flower ON belong.flower_id = flower.flower_id " \
          "WHERE flower.flower_id = ?"
    cursor.execute(sql, (flower_id,))

    # 获取查询结果
    results = cursor.fetchall()
    print("getFlowerBySort-results")
    print(results)

    # 将结果合并为字符串，并删除空格
    result_string = ', '.join([row[0].strip() for row in results])

    print("getFlowerBySort-result_string")
    print(result_string)

    return result_string


def getOrderInfoStatus(info):
    status = info[4]
    if status == '00':
        ret = '未处理'
    elif status == '01':
        ret = '已完成'
    elif status == '10':
        ret = '顾客申请取消'
    else:
        ret = '同意取消'
    return ret


def getOrderStatus(info):
    status = info[5]
    if status == '00':
        ret = '未处理'
    else:
        ret = '已处理'
    return ret


def updateOrderInfoStatus(orderInfo_id, status):
    # 执行 SQL 更新语句
    if status == '1':
        orderInfo_status = '00'
    elif status == '2':
        orderInfo_status = '01'
    elif status == '3':
        orderInfo_status = '10'
    else:
        orderInfo_status = '11'
    sql = f"UPDATE orderInfo SET [orderInfo_status] = '{orderInfo_status}' WHERE [orderInfo_id] = '{orderInfo_id}'"
    print(sql)
    cursor.execute(sql)
    sql = "SELECT [order_id] FROM orderInfo WHERE [orderInfo_id] = '{}'".format(orderInfo_id)
    print(sql)
    cursor.execute(sql)
    row = cursor.fetchone()
    if row:
        order_id = row[0]
        print(order_id)

    sql = "SELECT * FROM orderInfo WHERE [order_id] = ?"
    print(sql)
    cursor.execute(sql, (order_id,))
    # 获取查询结果
    results = cursor.fetchall()

    # 检查每条记录的orderInfo属性是否都不是"00"
    all_not_00 = all(result.orderInfo_status != "00" for result in results)

    # 输出检验结果
    if all_not_00 :
        print("所有记录的orderInfo属性都不是'00'")
        sql = f"UPDATE [order] SET [order_status] = '01' WHERE [order_id] = '{order_id}'"
        cursor.execute(sql)
        print("order_status已更新")


