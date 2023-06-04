# -*- codeing = utf-8 -*-
# @Time : 2023/6/1 0:39
# @Author : Murphy_42
# @File : showAddress.py
# @Software : PyCharm

from flask import Blueprint, render_template, redirect, url_for,session
from flask import request
import pymssql
from config import conn,cursor
from function.function_xyn import displayAddress


bp = Blueprint('showAddress',__name__,url_prefix='/client/address')  #http://127.0.0.1/client/address/

@bp.route('/show',methods=['GET','POST'])
def showaddress():
    addressId=displayAddress.get_clientAddress()
    results=[]
    for address in addressId:
        value=address
        select_query = "SELECT address_id, CONVERT(NVARCHAR(50), consignee_addr) AS 'nvarchar_column' FROM address WHERE address_id =?"
        data=(value,)
        cursor.execute(select_query,data)
        content = cursor.fetchall()
        results.append(content)
        print(results)

    columns = [row[0] for row in content]
    return render_template('addressShow.html', labels=columns, content=results)