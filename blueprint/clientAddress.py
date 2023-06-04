#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2023/5/26 23:28
# @Author  : Smalltown
# @FileName: clientAddress.py
# @Software: PyCharm
from flask import Blueprint, session, render_template, redirect, url_for, request

from config import cursor
from function.function_xyn import addAddress

bp = Blueprint('clientAddress',__name__,url_prefix='/client/address')  #http://127.0.0.1/client/address/

@bp.route('/add',methods=['GET','POST'])
def addAddress_client():
    if request.method == 'POST':
        address = request.form['consignee_addr']
        user_id = session.get("client_id")
        if (user_id == None):
            return redirect(url_for("client.clientLogin"))
        print(user_id)
        addAddress.address_insert(user_id,address)
        return redirect(url_for('showAddress.showaddress'))
    return render_template('client-addressAdd.html')


# @bp.route('/add')
# def addAddress():
#     user_id = session.get("client_id")
#     sql =''' '''
#     cursor.execute(sql, user_id)
#
#     return user_id
@bp.route('/select',methods=['GET','POST'])
def selectAddress():

    user_id = session.get("client_id")
    sql='''SELECT  consignee_addr     --展示A表中的A1\A2字段和C表中的C1\C2
            FROM  has_c_a                         --中间表
            INNER JOIN address ON address.address_id =has_c_a.address_id   --A表中的与B表中相同的字段
            INNER JOIN client ON client.client_id = has_c_a.client_id    --C表中的与B表中相同的字段
            where    has_c_a.client_id=?'''
    cursor.execute(sql,user_id)
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
    return render_template("order.html",addresses=addresses)
        # redirect(url_for("clientOrders.addOrderInfo",addresses=addresses,results=results))
