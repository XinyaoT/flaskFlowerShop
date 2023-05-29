#!/usr/bin/python3
# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, redirect, url_for,session
from flask import request

from function.function_tzq.tools import InsertMessageData

bp = Blueprint("message", __name__, url_prefix="/message")


@bp.route('/')
def load():
    return redirect(url_for('message.post'))


# 视图函数
@bp.route('/post', methods=['GET', 'POST'])
def post():

    # 传参方式
    # /post?message=xxxxxxx
    # return render_template("contact.html")
    if request.method == 'POST':
        print("hellp")
        nickname = request.form['nickname']
        key = request.form['key']
        message = request.form['message']
        # print(nickname)
        c_id = session.get("client_id")
        print(c_id)
        if (c_id == None):
            return redirect(url_for("client.clientLogin"))
        else:
            InsertMessageData(nickname, key, message,c_id)
    return render_template("contact.html")
