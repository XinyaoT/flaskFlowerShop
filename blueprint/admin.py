# -*- codeing = utf-8 -*-
# @Time : 2023/5/27 21:15
# @Author : Murphy_42
# @File : admin.py
# @Software : PyCharm


from flask import Blueprint, session
from flask import Flask,render_template
from flask import redirect
from flask import url_for
from flask import request
from function.function_xyn import clientLoginInAUp

bp = Blueprint('admin',__name__,url_prefix='/admin')   #http://127.0.0.1/admin

@bp.route("/client",method=['GET','POST'])
def showClient():
 pass