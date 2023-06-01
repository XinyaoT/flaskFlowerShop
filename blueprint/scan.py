#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2023/5/28 12:06
# @Author  : Smalltown
# @FileName: scan.py
# @Software: PyCharm
from flask import Blueprint, jsonify, render_template,session,redirect,url_for

from flaskFlowerShop.config import cursor

bp = Blueprint('scan',__name__,url_prefix='/scan')  #http://127.0.0.1/client/address/

@bp.route('/flower')
def get_flower():
    sql = "select * from flower"
    cursor.execute(sql)
    flowers = cursor.fetchall()
    products = []
    for flower in flowers:
        products.append({
            'flower_id': flower[0],
            'flower_name': flower[1],
            'flower_mean': flower[2],
            'flower_imPrice': flower[3],
            'flower_exPrice': flower[4],
            'flower_num': flower[5],
            'flower_sale': flower[6],
            'imgs':  [
                {'src': '../static/images/g-1.jpg'},
                {'src': '../static/images/g-2.jpg'},
                {'src': '../static/images/g-3.jpg'},
                {'src': '../static/images/g-4.jpg'},
                {'src': '../static/images/g-5.jpg'},
                {'src': '../static/images/g-6.jpg'},
                {'src': '../static/images/g-7.jpg'},
                {'src': '../static/images/g-8.jpg'},
                {'src': '../static/images/g-9.png'},
                {'src': '../static/images/g-10.png'}
            ]
        })

    # products = jsonify(result)
    # print(products)
    return render_template('scan.html', products=products )


@bp.route('/shoppingcart')
def get_shoppingcart():
    sql = '''SELECT  flower_name,flower_exPrice,cart_wholeMoney,add_flower_num,contain.cart_id,contain.flower_id     --展示A表中的A1\A2字段和C表中的C1\C2
            FROM  contain                         --中间表
            INNER JOIN flower ON flower.flower_id =contain.flower_id   --A表中的与B表中相同的字段
            INNER JOIN shoppingCart ON shoppingCart.cart_id = contain.cart_id    --C表中的与B表中相同的字段
            where    client_id=? and cart_status='0' '''
    client_id = session.get('client_id')
    print(client_id)
    if(client_id ==None):
        return redirect(url_for("client.clientLogin"))
    cursor.execute(sql,client_id)
    carts = cursor.fetchall()
    i=0
    wholeMoney = 0
    results = []
    for cart in carts:
        i = i+1
        results.append({
            'flower_name': cart[0],
            'imgs': '../static/images/g-10.png',
            'flower_exPrice': cart[1],
            'cart_wholeMoney': cart[2],
            'add_flower_num': cart[3],
            'cart_id': cart[4],
            'flower_id': cart[5]
        })
    for j in range(0,i):
        wholeMoney = wholeMoney + results[j]['cart_wholeMoney']
    print(results)
    print(wholeMoney)
    # return results
    return render_template('cart.html', results=results,wholeMoney=wholeMoney)


# @bp.route('/orderInfo')
# def get_order_info():
#     sql = "select * from orderInfo"
#     cursor.execute(sql)
#     orderInfos = cursor.fetchall()
#     results = []
#     for orderInfo in orderInfos:
#         results.append({
#             'orderInfo_id': orderInfo[0],
#             'cart_id': orderInfo[1],
#             'order_id': orderInfo[2],
#             'orderInfo_time': orderInfo[3],
#             'orderInfo_status': orderInfo[4],
#             'orderInfo_flower_id': orderInfo[5],
#             'orderInfo_flower_name': orderInfo[6],
#             'orderInfo_flowerNum':orderInfo[7],
#             'orderInfo_wholeMoney':orderInfo[8],
#             'orderInfo_addr':orderInfo[9],
#             'orderInfo_bunched':orderInfo[10],
#             'orderInfo_client_id':orderInfo[11]
#
#
#         })
#
#     # products = jsonify(result)
#     # print(products)
#     return render_template('over-view.html', results=results )
#
#
# @bp.route('/order')
# def get_order():
#     sql = "select * from [order]"
#     cursor.execute(sql)
#     orders = cursor.fetchall()
#     results = []
#     for order in orders:
#         results.append({
#             'order_id': order[0],
#             'client_id': order[1],
#             'order_purchaseMethod': order[2],
#             'order_price': order[3],
#             'order_time': order[4],
#             'order_status': order[5],
#
#         })
#
#     # products = jsonify(result)
#     # print(products)
#     return render_template('order-list.html', results=results )

@bp.route('/selectaddr',methods=['GET','POST'])
def selectAddress():
    if (session.get("client_id")==None):
        user_id ='u0001'
    else:
        user_id = session.get("client_id")
    sql='''SELECT  consignee_addr     --展示A表中的A1\A2字段和C表中的C1\C2
            FROM  has_c_a                         --中间表
            INNER JOIN address ON address.address_id =has_c_a.address_id   --A表中的与B表中相同的字段
            INNER JOIN client ON client.client_id = has_c_a.client_id    --C表中的与B表中相同的字段
            where    has_c_a.client_id=?'''
    cursor.execute(sql,user_id)
    # cursor.execute(sql, 'u0001')
    addrs = cursor.fetchall()
    print(addrs)
    addresses =[]
    for addr in addrs:
        addresses.append(
            addr[0]
        )
        print(addr)
    print(addresses)

    # ids = session.get("cartInfo")
    # print(ids)
    # sql2 = '''SELECT  flower_name,flower_exPrice,cart_wholeMoney,add_flower_num,contain.cart_id     --展示A表中的A1\A2字段和C表中的C1\C2
    #             FROM  contain                         --中间表
    #             INNER JOIN flower ON flower.flower_id =contain.flower_id   --A表中的与B表中相同的字段
    #             INNER JOIN shoppingCart ON shoppingCart.cart_id = contain.cart_id    --C表中的与B表中相同的字段
    #             where    contain.cart_id=?  '''
    # orders = []
    # for id in ids:
    #     cursor.execute(sql2, id)
    #     order = cursor.fetchone()
    #     orders.append(order)
    # results = []
    # for order in orders:
    #     results.append({
    #         'flower_name': order[0],
    #         'flower_exPrice': order[1],
    #         'cart_wholeMoney': order[2],
    #         'add_flower_num': order[3],
    #         'cart_id': order[4]
    #     })
    return jsonify(addresses)
        # render_template("order.html",addresses=addresses)
        # redirect(url_for("clientOrders.addOrderInfo",addresses=addresses,results=results))


@bp.route('/orders')
def get_orders():
    if (session.get("client_id") == None):
        user_id = 'u0001'
    else:
        user_id = session.get("client_id")
    # 最后返回订单页面进行渲染
    sql = '''select orderInfo_flower_name, orderInfo_flowerNum,orderInfo_addr,orderInfo_bunched,orderInfo_wholeMoney,orderInfo_status,orderInfo_id,orderInfo_time
       from orderInfo where orderInfo_clientId=?'''

    cursor.execute(sql, user_id)
    orderInfos = cursor.fetchall()
    results = []
    for orderInfo in orderInfos:
        results.append({
            "flower_name": orderInfo[0],
            "orderInfo_flowerNum": orderInfo[1],
            "orderInfo_addr": orderInfo[2],
            "orderInfo_bunched": orderInfo[3],
            "orderInfo_wholeMoney": orderInfo[4],
            "orderInfo_status": orderInfo[5],
            'imgs': '/static/images/g-10.png',

            'orderInfo_id': orderInfo[6],
            'orderInfo_time': orderInfo[7]
        })
    print(results)
    return render_template("order_list_user_whole.html", results=results)