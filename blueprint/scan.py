#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2023/5/28 12:06
# @Author  : Smalltown
# @FileName: scan.py
# @Software: PyCharm
from flask import Blueprint, jsonify, render_template,session,redirect,url_for
from config import conn,cursor

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
            where    client_id=? '''
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