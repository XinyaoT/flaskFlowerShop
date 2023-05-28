# -*- coding: utf-8 -*-ji

from tools import postMessage, delMessage, analyseFlower, cursor, conn, selOrder, postNotice
from word import wordcloud


def main():
    postMessage()
    # delMessage()
    analyseFlower()
    selOrder()
    postNotice()
    # 关闭数据库连接
    cursor.close()
    conn.close()
    wordcloud()


if __name__ == '__main__':
    main()
