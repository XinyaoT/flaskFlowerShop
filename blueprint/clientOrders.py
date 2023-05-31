#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2023/5/26 21:16
# @Author  : Smalltown
# @FileName: clientOrders.py
# @Software: PyCharm
import pymssql
from flask import Blueprint, request, session, render_template, redirect, url_for
import pyodbc as pyodbc
from function.function_txy.order import order_func as orderFun
from config import cursor, conn
from function.function_txy.shopping.shoppingcart_utils import updateCartStatus

bp = Blueprint('clientOrders', __name__, url_prefix='/client/orders')  # http://127.0.0.1/client/orders



@bp.route('/add', methods=['GET', 'POST'])
def addOrderInfo():
    user_id = session.get('client_id')
    if (user_id == None):
        return redirect(url_for("client.clientLogin"))
    ids = request.form.getlist('cartInfo')
    session['cartInfo'] = ids
    print(ids)
    ids_str = ",".join(ids)
    # print(ids)
    sql = '''SELECT  flower_name,flower_exPrice,cart_wholeMoney,add_flower_num,contain.cart_id     --展示A表中的A1\A2字段和C表中的C1\C2
            FROM  contain                         --中间表
            INNER JOIN flower ON flower.flower_id =contain.flower_id   --A表中的与B表中相同的字段
            INNER JOIN shoppingCart ON shoppingCart.cart_id = contain.cart_id    --C表中的与B表中相同的字段
            where    contain.cart_id=?  '''
    orders = []
    select_wholeMoney = 0
    for id in ids:
        cursor.execute(sql, id)
        order = cursor.fetchone()
        orders.append(order)
        select_wholeMoney = select_wholeMoney + order[2]
    print(select_wholeMoney)
    results = []
    for order in orders:
        results.append({
            'flower_name': order[0],
            'flower_exPrice': order[1],
            'cart_wholeMoney': order[2],
            'add_flower_num': order[3],
            'cart_id': order[4],
            'select_wholeMoney': select_wholeMoney
        })
        print(order)
        print(results[0]['select_wholeMoney'])
    # print(orders)

    print(results)
    return render_template("order.html", results=results, ids_str=ids_str, select_wholeMoney=select_wholeMoney)


@bp.route('/generate', methods=['GET', 'POST'])
def generateOrders():
    # print(ids)
    user_id = session.get('client_id')
    if (user_id == None):
        return redirect(url_for("client.clientLogin"))
    # 获取用户的购物车id信息
    # print("好了，你现在可以选择让购物车生成订单了\n")
    # cart_ids = request.form.getlist('ids_str')
    cart_ids = session.get('cartInfo')
    print('在这里')
    print(cart_ids)
    orderInfo_uuid = []

    results_str = request.form.get("results")
    num = results_str.count('{', 0, len(results_str))
    # print(num)
    # num = request.form["num"]   #购物车详情的数量 问
    client_id = session.get("client_id")

    # order_time = request.form["order_time"]  # 可以后端获取
    order_time = orderFun.get_date_time()
    order_price = request.form["select_wholeMoney"]

    order_addr = request.form["select-option"]  # 问

    order_bunched = request.form["selected_bunch"]
    print(num,client_id, order_time, order_addr, order_bunched,order_price)
    # 生成1条订单信息
    order_uuid = orderFun.addOrder_user(cursor, conn, client_id, order_price, order_time)

    # 同时生成多条订单详情信息，一条购物车详情对应一个，上面总共统计出有num个

    orderFun.addOrderInfo_user(cursor, conn, orderInfo_uuid, order_addr, order_bunched, cart_ids, order_uuid,
                               order_time, client_id, num)




    # 通过上述选择的购物车详情生成对应的订单详情信息

    # 最后返回订单页面进行渲染
    sql = '''select orderInfo_flower_name, orderInfo_flowerNum,orderInfo_addr,orderInfo_bunched,orderInfo_wholeMoney,orderInfo_status,orderInfo_id,orderInfo_time
    from orderInfo where cart_id=?'''
    orderInfos=[]
    for cart_id in cart_ids:
        cursor.execute(sql,cart_id)
        orderInfo=cursor.fetchone()
        orderInfos.append(orderInfo)
    results =[]
    for orderInfo in orderInfos:
        results.append({
            "flower_name":orderInfo[0],
            "orderInfo_flowerNum":orderInfo[1],
            "orderInfo_addr":orderInfo[2],
            "orderInfo_bunched":orderInfo[3],
            "orderInfo_wholeMoney":orderInfo[4],
            "orderInfo_status":orderInfo[5],
            'imgs': '/static/images/g-10.png',

            'orderInfo_id':orderInfo[6],
            'orderInfo_time':orderInfo[7]
        })
    print(results)
    return render_template("order_list_user.html",results=results)


@bp.route('/delete/?orderInfo_id=<orderInfo_id>')
def deleteOrders(orderInfo_id):
    user_id = session.get('client_id')
    if (user_id == None):
        return redirect(url_for("client.clientLogin"))


    # 取消订单申请
    orderFun.deleteOrderInfo_user(conn, cursor, orderInfo_id)
    return redirect(url_for("scan.get_orders"))