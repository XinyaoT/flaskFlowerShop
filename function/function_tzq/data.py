# -*- coding: utf-8 -*-


# 创建语句："IF OBJECT_ID('" + table_create + "') IS NOT NULL DROP TABLE " + table_create + " CREATE TABLE "+
# table_create + table_content
# 插入语句："INSERT INTO " + table_insert + " VALUES " + value_insert
# 删除语句："delete " + table_del + " where " + condition_del
# 修改语句："update [" + table_up + "] set " + result_up + " where " + condition_up
# 查询语句："SELECT * FROM " + table_sel
# 条件选择语句："SELECT " + col_name + " FROM " + table_ana + " WHERE " + condition_ana
# 排序语句："SELECT * FROM " + table_name + " ORDER BY " + col_name
# 关联查询语句："SELECT " + col_select + " FROM " + ord_table + " INNER JOIN " + inner_table + " ON " + condition_select
import datetime
import shortuuid

from blueprint.message import post


message_id = "m" + shortuuid.ShortUUID(alphabet='0123456789').random(length=7)
c_id = 'c1111111'
m_time = datetime.datetime.now().strftime("%Y-%m-%d")
message, key, nickname = post()
record = (message_id, c_id, message, m_time, key, nickname)

# 操作数据
table1 = 'Flower'
value_insert1 = '(%s, %s, %s)'
data_insert1 = [
    (100, 'sort1', 'description1'),
    (200, 'sort2', 'description2'),
    (300, 'sort3', 'description3')
]
table_content1 = """(
        sortID int primary key,
        sortName varchar(20) not null,
        sortDes varchar(50) not null ,
        )"""
condition_del1 = 'sortID=100'
result_up1 = "sortName ='name'"
condition_up1 = 'sortID>200'

# message数据
# 创建message
message_id1 = "m" + shortuuid.ShortUUID(alphabet='0123456789').random(length=7)
message_id2 = "m" + shortuuid.ShortUUID(alphabet='0123456789').random(length=7)
message_id3 = "m" + shortuuid.ShortUUID(alphabet='0123456789').random(length=7)
message_id4 = "m" + shortuuid.ShortUUID(alphabet='0123456789').random(length=7)
message_id5 = "m" + shortuuid.ShortUUID(alphabet='0123456789').random(length=7)
c_id1 = 'c1111111'
c_id2 = 'c2222222'
c_id3 = 'c3333333'
c_id4 = 'c4444444'
c_id5 = 'c5555555'
m_time1 = datetime.datetime.now().strftime("%Y-%m-%d")
m_time2 = datetime.datetime.now().strftime("%Y-%m-%d")
m_time3 = datetime.datetime.now().strftime("%Y-%m-%d")
m_time4 = datetime.datetime.now().strftime("%Y-%m-%d")
m_time5 = datetime.datetime.now().strftime("%Y-%m-%d")
data_mes_insert = [
    (message_id1, c_id1, '母亲节买了一束康乃馨送给妈妈，妈妈很开心', m_time1, '母亲节', '小田'),
    (message_id2, c_id2, '母亲节买了一束康乃馨送给妈妈，妈妈夸我长大了', m_time2, '母亲节', '小张'),
    (message_id3, c_id3, '情人节买了一束玫瑰送给女朋友，她很开心', m_time3, '情人节', '小黄'),
    (message_id4, c_id4, '圣诞节买了一束康乃馨送给妈妈', m_time4, '圣诞节', '小吴'),
    (message_id5, c_id5, '母亲节买了一束康乃馨送给妈妈', m_time5, '母亲节', '小李'),
    record
]
# 删除message
c_id = "'c5555555'"
condition_mes_del = c_id

# 数据分析
case = 0


notice_id1 = "n" + shortuuid.ShortUUID(alphabet='0123456789').random(length=7)
notice_id2 = "n" + shortuuid.ShortUUID(alphabet='0123456789').random(length=7)
notice_id3 = "n" + shortuuid.ShortUUID(alphabet='0123456789').random(length=7)
a_id1 = 'a1111111'
a_id2 = 'a2222222'
a_id3 = 'a3333333'
m_time1 = datetime.datetime.now().strftime("%Y-%m-%d")
m_time2 = datetime.datetime.now().strftime("%Y-%m-%d")
m_time3 = datetime.datetime.now().strftime("%Y-%m-%d")
data_not_insert = [
    (notice_id1, a_id1, '母亲节', '母亲节到了，买了一束康乃馨送给妈妈吧，她会很开心', m_time1),
    (notice_id2, a_id2, '情人节', '情人节到了，买了一束玫瑰花送给女朋友吧，她会很开心', m_time2),
    (notice_id3, a_id3, '圣诞节', '圣诞节到了，买了一束郁金香送给朋友吧，她会很开心', m_time3),
]
