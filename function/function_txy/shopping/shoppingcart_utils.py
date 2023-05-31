#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2023/5/9 8:32
# @Author  : Smalltown
# @FileName: shoppingcart_utils.py
# @Software: PyCharm

def addClient (conn,cursor,data):
    sql = "INSERT INTO client (client_id,client_password,client_sex,client_phone,client_name) VALUES (?,?,?,?,?)"
    cursor.execute(sql, data)
    conn.commit()


def addCart(conn,cursor,data):
    sql = "INSERT INTO shoppingCart (cart_id,client_id,cart_wholeMoney,add_flower_num,cart_status) VALUES (?,?,?,?,?)"
    cursor.execute(sql,data)
    conn.commit()

def addContain(conn,cursor,data):
    sql = "INSERT INTO contain (cart_id,flower_id) VALUES (?,?)"
    cursor.execute(sql, data)
    conn.commit()

def updateCartStatus(conn,cursor,cart_id):
    sql = "update shoppingCart set cart_status='1' where cart_id = ?"
    cursor.execute(sql, cart_id)
    conn.commit()

def getCartStatus(cursor,cart_id):
    sql = "SELECT cart_status FROM shoppingCart where cart_id= ?"
    cursor.execute(sql, cart_id)
    return cursor.fetchone()[0]

def updateFLower_flowernum(conn,cursor,data):
    sql = "update flower set flower_num=? where flower_id = ?"
    cursor.execute(sql, data)
    conn.commit()

def updateFLower_flowersale(conn,cursor,data):
    sql = "update flower set flower_sale=? where flower_id = ?"
    cursor.execute(sql, data)
    conn.commit()

def updateShoppingcart_cartWholemoney(conn,cursor,data):
    sql = "update shoppingCart set cart_wholeMoney=? where cart_id = ?"
    cursor.execute(sql, data)
    conn.commit()

def updateShoppingcart_add_flower_num(conn,cursor,data):
    sql = "update shoppingCart set add_flower_num=? where cart_id =?"
    cursor.execute(sql, data)
    conn.commit()

def getFlower_flowernum(cursor,flower_id):
    sql_flower_num = "SELECT flower_num FROM flower where flower_id= ? "
    cursor.execute(sql_flower_num, flower_id)
    return cursor.fetchone()[0]

def getFlower_flowername(cursor,flower_id):
    sql_flower_id = "SELECT flower_name FROM flower where flower_id= ? "
    cursor.execute(sql_flower_id, flower_id)
    return cursor.fetchone()[0]

def getFlower_flowersale(cursor,flower_id):
    sql = "SELECT flower_sale FROM flower where flower_id= ?"
    cursor.execute(sql, flower_id)
    return cursor.fetchone()[0]

def getShoppingcart_add_flower_num(cursor,cart_id):
    sql = "SELECT add_flower_num FROM shoppingCart where cart_id= ?  "
    cursor.execute(sql, cart_id)
    return cursor.fetchone()[0]

def getShoppingcart_wholeMoneyNotadd(cursor,cart_id):
    sql = "SELECT cart_wholeMoney FROM shoppingCart where cart_id= ? "
    cursor.execute(sql, cart_id)
    return cursor.fetchone()[0]
def getShoppingcart_wholeMoney(cursor,flower_id):
    sql = "SELECT flower_exPrice FROM flower where flower_id= ? "
    cursor.execute(sql, flower_id)
    return cursor.fetchone()[0]

def deleteContain(cursor, conn, data):
    sql = "DELETE FROM contain WHERE cart_id = ? and flower_id = ?"
    cursor.execute(sql, data)
    conn.commit()

def deleteShoppingcart(cursor, conn, cart_id):
    sql = "DELETE FROM shoppingCart WHERE cart_id = ? "
    cursor.execute(sql, cart_id)
    conn.commit()


def get_cartId(cursor,flower_id):
    sql = '''select cart_id from contain where flower_id=?'''
    cursor.execute(sql, flower_id)
    return cursor.fetchone()