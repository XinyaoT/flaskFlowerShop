#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2023/5/26 21:16
# @Author  : Smalltown
# @FileName: clientShoppingcart.py
# @Software: PyCharm
from flask import Blueprint

bp = Blueprint('clientShoppingcart',__name__,url_prefix='/client/shoppingcart')   #http://127.0.0.1/client/shoppingcart

@bp.route('/add')
def addShoppingcart():
    return "addshoppingcart"