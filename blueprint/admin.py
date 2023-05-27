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
from config import conn,cursor

bp = Blueprint('admin',__name__,url_prefix='/admin')   #http://127.0.0.1/admin

@bp.route("/client",methods=['GET','POST'])
def showClient():
  sql = "SELECT * FROM client"
  cursor.execute(sql)
  content = [tuple(item.encode('latin-1').decode('gbk') if isinstance(item, str) else item for item in row) for row in
             cursor.fetchall()]
  columns = [column[0] for column in cursor.description]
  print(columns)
  print(content)
  return render_template('admin-list.html', labels=columns, content=content)
