#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2023/5/9 8:32
# @Author  : Smalltown
# @FileName: shoppingcart_utils.py
# @Software: PyCharm

def addClient (conn,cursor,data):
    sql = "INSERT INTO client (client_id,client_password,client_sex,client_phone,client_name) VALUES (%s,%s,%s,%s,%s)"
    cursor.execute(sql, data)
    conn.commit()


def addCart(conn,cursor,data):
    sql = "INSERT INTO shoppingCart (cart_id,client_id,cart_wholeMoney,add_flower_num) VALUES (%s,%s,%s,%d)"
    cursor.execute(sql,data)
    conn.commit()

def addContain(conn,cursor,data):
    sql = "INSERT INTO contain (cart_id,flower_id) VALUES (%s,%s)"
    cursor.execute(sql, data)
    conn.commit()

def updateFLower_flowernum(conn,cursor,data):
    sql = "update flower set flower_num=%d where flower_id = %s"
    cursor.execute(sql, data)
    conn.commit()

def updateFLower_flowersale(conn,cursor,data):
    sql = "update flower set flower_sale=%d where flower_id = %s"
    cursor.execute(sql, data)
    conn.commit()

def updateShoppingcart_cartWholemoney(conn,cursor,data):
    sql = "update shoppingCart set cart_wholeMoney=%s where cart_id = %s"
    cursor.execute(sql, data)
    conn.commit()

def updateShoppingcart_add_flower_num(conn,cursor,data):
    sql = "update shoppingCart set add_flower_num=%s where cart_id = %s"
    cursor.execute(sql, data)
    conn.commit()

def getFlower_flowernum(cursor,flower_id):
    sql_flower_num = "SELECT flower_num FROM flower where flower_id= %s "
    cursor.execute(sql_flower_num, flower_id)
    return cursor.fetchone()[0]

def getFlower_flowername(cursor,flower_id):
    sql_flower_id = "SELECT flower_name FROM flower where flower_id= %s "
    cursor.execute(sql_flower_id, flower_id)
    return cursor.fetchone()[0]

def getFlower_flowersale(cursor,flower_id):
    sql = "SELECT flower_sale FROM flower where flower_id= %s "
    cursor.execute(sql, flower_id)
    return cursor.fetchone()[0]

def getShoppingcart_add_flower_num(cursor,cart_id):
    sql = "SELECT add_flower_num FROM shoppingCart where cart_id= %s "
    cursor.execute(sql, cart_id)
    return cursor.fetchone()[0]

def getShoppingcart_wholeMoney(cursor,flower_id):
    sql = "SELECT flower_exPrice FROM flower where flower_id= %s "
    cursor.execute(sql, flower_id)
    return cursor.fetchone()[0]

def deleteContain(cursor, conn, data):
    sql = "DELETE FROM contain WHERE cart_id = %s and flower_id = %s"
    cursor.execute(sql, data)
    conn.commit()

def deleteShoppingcart(cursor, conn, cart_id):
    sql = "DELETE FROM shoppingCart WHERE cart_id = %s "
    cursor.execute(sql, cart_id)
    conn.commit()