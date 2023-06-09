from flask import Blueprint, render_template, redirect, url_for, session
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
    user_id = session.get('client_id')
    if (user_id == None):
        return redirect(url_for("client.clientLogin"))
    if request.method == 'POST':
        nickname = request.form['nickname']
        key = request.form['key']
        message = request.form['message']
        # print(nickname)
        InsertMessageData(nickname, key, message,user_id)
    return render_template("contact.html")
