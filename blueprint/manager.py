from flask import Blueprint, render_template, request, redirect, url_for

from config import cursor, conn
from function.function_tzq.tools import DataOrderAnalyse, OrderFlower, DataMessageAnalyse, InsertNoticeData, \
    createFlowerTuple, InsertFlowerData
from function.function_tzq.word import wordcloud

bp = Blueprint("manager", __name__, url_prefix="/manager")


@bp.route('/')
def welcome():
    return render_template('manage.html')

@bp.route('/index')
def welcome_index():
    parameter_value1 = DataOrderAnalyse()
    parameter_value2 = OrderFlower(1)
    parameter_value3 = OrderFlower(0)
    parameter_value4 = DataMessageAnalyse()
    print(parameter_value1, parameter_value2, parameter_value3, parameter_value4)
    image_base64 = wordcloud()
    return render_template('welcome.html', parameter1=parameter_value1, parameter2=parameter_value2,
                           parameter3=parameter_value3, parameter4=parameter_value4, initial_image_data=image_base64)

@bp.route('/flower/oderbyex')
def orderFlowerEx():
    sql = "SELECT * FROM flower ORDER BY flower_sale DESC"
    cursor.execute(sql)
    content = [tuple(item.encode('gbk').decode('gbk') if isinstance(item, str) else item for item in row) for row in
               cursor.fetchall()]
    columns = [column[0] for column in cursor.description]
    # print(columns)
    # print(content)
    return render_template('flower-list.html', labels=columns, content=content)


@bp.route('/flower/oderbynum')
def orderFlowerNum():
    sql = "SELECT * FROM flower ORDER BY flower_num DESC"
    cursor.execute(sql)
    content = [tuple(item.encode('gbk').decode('gbk') if isinstance(item, str) else item for item in row) for row in
               cursor.fetchall()]
    columns = [column[0] for column in cursor.description]
    # print(columns)
    # print(content)
    return render_template('flower-list.html', labels=columns, content=content)


# 发布公告
@bp.route('/notice', methods=['GET', 'POST'])
def notice():
    # 传参方式
    # /post?message=xxxxxxx
    # return render_template("contact.html")
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        print(title)
        InsertNoticeData(title, content)
    return render_template("notice.html")


# 删除消息
@bp.route('/delmessage', methods=['GET', 'POST'])
def delMessage():
    if request.method == 'POST':
        try:
            print("OK")
            argument = request.form.get('id')
            print(argument)

            # 使用参数化查询
            sql = "DELETE FROM message WHERE message_id = ?"
            cursor.execute(sql, (argument,))

            # 提交事务
            conn.commit()
            print("Delete operation successful")
        except Exception as e:
            # 发生异常时进行错误处理
            conn.rollback()  # 回滚事务
            print("Delete operation failed:", str(e))

    sql = "SELECT * FROM message"
    cursor.execute(sql)
    content = [tuple(item.encode('gbk').decode('gbk') if isinstance(item, str) else item for item in row) for
               row in
               cursor.fetchall()]
    columns = [column[0] for column in cursor.description]
    # print(columns)
    print(content)
    return render_template('message.html', labels=columns, content=content)


# 增加花朵
@bp.route('/addflower', methods=['GET', 'POST'])
def addFlower():
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
        content = [tuple(item.encode('gbk').decode('gbk') if isinstance(item, str) else item for item in row) for row in
                   cursor.fetchall()]
        columns = [column[0] for column in cursor.description]
        print(columns)
        print(content)
        return render_template('flower-list.html', labels=columns, content=content)
    return render_template('flower-add.html')

# 删除花朵，暂不实现
# @bp.route('/delflower/flower_id=<flower_id>', methods=['GET', 'POST'])
# def deleteFlower(flower_id):
#     print(flower_id)
#     sql = "DELETE FROM flower WHERE flower_id='" + flower_id + "'"
#     print(sql)
#     cursor.execute(sql)
#     sql = "SELECT * FROM flower"
#     cursor.execute(sql)
#     content = [tuple(item.encode('gbk').decode('gbk') if isinstance(item, str) else item for item in row) for
#                row in
#                cursor.fetchall()]
#     columns = [column[0] for column in cursor.description]
#     print(columns)
#     print(content)
#     return render_template('flower-list.html', labels=columns, content=content)


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
