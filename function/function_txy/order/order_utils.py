#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2023/5/15 19:24
# @Author  : Smalltown
# @FileName: order_utils.py
# @Software: PyCharm

def addOrderInfo(conn,cursor,data):
    # sql = "INSERT INTO orderInfo (orderInfo_id,cart_id," \
    #       "order_id,orderInfo_time," \
    #       "orderInfo_flower_id," \
    #       "orderInfo_flower_name," \
    #       "orderInfo_flowerNum,orderInfo_wholeMoney," \
    #       "orderInfo_addr,orderInfo_bunched,orderInfo_clientId) VALUES (%s,%s,%s,%s,%s,%s,%d,%s,%s,%s,%s)"
    sql = "INSERT INTO orderInfo (orderInfo_id,cart_id," \
          "order_id,orderInfo_time," \
          "orderInfo_status,orderInfo_flower_id," \
          "orderInfo_flower_name," \
          "orderInfo_flowerNum,orderInfo_wholeMoney," \
          "orderInfo_addr,orderInfo_bunched,orderInfo_clientId) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)"

    # # 处理非UTF-8字符的解码
    # decoded_data = []
    # for item in data:
    #     if isinstance(item, bytes):
    #         try:
    #             decoded_item = item.decode('utf-8')
    #         except UnicodeDecodeError:
    #             # 使用其他编码进行解码
    #             decoded_item = item.decode('gbk', errors='replace')
    #     else:
    #         decoded_item = item
    #     decoded_data.append(decoded_item)
    #     decoded_data1 = tuple(decoded_data)
    cursor.execute(sql,data)
    conn.commit()

def addOrder(conn,cursor,data):
    # sql = "INSERT INTO [order](order_id,client_id," \
    #       "order_price," \
    #       "order_time) VALUES (%s,%s,%s,%s)"
    sql = "INSERT INTO [order](order_id,client_id," \
          "order_price," \
          "order_time) VALUES (?,?,?,?)"
    cursor.execute(sql,data)
    conn.commit()

def getOrderInfo_flower_id(cursor,cart_id):
    # sql = "SELECT flower_id FROM contain where cart_id= %s "
    sql = "SELECT flower_id FROM contain where cart_id= ? "
    cursor.execute(sql, cart_id)
    return cursor.fetchone()[0]

def getOrderInfo_flower_name(cursor,flower_id):
    # sql = "SELECT flower_name FROM flower where flower_id= %s "
    sql = "SELECT flower_name FROM flower where flower_id= ? "
    cursor.execute(sql, flower_id)
    return cursor.fetchone()[0]

def getOrderInfo_flowerNum(cursor,cart_id):
    # sql = "SELECT add_flower_num FROM shoppingCart where cart_id= %s "
    sql = "SELECT add_flower_num FROM shoppingCart where cart_id= ? "
    cursor.execute(sql, cart_id)
    return cursor.fetchone()[0]

def getOrderInfo_wholeMoney(cursor,cart_id):
    # sql = "SELECT cart_wholeMoney FROM shoppingCart where cart_id= %s "
    sql = "SELECT cart_wholeMoney FROM shoppingCart where cart_id= ? "
    cursor.execute(sql, cart_id)
    return cursor.fetchone()[0]

# def getAddress_id(cursor,client_id):
#     sql = "select client_id,address_id from has_c_a where client_id =%s "
#     cursor.execute(sql, client_id)
#     return cursor.fetchall()[0]
def getIsOrderInfo_orderInfoId(cursor,order_id):
    # sql = "SELECT orderInfo_id FROM orderInfo where order_id= %s "
    sql = "SELECT orderInfo_id FROM orderInfo where order_id= ? "
    cursor.execute(sql, order_id)

    return len(cursor.fetchall())

def getOrderInfo_orderId(cursor,orderInfo_id):
    # sql = "SELECT order_id FROM orderInfo where orderInfo_id= %s "
    sql = "SELECT order_id FROM orderInfo where orderInfo_id= ? "
    cursor.execute(sql, orderInfo_id)
    return cursor.fetchone()[0]

def deleteOrderInfo(cursor, conn, data):
    # sql = "DELETE FROM orderInfo WHERE orderInfo_id = %s "
    sql = "DELETE FROM orderInfo WHERE orderInfo_id = ? "
    cursor.execute(sql, data)
    conn.commit()

def deleteOrder(cursor, conn, data):
    # sql = "DELETE FROM [order] WHERE order_id = %s "
    sql = "DELETE FROM [order] WHERE order_id = ? "
    cursor.execute(sql, data)
    conn.commit()

def deleteShoppingCart(cursor, conn, cart_id):
    # sql = "DELETE FROM [order] WHERE order_id = %s "
    sql1 = "DELETE FROM shoppingCart WHERE cart_id = ? "
    cursor.execute(sql1, cart_id)
    conn.commit()
    sql2 =""
def updateOderInfoStatus(conn,cursor,orderInfo_id):
    # sql = "update orderInfo set orderInfo_status='11' where orderInfo_id = %s"
    sql = "update orderInfo set orderInfo_status='10' where orderInfo_id = ?"
    cursor.execute(sql, orderInfo_id)
    conn.commit()


def updateFlowerSale(conn,cursor,flower_id,orderInfo_flowerNum):
    sql1 = "select flower_sale from flower where flower_id =?"
    cursor.execute(sql1, flower_id)
    sale = int(cursor.fetchone()[0])+orderInfo_flowerNum
    sql = "update flower set flower_sale=? where flower_id = ?"
    cursor.execute(sql, (sale,flower_id))
    conn.commit()

