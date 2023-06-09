#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os

from flask import Flask, request, jsonify

from config import conn,cursor
import config
from blueprint.clientOrders import bp as orders_client_bp
from blueprint.clientAddress import bp as address_client_bp
from blueprint.clientShoppingcart import bp as shoppingcart_client_bp
from blueprint.admin import bp as admin_bp
from blueprint.message import bp as message_bp
from blueprint.client import bp as client_bp
from blueprint.scan import bp as scan_bp
from blueprint.query import bp as query_bp
from blueprint.manager import bp as manager_bp
from blueprint.showAddress import bp as showAddress_bp

from flask import Flask,render_template

from function.function_tzq.word import wordcloud

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

app.register_blueprint(showAddress_bp)
app.register_blueprint(orders_client_bp)
app.register_blueprint(address_client_bp)
app.register_blueprint(shoppingcart_client_bp)
app.register_blueprint(client_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(message_bp)
app.register_blueprint(scan_bp)
app.config.from_object(config)
app.register_blueprint(query_bp)
app.register_blueprint(manager_bp)


@app.route('/')
def index():
    sql = "select * from notice"
    cursor.execute(sql)
    notices = cursor.fetchall()
    print(notices)
    results = []
    for notice in notices:
        results.append({
            'notice_id': notice[0],
            'notice_title': notice[2],
            'notice_content': notice[3],
            'notice_time': notice[4],
        })
    # print(results.encode('utf-8').decode('utf-8'))
    # return results
    image_base64 = wordcloud()
    return render_template('index.html', results=results, initial_image_data=image_base64)



# def get_notice():
#     sql = "select * from notice"
#     cursor.execute(sql)
#     notices = cursor.fetchall()
#     print(notices)
#     results = []
#     for notice in notices:
#         results.append({
#             'notice_id': notice[0],
#             'notice_title': notice[2],
#             'notice_content': notice[3],
#             'notice_time': notice[4],
#             })
#     # print(results.encode('utf-8').decode('utf-8'))
#     #return results
#     return render_template('index.html', results=results)




if __name__ == '__main__':
    app.run(debug=True)
