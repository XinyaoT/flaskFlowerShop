#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2023/5/12 21:57
# @Author  : Smalltown
# @FileName: shoppingcart_func.py
# @Software: PyCharm

import shoppingcart_utils as shopping

def fun_addshoppingcart(cart_id, user_id, flower_name, wholemoney, add_flower_num, cursor, conn):

    #          获取用户选择的花在flower表中的id
    flower_id = shopping.getFlower_flowerid(cursor, flower_name)

    #         获取flower表中原有的flower_num的值
    old_num = shopping.getFlower_flowernum(cursor, flower_id)

    #          计算出new_num的值
    new_num = int(old_num) - int(add_flower_num)

    #           新增一条购物车信息
    data2 = (cart_id, user_id, wholemoney, add_flower_num)
    shopping.addCart(conn=conn, cursor=cursor, data=data2)

    #           修改flower表中flower_num的值
    data3 = (new_num, flower_id)
    shopping.updateFLower_flowernum(conn=conn, cursor=cursor, data=data3)

    # #####################################dingdan####################################################
    # #           修改flower表中的flower_sale的值
    # data4 = (new_sale, flower_id)
    # shopping.updateFLower_flowersale(conn=conn, cursor=cursor, data=data4)
    # ########## # ###############################################################
    '''新增一条联系'''
    data5 = (cart_id, flower_id)
    shopping.addContain(conn=conn, cursor=cursor, data=data5)

def fun_can_add_or_not(cursor, flower_name, add_flower_num):
    #          获取用户选择的花在flower表中的id
    flower_id = shopping.getFlower_flowerid(cursor, flower_name)

    # # #######################test#################################################################
    # sql_flower_id = "SELECT Flower_id FROM flower where Flower_Name= %s"
    # cursor.execute(sql_flower_id, "玫瑰")
    # Flower_id = cursor.fetchone()[0]
    # print(Flower_id)
    # # #######################test#################################################################

    #         获取flower表中原有的flower_num的值
    old_num = shopping.getFlower_flowernum(cursor, flower_id)

    #          计算出new_num的值
    new_num = int(old_num) - int(add_flower_num)

    # # #########################dingdan ######################################
    # #           获取flower表中原有的flower_sale的值
    # old_sale = shopping.getFlower_flowersale(cursor, flower_id)
    #
    # #          计算出new_sale的值
    # new_sale = int(old_sale) + int(add_flower_num)
    # # ###############################################################

    if new_num<= 0:
        return 1
    else:
        return 0

def fun_modifyAddShoppingcart(cursor,conn, flower_name, add_num, cart_wholeMoney, cart_id):
    #     更新flower中的num
    flower_id = shopping.getFlower_flowerid(cursor=cursor, flower_name=flower_name)
    print(flower_id)
    old_cart_num = shopping.getShoppingcart_add_flower_num(cursor=cursor, cart_id=cart_id)
    print(old_cart_num)
    old_flower_num = shopping.getFlower_flowernum(cursor=cursor, flower_id=flower_id)
    print(old_flower_num)
    new_flower_num = int(old_flower_num) - int(add_num) + int(old_cart_num)
    print(new_flower_num)
    data3 = (new_flower_num, flower_id)
    shopping.updateFLower_flowernum(conn=conn, cursor=cursor, data=data3)

#     更新cart中的wholemoney addflowernum


    data1 = (cart_wholeMoney, cart_id)
    shopping.updateShoppingcart_cartWholemoney(conn=conn, cursor=cursor, data=data1)

    data2 = (add_num, cart_id)
    shopping.updateShoppingcart_add_flower_num(conn=conn, cursor=cursor, data=data2)
    return int(add_num) - int(old_cart_num)


def fun_modifyDecShoppingcart(cursor,conn, flower_name, dec_num, cart_wholeMoney, cart_id):
    #     更新flower中的num
    flower_id = shopping.getFlower_flowerid(cursor=cursor, flower_name=flower_name)
    print(flower_id)

    old_cart_num = shopping.getShoppingcart_add_flower_num(cursor=cursor, cart_id=cart_id)
    print(old_cart_num)

    old_flower_num = shopping.getFlower_flowernum(cursor=cursor, flower_id=flower_id)
    print(old_flower_num)

    new_flower_num = int(old_flower_num) - int(dec_num) + int(old_cart_num)
    print(new_flower_num)
    data3 = (new_flower_num, flower_id)
    shopping.updateFLower_flowernum(conn=conn, cursor=cursor, data=data3)

#     更新cart中的wholemoney addflowernum


    data1 = (cart_wholeMoney, cart_id)
    shopping.updateShoppingcart_cartWholemoney(conn=conn, cursor=cursor, data=data1)

    data2 = (dec_num, cart_id)
    shopping.updateShoppingcart_add_flower_num(conn=conn, cursor=cursor, data=data2)
    return int(old_cart_num) - int(dec_num)


def fun_modifyDeleShoppingcart(cursor, conn, cart_id, flower_name):
    flower_id = shopping.getFlower_flowerid(cursor=cursor, flower_name=flower_name)
    data = (cart_id, flower_id)

    # 更新花表的num
    flower_id = shopping.getFlower_flowerid(cursor=cursor, flower_name=flower_name)
    print(flower_id)

    old_cart_num = shopping.getShoppingcart_add_flower_num(cursor=cursor, cart_id=cart_id)
    print(old_cart_num)

    old_flower_num = shopping.getFlower_flowernum(cursor=cursor, flower_id=flower_id)
    print(old_flower_num)

    new_flower_num = int(old_flower_num) + int(old_cart_num)
    print(new_flower_num)

    data3 = (new_flower_num, flower_id)
    shopping.updateFLower_flowernum(conn=conn, cursor=cursor, data=data3)

    # 删除联系
    shopping.deleteContain(cursor=cursor, conn=conn, data=data)

    # 删除购物车信息
    shopping.deleteShoppingcart(cursor=cursor, conn=conn, cart_id=cart_id)