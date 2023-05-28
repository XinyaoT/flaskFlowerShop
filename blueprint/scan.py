#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2023/5/28 12:06
# @Author  : Smalltown
# @FileName: scan.py
# @Software: PyCharm
from flask import Blueprint, jsonify, render_template,session
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
    sql = "select * from shoppingCart where client_id=%s"
    client_id = session.get('client_id')
    cursor.execute(sql,client_id)
    carts = cursor.fetchall()
    results = []
    for cart in carts:
        results.append({
            'id': cart[0],
            'imgs': '../static/images/g-10.png',
            'goodsInfo': '号地块健身房回复的科技示范户快速坚实的看了看大家发快递了很费劲的开始放假',
            'goodsParams': '四季度后付款的酸辣粉',
            'price': cart[2],
            'singleGoodsMoney': cart[3],

        })
    # print(results)
    results_json = jsonify(results)
    # return results
    return render_template('cart.html', results_json=results_json)