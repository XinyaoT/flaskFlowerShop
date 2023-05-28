from flask import Blueprint, render_template, request

from config import cursor, conn
from function.function_tzq.tools import InsertNoticeData, createFlowerTuple, InsertFlowerData

bp = Blueprint("manager", __name__, url_prefix="/manager")


@bp.route("/analyse/message")
def DataMessageAnalyse():
    # sql = "SELECT message_key, count(*) FROM message GROUP BY message_key"
    # cursor.execute(sql)
    # conn.commit()
    # results = cursor.fetchall()
    # columns = [column[0] for column in cursor.description]
    # for row in results:
    #     print(f"{columns[0]}={row[0].encode('latin-1').decode('gbk')}, {columns[1]}={row[1]}")
    return render_template("admin-add.html")


@bp.route('/notice', methods=['GET', 'POST'])
def notice():
    # 传参方式
    # /post?message=xxxxxxx
    # return render_template("contact.html")
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        # print(title)
        InsertNoticeData(title, content)
    return render_template("notice.html")


@bp.route('/delmessage', methods=['GET', 'POST'])
def delMessage():
    if request.method == 'POST':
        # print("OK")
        argument = request.form.get('id')
        # print(argument)
        sql = "delete from message where message_id='" + argument + "'"
        # print(sql)
        cursor.execute(sql)
    sql = "SELECT * FROM message"
    cursor.execute(sql)
    content = [tuple(item.encode('latin-1').decode('gbk') if isinstance(item, str) else item for item in row) for
               row in
               cursor.fetchall()]
    columns = [column[0] for column in cursor.description]
    # print(columns)
    # print(content)
    return render_template('message.html', labels=columns, content=content)


@bp.route('/addflower/?id=<id>', methods=['GET', 'POST'])
def addFlower(id):
    if request.method == 'POST':
        flower_name = request.form['flower_name']
        flower_names = createFlowerTuple()
        print(flower_names)
        print(flower_name)
        for item in flower_names:
            if item == flower_name:
                return render_template('flower-add.html')
        flower_mean = request.form['flower_mean']
        flower_imprice = request.form['flower_imprice']
        flower_exprice = request.form['flower_exprice']
        flower_num = request.form['flower_num']
        flower_sale = request.form['flower_sale']
        InsertFlowerData(flower_name, flower_mean, flower_imprice, flower_exprice, flower_num, flower_sale)
        sql = "SELECT * FROM flower"
        cursor.execute(sql)
        content = [tuple(item.encode('latin-1').decode('gbk') if isinstance(item, str) else item for item in row) for row in
                cursor.fetchall()]
        columns = [column[0] for column in cursor.description]
        print(columns)
        print(content)
        return render_template('flower-list.html', labels=columns, content=content)
    return render_template('flower-add.html')


@bp.route('/delflower', methods=['GET', 'POST'])
def deleteFlower():
    if request.method == 'POST':
        # print("OK")
        argument = request.form.get('id')
        # print(argument)
        sql = "delete from flower where flower_id='" + argument + "'"
        # print(sql)
        cursor.execute(sql)
    sql = "SELECT * FROM flower"
    cursor.execute(sql)
    content = [tuple(item.encode('latin-1').decode('gbk') if isinstance(item, str) else item for item in row) for
               row in
               cursor.fetchall()]
    columns = [column[0] for column in cursor.description]
    # print(columns)
    # print(content)
    return render_template('flower-list.html', labels=columns, content=content)


# @bp.route('/delete/flower', methods=['GET', 'POST'])
# def delFlower():
#     flower_id=
#     sql = "delete from flower where flower_id='"+flower_id+"'"
#     cursor.execute(sql)
#     sql = "SELECT * FROM flower"
#     cursor.execute(sql)
#     content = [tuple(item.encode('latin-1').decode('gbk') if isinstance(item, str) else item for item in row) for row in
#                cursor.fetchall()]
#     columns = [column[0] for column in cursor.description]
#     # print(columns)
#     # print(content)
#     return render_template('flower-list.html', labels=columns, content=content)


# @bp.route('/add/flower', methods=['GET', 'POST'])
# def addFlower():
#     if request.method == 'POST':
#         flower_name = request.form['keyword']
#         print(keyword)
#         if client.client_null(id, password):
#             login_massage = "温馨提示：账号和密码是必填"
#             return render_template('index.html', message=login_massage)
#         elif client.client_select(id, password):
#             return render_template('test.html', username=id)
#     return render_template('index.html')
#     flower_id=
#     sql = "delete from flower where flower_id='"+flower_id+"'"
#     cursor.execute(sql)
#     sql = "SELECT * FROM flower"
#     cursor.execute(sql)
#     content = [tuple(item.encode('latin-1').decode('gbk') if isinstance(item, str) else item for item in row) for row in
#                cursor.fetchall()]
#     columns = [column[0] for column in cursor.description]
#     # print(columns)
#     # print(content)
#     return render_template('flower-list.html', labels=columns, content=content)
