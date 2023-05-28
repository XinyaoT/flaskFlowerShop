import wordcloud as wc
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import tools
import jieba

with open("改革开放 科技创新.txt", mode="r", encoding="utf-8") as fp:
    content = fp.read()
results = jieba.lcut(content)
text = " ".join(results)


# 打开图像并转换为灰度图像
image = Image.open("flower.png")

# 将图像转换为numpy数组并确保其数据类型为浮点数
mask = np.array(image)

# sql = "SELECT message_key FROM message"
# tools.cursor.execute(sql)
# results = tools.cursor.fetchall()
# key_list = [result[0].encode('latin-1').decode('gbk') for result in results]
# text = " ".join(key_list)


def wordcloud():
    # image.show()
    # print(text)
    word_cloud = wc.WordCloud(font_path="方正粗黑宋简体.ttf", background_color="white", mask=mask)
    word_cloud.generate(text)

    plt.imshow(word_cloud)
    plt.axis("off")
    plt.show()
