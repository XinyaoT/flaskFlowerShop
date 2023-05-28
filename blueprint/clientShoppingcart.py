#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2023/5/26 21:16
# @Author  : Smalltown
# @FileName: clientShoppingcart.py
# @Software: PyCharm
from flask import Blueprint, request, session,redirect,url_for
import shortuuid
import pymssql
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
    # flower_name = request.form["flower_name"]
    user_id = session.get('client_id')
    cart_id = "c" + shortuuid.ShortUUID(alphabet='0123456789').random(length=7)  # 自动分配cartID
    add_flower_num = 1
    wholemoney = shoppingFun.getWholeMoney(cursor=cursor,flower_id=flower_id)
    print(flower_id,user_id,cart_id,add_flower_num,wholemoney)
    '''点击+ 确认，'''

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
                                        wholemoney=wholemoney, add_flower_num=add_flower_num, cursor=cursor, conn=conn)
        messageACK = "现在你已经成功将此花加入你的购物车了！"
        print(messageACK,"\n")

    return redirect(url_for('scan.get_flower'))





@bp.route('/modify',methods= ['GET','POST'])
def modifyShoppingcart():
    # # ###############################连接###########################################
    # conn = pymssql.connect(host="LAPTOP-D2INVD39", database='flower_shop_6', user='sa', password='123')
    # str = "连接失败！"
    # if conn:
    #     str = '连接成功！'
    #     # db.close() # 关闭连接，释放内存
    # print(str)  # 如果结果为连接成功即表示已经成功连接。
    # cursor = conn.cursor()
    # # ###############################连接###########################################

    '''此模块描述当用户进入购物车的页面对于购物车的每一条信息进行  ++/--/删除'''
    print("你现在进入*我的购物车*当中了，你可以选择对自己购物车中的每一条记录进行++或--或者删除")

    # lang = input("如果输入+，表示你想增加你选中的商品（你选中哪些是前端告诉我的）\n如果输入-，表示你想删减选中的商品（你选中哪些也是前端告诉我的）\n"
    #              "如果输入*删除*，那么你选中的这条记录会被删除\n:")
    lang = request.form.get("action")
    match lang:
        case "+":
            print("你可以开始增加商品选购数量了！\n")
            # flower_name = input("请告诉我你选择的商品名字：")
            # add_num = input("请告诉我，你增加后的数量：")  # 这里的限制操作前端来做,,
            # cart_wholeMoney = input("前端告诉我最后你提交的总价为：")
            # cart_id = input("前端告诉我你这条信息的cart_id为：")
            flower_name = request.form["flower_name"]
            add_num =request.form["add_num"]
            cart_wholeMoney = request.form["cart_wholeMoney"]
            cart_id = request.form["cart_id"]
            dertaAdd = shoppingFun.fun_modifyAddShoppingcart(cursor=cursor, conn=conn, flower_name=flower_name,
                                                             add_num=add_num, cart_wholeMoney=cart_wholeMoney,
                                                             cart_id=cart_id)
            print("你现在已经成功添加了", dertaAdd, "个商品拉")

        case "-":

            print("你可以开始减少商品选购数量了！\n")
            # flower_name = input("请告诉我你选择的商品名字：")
            # dec_num = input("请告诉我，你减少后的数量：")  # 这里的限制操作前端来做,,
            flower_name = request.form["flower_name"]
            dec_num = request.form["dec_num"]
            if dec_num == 1:
                print("已经不能再减少了哟！\n")
            else:
                # cart_wholeMoney = input("前端告诉我最后你提交的总价为：")
                # cart_id = input("前端告诉我你这条信息的cart_id为：")
                cart_wholeMoney = request.form["cart_wholeMoney"]
                cart_id = request.form["cart_id"]
                dertaDec = shoppingFun.fun_modifyDecShoppingcart(cursor=cursor, conn=conn, flower_name=flower_name,
                                                                 dec_num=dec_num, cart_wholeMoney=cart_wholeMoney,
                                                                 cart_id=cart_id)
                print("你现在已经成功减少了", dertaDec, "个商品拉")

        case "删除":

            print("你可以开始删除购物车信息拉！\n")
            # flower_name = input("请告诉我你选择的商品名字：")
            # cart_id = input("前端告诉我你这条信息的cart_id为：")
            flower_name = request.form["flower_name"]
            cart_id = request.form["cart_id"]
            shoppingFun.fun_modifyDeleShoppingcart(cursor=cursor, conn=conn, cart_id=cart_id, flower_name=flower_name)
            print("你删除了编号为", cart_id, "的购物信息")

    return "modifyShoopingcart"