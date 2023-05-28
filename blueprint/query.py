from flask import Blueprint, render_template, redirect, url_for
from flask import request

from function.function_tzq.tools import InsertMessageData, cursor, createFlowerTuple, InsertFlowerData, \
    createMessageTuple

bp = Blueprint("query", __name__, url_prefix="/query")


@bp.route('/message', methods=['GET', 'POST'])
def queryMessage():
    if request.method == 'POST':
        keyword = request.form['keyword']
        # print(keyword)
        keywords = createMessageTuple()
        # print(keyword)
        # print(keywords)
        for item in keywords:
            if item == keyword:
                sql = "SELECT * FROM message WHERE message_key='" + keyword + "'"
                # print("true")
                cursor.execute(sql)
                content = [
                    tuple(item.encode('latin-1').decode('gbk') if isinstance(item, str) else item for item in row) for
                    row in cursor.fetchall()]
                columns = [column[0] for column in cursor.description]
                return render_template('message.html', labels=columns, content=content)
                break
    sql = "SELECT * FROM message"
    cursor.execute(sql)
    content = [tuple(item.encode('latin-1').decode('gbk') if isinstance(item, str) else item for item in row) for row in
               cursor.fetchall()]
    columns = [column[0] for column in cursor.description]
    # print(columns)
    # print(content)
    return render_template('message.html', labels=columns, content=content)





@bp.route('/flower', methods=['GET', 'POST'])
def queryFlower():
    if request.method == 'GET':
        print("OK")
        action = request.args.get('action')
        print(action)
        if action == 'add':
            return redirect(url_for('manager.addFlower', _external=True))
        else:
            return redirect(url_for('manager.deleteFlower'))
    sql = "SELECT * FROM flower"
    cursor.execute(sql)
    content = [tuple(item.encode('latin-1').decode('gbk') if isinstance(item, str) else item for item in row) for row in
               cursor.fetchall()]
    columns = [column[0] for column in cursor.description]
    print(columns)
    print(content)
    return render_template('flower-list.html', labels=columns, content=content)
    # return render_template('flower-list.html')

# @bp.route('/notice', methods=['GET', 'POST'])
# def queryNotice():
#     sql = "SELECT * FROM notice"
#     cursor.execute(sql)
#     content = [tuple(item.encode('latin-1').decode('gbk') if isinstance(item, str) else item for item in row) for row in
#                cursor.fetchall()]
#     columns = [column[0] for column in cursor.description]
#     # print(columns)
#     # print(content)
#     return render_template('message.html', labels=columns, content=content)
