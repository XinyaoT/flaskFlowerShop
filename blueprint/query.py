from flask import Blueprint, render_template, redirect, url_for
from flask import request

from flaskFlowerShop.config import cursor
from flaskFlowerShop.function.function_tzq.tools import createMessageTuple, createClientTuple, createFlowerTuple, \
    getFlowerBySort

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
                    tuple(item.encode('gbk').decode('gbk') if isinstance(item, str) else item for item in row) for
                    row in cursor.fetchall()]
                columns = [column[0] for column in cursor.description]
                return render_template('message.html', labels=columns, content=content)
                break
    sql = "SELECT * FROM message"
    cursor.execute(sql)
    content = [tuple(item.encode('gbk').decode('gbk') if isinstance(item, str) else item for item in row) for row in
               cursor.fetchall()]
    columns = [column[0] for column in cursor.description]
    print(columns)
    print(content)
    return render_template('message.html', labels=columns, content=content)


@bp.route('/client', methods=['GET', 'POST'])
def queryClient():
    if request.method == 'POST':
        client = request.form['client']
        # print(keyword)
        clients = createClientTuple()
        # print(keyword)
        # print(keywords)
        for item in clients:
            if item == client:
                sql = "SELECT * FROM client WHERE client_id='" + client + "'"
                # print("true")
                cursor.execute(sql)
                content = [
                    tuple(item.encode('gbk').decode('gbk') if isinstance(item, str) else item for item in row) for
                    row in cursor.fetchall()]
                columns = [column[0] for column in cursor.description]
                return render_template('member-list.html', labels=columns, content=content)
    sql = "SELECT * FROM client"
    cursor.execute(sql)
    content = [tuple(item.encode('gbk').decode('gbk') if isinstance(item, str) else item for item in row) for row in
               cursor.fetchall()]
    columns = [column[0] for column in cursor.description]
    # print(columns)
    # print(content)
    return render_template('member-list.html', labels=columns, content=content)


@bp.route('/flower', methods=['GET', 'POST'])
def queryFlower():
    # if request.method == 'GET':
    #     print("OK")
    #     action = request.args.get('action')
    #     print(action)
    #     if action == 'add':
    #         return redirect(url_for('manager.addFlower', _external=True))
    #     else:
    #         return redirect(url_for('manager.deleteFlower'))
    if request.method == 'GET':
        flowername = request.args.get('flowername')
        # print(flowername)
        flowernames = createFlowerTuple()
        # print(flowernames)
        # print(flowername)
        for item in flowernames:
            if item == flowername:
                sql = "SELECT * FROM flower WHERE flower_name='" + flowername + "'"
                # print("true")
                cursor.execute(sql)
                content = [
                    tuple(item.encode('gbk').decode('gbk') if isinstance(item, str) else item for item in row) for
                    row in cursor.fetchall()]
                columns = [column[0] for column in cursor.description]
                return render_template('flower-list.html', labels=columns, content=content)
    sql = "SELECT * FROM flower"
    cursor.execute(sql)
    # 获取查询结果
    results = cursor.fetchall()
    print(results)
    # 将结果转化为列表形式，并为每一行添加属性
    content = []
    for row in results:
        # 将每一行转化为字典形式，并添加属性
        row_dict = {column[0]: item.encode('gbk').decode('gbk') if isinstance(item, str) else item for column, item in
                    zip(cursor.description, row)}
        row_dict['sorts'] = getFlowerBySort(row[0])  # 添加新属性
        # 为了将cursor值导回flower表
        sql = "SELECT * FROM flower"
        cursor.execute(sql)
        print(row_dict)
        content.append(row_dict)
    print(content)
    result_tuples = [tuple(d.values()) for d in content]
    print("content")
    print(content)
    return render_template('flower-list.html', content=result_tuples)


