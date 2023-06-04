# -*- codeing = utf-8 -*-
# @Time : 2023/6/2 15:57
# @Author : Murphy_42
# @File : displayAddress.py
# @Software : PyCharm

from flask import Blueprint, render_template, redirect, url_for,session
from flask import request
import pymssql
from config import conn,cursor

def get_clientAddress():
    user_id = session.get("client_id")
    select_query = "SELECT * FROM has_c_a WHERE client_id = ?"
    data = (user_id,)
    cursor.execute(select_query,data)
    result = cursor.fetchall()

    address = []
    for tuple in result:
        addressId = tuple[0]
        address.append(addressId)
    return address