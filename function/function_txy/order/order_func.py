#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2023/5/15 19:23
# @Author  : Smalltown
# @FileName: order_func.py
# @Software: PyCharm


import shortuuid
import function.function_txy.order.order_utils as order
import function.function_txy.shopping.shoppingcart_utils as shopping
import time


def adminDeleteTheOrder():
    print("pass")


def deleteOrderInfo_user(conn, cursor, orderInfo):

    order.updateOderInfoStatus(conn=conn, cursor=cursor, orderInfo_id=orderInfo)

    print("取消订单的信息已同步给管理员")


def addOrder_user(cursor, conn, client_id, order_price, order_time):
    order_uuid = "or" + shortuuid.ShortUUID(alphabet='0123456789').random(length=6)
    print(order_uuid)
    data1 = (order_uuid, client_id, order_price, order_time)
    order.addOrder(conn=conn, cursor=cursor, data=data1)
    return order_uuid


def addOrderInfo_user(cursor, conn, orderInfo_uuid, order_addr, order_bunched, cart_info, order_uuid, order_time,
                      client_id, num):
    for i in range(0, num ):
        print(i)
        orderInfo_uuid.append("oi" + shortuuid.ShortUUID(alphabet='0123456789').random(length=6))
        print(orderInfo_uuid)
        orderInfo_flower_id = order.getOrderInfo_flower_id(cursor=cursor, cart_id=cart_info[i])
        orderInfo_flower_name = order.getOrderInfo_flower_name(cursor=cursor, flower_id=orderInfo_flower_id)
        print(orderInfo_flower_name)
        orderInfo_flowerNum = int(order.getOrderInfo_flowerNum(cursor=cursor, cart_id=cart_info[i]))
        orderInfo_whole_money = order.getOrderInfo_wholeMoney(cursor=cursor, cart_id=cart_info[i])
        orderInfo_addr = order_addr
        orderInfo_bunched = order_bunched
        orderInfo_clientId = client_id

        data = (orderInfo_uuid[i], cart_info[i], order_uuid, order_time,"00", orderInfo_flower_id, orderInfo_flower_name,
                orderInfo_flowerNum, orderInfo_whole_money, orderInfo_addr, orderInfo_bunched, orderInfo_clientId)
        print(data)
        order.addOrderInfo(conn=conn, cursor=cursor, data=data)
        # 更新花的销量
        order.updateFlowerSale(conn=conn, cursor=cursor, flower_id=orderInfo_flower_id,
                               orderInfo_flowerNum=orderInfo_flowerNum)
        # 更新购物车的记录
        for j in range(0, num):
            shopping.updateCartStatus(conn, cursor, cart_info[j])

        # # 删除购物车记录
        # for j in range(0, num):
        #     # 删除联系
        #     shopping.deleteContain(cursor=cursor, conn=conn, data=(cart_info[j],orderInfo_flower_id))
        #
        #     # # 删除购物车信息
        #     # shopping.deleteShoppingcart(cursor=cursor, conn=conn, cart_id=cart_info[j])

def get_date_time():
    t = time.localtime()
    t_s = "{}-{}-{} {}:{}:{}".format(t.tm_year, t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min, t.tm_sec)
    return t_s
