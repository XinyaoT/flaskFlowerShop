#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2023/5/26 23:49
# @Author  : Smalltown
# @FileName: client.py
# @Software: PyCharm

from flask import Blueprint, session
from flask import Flask,render_template
from flask import redirect
from flask import url_for
from flask import request
from function.function_xyn import clientLoginInAUp

bp = Blueprint('client',__name__,url_prefix='/client')   #http://127.0.0.1/client

@bp.route('/login', methods=['GET', 'POST'])
def clientLogin():
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'login':
            return user_login()
        elif action == 'register':
            return register()
    return render_template('login.html')

def user_login():
    if request.method=='POST':
        id=request.form['client_id']
        print(id)
        session['client_id']= id
        password=request.form['client_password']
        print(password)
        if clientLoginInAUp.client_null(id, password):
            login_massage = "温馨提示：账号和密码是必填"
            return render_template('login.html', message=login_massage)
        elif clientLoginInAUp.client_select(id, password):
            return render_template('index.html', username=id)
    return render_template('login.html')

def register():
    if request.method == 'POST':
        name = request.form['client_name']
        password = request.form['client_password']
        sex = request.form['client_sex']
        phone = request.form['client_phone']
        id = clientLoginInAUp.client_insert(password,sex,phone,name)
        session['client_id'] = id
        return render_template('index.html')
    return render_template('login.html')

