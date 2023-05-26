#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2023/5/26 21:16
# @Author  : Smalltown
# @FileName: clientOrders.py
# @Software: PyCharm
from flask import Blueprint

bp = Blueprint('clientOrders',__name__,url_prefix='/client/orders')   #http://127.0.0.1/client/orders

@bp.route('/generate')
def generateOrders():
    pass
