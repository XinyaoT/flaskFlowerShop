# 该部分只涉及到一个生成词云图片的函数

import wordcloud as wc
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import jieba
import io
import base64



def wordcloud():
    # 打开图像并转换为灰度图像
    image = Image.open("flower.png")

    # 将图像转换为numpy数组并确保其数据类型为浮点数
    mask = np.array(image)




# 这部分只是为了测试，因为数据库数据不够，画出来的图形会不美观，看不出花朵的形状
    with open("改革开放 科技创新.txt", mode="r", encoding="utf-8") as fp:
        content = fp.read()
    results = jieba.lcut(content)
    text = " ".join(results)
# 真正使用时只需要注释掉上面的代码，运行这段代码就行
    # sql = "SELECT message_key FROM message"
    # tools.cursor.execute(sql)
    # results = tools.cursor.fetchall()
    # key_list = [result[0].encode('gbk').decode('gbk') for result in results]
    # text = " ".join(key_list)
    # image.show()
    # print(text)




    word_cloud = wc.WordCloud(font_path="方正粗黑宋简体.ttf", background_color="white", mask=mask)
    word_cloud.generate(text)

    plt.imshow(word_cloud)
    plt.axis("off")
    plt.show()
    # 保存词云图像为图片文件
    word_cloud.to_file("wordcloud.png")
    # 假设您已经生成了词云图像，保存为wordcloud.png
    image_path = 'wordcloud.png'
    # 打开图像文件
    open_image = Image.open(image_path)
    # 将图像转换为字节流
    image_byte_array = io.BytesIO()
    open_image.save(image_byte_array, format='PNG')
    image_byte_array = image_byte_array.getvalue()
    # 将图像字节流转换为Base64编码
    image_base64 = base64.b64encode(image_byte_array).decode('utf-8')
    return image_base64
