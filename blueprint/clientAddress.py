#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2023/5/26 23:28
# @Author  : Smalltown
# @FileName: clientAddress.py
# @Software: PyCharm
from flask import Blueprint

bp = Blueprint('clientAddress',__name__,url_prefix='/client/address')  #http://127.0.0.1/client/address/

@bp.route('/add')
def addAddress():
    pass