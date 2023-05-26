#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2023/5/26 23:49
# @Author  : Smalltown
# @FileName: client.py
# @Software: PyCharm
from flask import Blueprint

bp = Blueprint('client',__name__,url_prefix='/client')   #http://127.0.0.1/client

@bp.route('/login')
def clientLogin():
    pass
