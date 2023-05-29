#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2023/5/26 21:16
# @Author  : Smalltown
# @FileName: clientShoppingcart.py
# @Software: PyCharm
from flask import Blueprint, session,redirect,url_for
import shortuuid
from function.function_txy.shopping.shoppingcart_utils import get_cartId,getShoppingcart_add_flower_num,updateShoppingcart_cartWholemoney,updateShoppingcart_add_flower_num,getShoppingcart_wholeMoneyNotadd
from function.function_txy.shopping import shoppingcart_func as shoppingFun
from config import conn,cursor
bp = Blueprint('clientShoppingcart',__name__,url_prefix='/client/shoppingcart')   #http://127.0.0.1/client/shoppingcart

@bp.route('/add/?flower_id=<flower_id>',methods= ['GET','POST'])
def addShppingcart(flower_id):

    '''前端接收用户传入的购物车数据，插入cart Info的表中,
                用户选择一种花就应该有一个购物车id，
                现在假设用户已经选择好了一种花，加入购物车'''

    print("现在你已经可以开始选购你喜欢的花朵了！\n")

    '''接受参数'''
    user_id = session.get('client_id')
    if (user_id == None):
        return redirect(url_for("client.clientLogin"))
    # 增加判断机制，是否是同一个商品
    iscart_id =get_cartId(cursor,flower_id)

    if (iscart_id==None):
        cart_id = "c" + shortuuid.ShortUUID(alphabet='0123456789').random(length=7)  # 自动分配cartID
        add_flower_num = 1
        wholemoney = shoppingFun.getWholeMoney(cursor=cursor, flower_id=flower_id)

        '''判断是否能加入购物车'''
        flag = shoppingFun.fun_can_add_or_not(cursor, flower_id, add_flower_num)

        # 不可以加入
        if flag == 1:
            messageNAK = "库存不足，请重新设置购买数量"
            print(messageNAK)
        # 可以加入
        else:
            # 更新shoppingcart flower表 contain表，对于flower表的sale应该在订单处更新
            shoppingFun.fun_addshoppingcart(cart_id=cart_id, user_id=user_id, flower_id=flower_id,
                                            wholemoney=wholemoney, add_flower_num=add_flower_num, cursor=cursor,
                                            conn=conn)
            messageACK = "现在你已经成功将此花加入你的购物车了！"
            print(messageACK, "\n")


    else:
        cart_id = get_cartId(cursor,flower_id)[0]
        add_flower_num = getShoppingcart_add_flower_num(cursor,cart_id) + 1
        print(getShoppingcart_add_flower_num(cursor,cart_id))
        print(add_flower_num)
        '''判断是否能加入购物车'''
        flag = shoppingFun.fun_can_add_or_not(cursor, flower_id, add_flower_num)

        # 不可以加入
        if flag == 1:
            messageNAK = "库存不足，请重新设置购买数量"
            print(messageNAK)
        # 可以加入
        else:
            wholemoney = add_flower_num * shoppingFun.getWholeMoney(cursor=cursor, flower_id=flower_id)
            shoppingFun.fun_updateShoppingcart(conn,cursor,wholemoney,cart_id,add_flower_num)
            shoppingFun.updateFlowerNum(conn,cursor,add_flower_num,flower_id)
    print(flower_id,user_id,cart_id,add_flower_num,wholemoney)
    '''点击+ 确认，'''

    return redirect(url_for('scan.get_flower'))





@bp.route('/modify?<cid>/?cart_id=<cart_id>/?flower_name=<flower_name>/?flower_id=<flower_id>',methods= ['GET','POST'])
def modifyShoppingcart(cid,cart_id,flower_name,flower_id):

    '''此模块描述当用户进入购物车的页面对于购物车的每一条信息进行  ++/--/删除'''
    print("你现在进入*我的购物车*当中了，你可以选择对自己购物车中的每一条记录进行++或--或者删除")

    match cid:
        case "2":
            print("你可以开始增加商品选购数量了！\n")
            add_num =getShoppingcart_add_flower_num(cursor,cart_id)+1
            cart_wholeMoney = add_num * shoppingFun.getWholeMoney(cursor,flower_id)
            dertaAdd = shoppingFun.fun_modifyAddShoppingcart(cursor=cursor, conn=conn, flower_id=flower_id,
                                                             add_num=add_num, cart_wholeMoney=cart_wholeMoney,
                                                             cart_id=cart_id)
            print("你现在已经成功添加了", dertaAdd, "个商品拉")
            return redirect(url_for("scan.get_shoppingcart"))

        case "1":

            print("你可以开始减少商品选购数量了！\n")
            dec_num = getShoppingcart_add_flower_num(cursor, cart_id) - 1
            if dec_num == 1:
                print("已经不能再减少了哟！\n")
            else:
                cart_wholeMoney = dec_num * shoppingFun.getWholeMoney(cursor, flower_id)
                dertaDec = shoppingFun.fun_modifyDecShoppingcart(cursor=cursor, conn=conn, flower_id=flower_id,
                                                                 dec_num=dec_num, cart_wholeMoney=cart_wholeMoney,
                                                                 cart_id=cart_id)
                print("你现在已经成功减少了", dertaDec, "个商品拉")
            return redirect(url_for("scan.get_shoppingcart"))

        case "3":
            print("你可以开始删除购物车信息拉！\n")
            shoppingFun.fun_modifyDeleShoppingcart(cursor=cursor, conn=conn, cart_id=cart_id, flower_id=flower_id)
            print("你删除了编号为", cart_id, "的购物信息")
            return redirect(url_for("scan.get_shoppingcart"))

